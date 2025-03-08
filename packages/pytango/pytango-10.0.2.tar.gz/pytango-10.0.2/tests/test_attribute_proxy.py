# SPDX-FileCopyrightText: All Contributors to the PyTango project
# SPDX-License-Identifier: LGPL-3.0-or-later
import time
from functools import partial

import pytest

from tango import (
    DevState,
    AttributeProxy,
    GreenMode,
    DevFailed,
    EventType,
    AttrWriteType,
)
from tango.asyncio import AttributeProxy as asyncio_AttributeProxy
from tango.gevent import AttributeProxy as gevent_AttributeProxy
from tango.futures import AttributeProxy as futures_AttributeProxy

from tango.server import Device, attribute, command

from tango.test_utils import assert_close, DeviceTestContext, MultiDeviceTestContext
from tango.utils import EventCallback, AsyncEventCallback


TEST_VALUES = {
    "scalar_int": (2, 3, 4, 5, 6),
    "spectrum_str": (["c", "d"], ["e", "f"], ["g", "h"], ["i", "j"], ["k", "l"]),
    "image_float": (
        [[15.5, 16.6], [17.7, 18.8]],
        [[19.9, 20.0], [21.1, 22.2]],
        [[23.3, 24.4], [25.5, 26.6]],
        [[27.7, 28.8], [29.9, 30.0]],
        [[31.1, 32.2], [33.3, 34.4]],
    ),
}

ATTRIBUTES_TO_TEST = list(TEST_VALUES.keys())

attribute_proxy_map = {
    GreenMode.Synchronous: AttributeProxy,
    GreenMode.Futures: futures_AttributeProxy,
    GreenMode.Asyncio: partial(asyncio_AttributeProxy, wait=True),
    GreenMode.Gevent: gevent_AttributeProxy,
}

# Tests


class EasyEchoDevice(Device):

    scalar_int_value = 1
    spectrum_str_value = ["a", "b"]
    image_float_value = [[1.1, 2.2], [3.3, 4.4]]

    def init_device(self):
        self.set_state(DevState.ON)

    @attribute(access=AttrWriteType.READ_WRITE)
    def scalar_int(self) -> int:
        return self.scalar_int_value

    @scalar_int.setter
    def set_scalar_int(self, new_value):
        self.scalar_int_value = new_value

    @attribute(access=AttrWriteType.READ_WRITE)
    def spectrum_str(self) -> tuple[str, str]:
        return self.spectrum_str_value

    @spectrum_str.setter
    def set_spectrum_str(self, new_value):
        self.spectrum_str_value = new_value

    @attribute(access=AttrWriteType.READ_WRITE)
    def image_float(self) -> tuple[tuple[float, float], tuple[float, float]]:
        return self.image_float_value

    @image_float.setter
    def set_image_float(self, new_value):
        self.image_float_value = new_value


devices_info = ({"class": EasyEchoDevice, "devices": [{"name": "test/dev/main"}]},)


@pytest.fixture(params=ATTRIBUTES_TO_TEST)
def attribute_proxy(request):
    with MultiDeviceTestContext(devices_info=devices_info):
        proxy = AttributeProxy(f"test/dev/main/{request.param}")
        assert proxy.__repr__() == proxy.__str__() == f"AttributeProxy({request.param})"
        yield proxy


def test_ping(attribute_proxy):
    duration = attribute_proxy.ping(wait=True)
    assert isinstance(duration, int)


def test_state_status(attribute_proxy):
    state = attribute_proxy.state(wait=True)
    assert isinstance(state, DevState)

    status = attribute_proxy.status(wait=True)
    assert status == f"The device is in {state} state."


def test_read_write_attribute(attribute_proxy):
    values = TEST_VALUES[attribute_proxy.name()]
    attribute_proxy.write(values[0], wait=True)
    assert_close(attribute_proxy.read(wait=True).value, values[0])
    assert_close(attribute_proxy.write_read(values[1], wait=True).value, values[1])


def test_attribute_poll(attribute_proxy):
    poll_period = 0.1  # sec
    values = TEST_VALUES[attribute_proxy.name()]

    _assert_polling_can_be_started(attribute_proxy, poll_period)
    _wait_until_middle_of_a_polling_period(attribute_proxy, poll_period)

    t_start = time.time()
    history = _write_values_and_read_via_polling(attribute_proxy, poll_period, values)
    t_end = time.time()

    _assert_polling_can_be_stopped(attribute_proxy)
    _assert_reading_times_increase_monotonically_within_limits(history, t_start, t_end)
    _assert_reading_values_match(history, values)


