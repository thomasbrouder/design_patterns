class RemoteControl():
    """
    The "abstraction" defines the interface for the "control"
    part of the two class hierarchies. It maintains a reference
    to an object of the "implementation" hierarchy and delegates
    all of the real work to this object.
    """
    def __init__(self, device: "Device"):
        self._device = device

    def toggle_power(self):
        if self._device.is_enabled():
            self._device.disable()
            print(f"{self._device.name} power OFF")

        else:
            self._device.enable()
            print(f"{self._device.name} power ON")

    def volume_down(self):
        self._device.set_volume(self._device.get_volume() - 10)
        print(f"{self._device.name} volume set to {self._device.get_volume()}")

    def volume_up(self):
        self._device.set_volume(self._device.get_volume() + 10)
        print(f"{self._device.name} volume set to {self._device.get_volume()}")

    def channel_down(self):
        self._device.set_channel(self._device.get_channel() - 1)
        print(f"{self._device.name} channel set to {self._device.get_channel()}")

    def channel_up(self):
        self._device.set_channel(self._device.get_channel() + 1)
        print(f"{self._device.name} channel set to {self._device.get_channel()}")


class AdvancedRemoteControl(RemoteControl):
    """
    You can extend classes from the abstraction hierarchy
    independently from device classes.
    """
    def __init__(self, device: "Device"):
        self._device = device

    def mute(self):
        self._device.set_volume(0)
        print(f"MUTE: {self._device.name} volume set to 0")


class Device():
    """
    The "implementation" interface declares methods common to all
    concrete implementation classes. It doesn't have to match the
    abstraction's interface. In fact, the two interfaces can be
    entirely different. Typically the implementation interface
    provides only primitive operations, while the abstraction
    defines higher-level operations based on those primitives.
    """
    def __init__(self, name):
        self._is_enabled = False
        self._channel = 1
        self._volume = 50
        self.name = name

    def is_enabled(self):
        return self._is_enabled

    def enable(self):
        self._is_enabled = True

    def disable(self):
        self._is_enabled = False

    def get_volume(self):
        return self._volume

    def set_volume(self, percent):
        self._volume = percent

    def get_channel(self):
        return self._channel

    def set_channel(self, channel):
        self._channel = channel


"""
All devices follow the same interface.
"""


class Tv(Device):
    pass


class Radio(Device):
    pass


"""Somewhere in client code."""
if __name__ == '__main__':
    tv = Tv(name="TV")
    tv_remote = RemoteControl(tv)
    tv_remote.toggle_power()
    tv_remote.volume_up()
    tv_remote.volume_up()
    tv_remote.volume_up()
    tv_remote.channel_up()

    radio = Radio(name="radio")
    radio_remote = AdvancedRemoteControl(radio)
    radio_remote.volume_up()
    radio_remote.volume_up()
    radio_remote.volume_up()
    radio_remote.volume_up()
    tv_remote.volume_down()
    tv_remote.volume_down()
    tv_remote.volume_down()

    tv_remote.channel_up()
    tv_remote.toggle_power()