def _assert_polling_can_be_started(attribute_proxy, poll_period_sec):
    poll_period_msec = round(poll_period_sec * 1000)
    assert not attribute_proxy.is_polled()
    attribute_proxy.poll(poll_period_msec)
    assert attribute_proxy.is_polled()
    assert attribute_proxy.get_poll_period() == poll_period_msec


def _assert_polling_can_be_stopped(attribute_proxy):
    attribute_proxy.stop_poll()
    assert not attribute_proxy.is_polled()


def _wait_until_middle_of_a_polling_period(attribute_proxy, poll_period_sec):
    # wait for first reading to arrive in the polling history buffer
    nap_time = poll_period_sec / 10.0
    retries = 20
    while retries > 0:
        try:
            attribute_proxy.history(1)
            break
        except DevFailed:
            # history not ready yet
            time.sleep(nap_time)
            retries -= 1
    is_polling_working = retries > 0
    assert is_polling_working
    # now wait half the polling period, so we are midway through
    time.sleep(poll_period_sec / 2.0)


def _write_values_and_read_via_polling(attribute_proxy, poll_period_sec, values):
    for value in values:
        attribute_proxy.write(value)
        time.sleep(poll_period_sec)
    return attribute_proxy.history(len(values))


def _assert_reading_times_increase_monotonically_within_limits(history, t_start, t_end):
    t_previous = t_start
    for reading in history:
        t_current = reading.time.totime()
        assert t_previous < t_current < t_end
        t_previous = t_current


def _assert_reading_values_match(history, values):
    assert_close([read.value for read in history], values)


max_reply_attempts = 10
delay = 0.1


def test_read_write_attribute_async(attribute_proxy):
    value = TEST_VALUES[attribute_proxy.name()][0]
    w_id = attribute_proxy.write_asynch(value, wait=True)
    got_reply, attempt = False, 0
    while not got_reply:
        try:
            attribute_proxy.write_reply(w_id, wait=True)
            got_reply = True
        except DevFailed:
            attempt += 1
            if attempt >= max_reply_attempts:
                raise RuntimeError(
                    f"Test failed: cannot get write reply within {max_reply_attempts*delay} sec"
                )
            time.sleep(delay)

    r_id = attribute_proxy.read_asynch(wait=True)
    got_reply, attempt = False, 0
    while not got_reply:
        try:
            ret = attribute_proxy.read_reply(r_id, wait=True)
            got_reply = True
        except DevFailed:
            attempt += 1
            if attempt >= max_reply_attempts:
                raise RuntimeError(
                    f"Test failed: cannot get read reply within {max_reply_attempts*delay} sec"
                )
            time.sleep(delay)

    assert_close(ret.value, value)


class EasyEventDevice(Device):
    def init_device(self):
        self.set_change_event("attr", True, False)

    @attribute
    def attr(self) -> int:
        return 1

    @command
    def send_event(self):
        self.push_change_event("attr", 2)


@pytest.mark.parametrize("green_mode", GreenMode.values.values())
def test_event(green_mode):
    with DeviceTestContext(EasyEventDevice, device_name="test/device/1", process=True):
        proxy = attribute_proxy_map[green_mode]("test/device/1/attr")
        cb = (
            AsyncEventCallback() if green_mode == GreenMode.Asyncio else EventCallback()
        )
        eid = proxy.subscribe_event(EventType.CHANGE_EVENT, cb, wait=True)
        proxy.get_device_proxy().command_inout("send_event", wait=True)
        if green_mode == GreenMode.Gevent:
            # I do not understand it, but with Gevent somehow we don't get the
            # second event. It is a bug and has to be fixed. As a workaround,
            # waiting on another device proxy call helps.
            proxy.get_device_proxy().command_inout("state", wait=True)
        evts = cb.get_events()
        rep = 0
        while len(evts) < 2 and rep < 50:
            rep += 1
            evts = cb.get_events()
            time.sleep(0.1)
        if len(evts) < 2:
            pytest.fail(f"Cannot receive events in {green_mode}")
        assert_close([evt.attr_value.value for evt in evts[:2]], [1, 2])
        proxy.unsubscribe_event(eid, wait=True)
