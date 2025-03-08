"""Gecko inMix accessory class."""

from __future__ import annotations

import asyncio
import logging
from re import A
from typing import TYPE_CHECKING, Any

from geckolib.automation.light import GeckoLight
from geckolib.automation.power import GeckoPower
from geckolib.automation.select import GeckoSelect

if TYPE_CHECKING:
    from geckolib.automation.async_facade import GeckoAsyncFacade
    from geckolib.driver.accessor import (
        GeckoByteStructAccessor,
        GeckoEnumStructAccessor,
    )

_LOGGER = logging.getLogger(__name__)

ATTR_RGBCOLOR = "rgb_color"
ATTR_BRIGHTNESS = "brightness"
ZONE_KEY_NONE = "None"

"""
    Notes:

    InMix-Color[n]: If not NO_COLOR, then InMix-Mode[n] must be STATIC


"""


class GeckoInMixZone(GeckoLight):
    """Class for an inMix light."""

    def __init__(self, facade: GeckoAsyncFacade, inmix: GeckoInMix, zone: int) -> None:
        """Initialize the Li light."""
        super().__init__(facade, f"Zone {zone}", f"InMixZone{zone}")
        if zone <= inmix.number_of_zones:
            self.set_availability(is_available=True)
        else:
            return

        self._synchro_accessor: GeckoEnumStructAccessor = self.facade.spa.accessors[
            f"InMix-Synchro{zone}"
        ]
        self._mode_accessor: GeckoEnumStructAccessor = self.facade.spa.accessors[
            f"InMix-Mode{zone}"
        ]
        self._color_accessor: GeckoEnumStructAccessor = self.facade.spa.accessors[
            f"InMix-Color{zone}"
        ]
        self._speed_accessor: GeckoEnumStructAccessor = self.facade.spa.accessors[
            f"InMix-Speed{zone}"
        ]
        self._red_accessor: GeckoByteStructAccessor = self.facade.spa.accessors[
            f"InMix-RedLevel{zone}"
        ]
        self._green_accessor: GeckoByteStructAccessor = self.facade.spa.accessors[
            f"InMix-GreenLevel{zone}"
        ]
        self._blue_accessor: GeckoByteStructAccessor = self.facade.spa.accessors[
            f"InMix-BlueLevel{zone}"
        ]

        # Set accessors for direct struct update, and watch them
        for accessor in [
            self._synchro_accessor,
            self._mode_accessor,
            self._color_accessor,
            self._speed_accessor,
            self._red_accessor,
            self._green_accessor,
            self._blue_accessor,
        ]:
            accessor.direct_update = True
            accessor.watch(self._on_change)

        self._brightness = 255
        self._zone = zone
        self._get_inmix()
        self._ignore_changes = False

    @property
    def is_on(self) -> bool:
        """Determine if the light is on or not."""
        return self._mode_accessor.value != "STATIC"

    @property
    def rgb_color(self) -> tuple[int, int, int] | None:
        """Get the RGB colour."""
        if self.is_on:
            return self._rgb
        return None

    @property
    def brightness(self) -> int | None:
        """Get the zone brightness."""
        if self.is_on:
            return self._brightness
        return None

    @property
    def zone_key(self) -> str:
        """Get the zone key."""
        return f"ZONE{self._zone}"

    @property
    def synchro(self) -> str:
        """Get this zone sync value."""
        return self._synchro_accessor.value

    async def set_synchro(self, zone: GeckoInMixZone | None) -> None:
        """Set the zone sync value."""
        if zone is None:
            await self._synchro_accessor.async_set_value(self.zone_key)
            return
        if self.zone_key == zone.zone_key:
            return
        if zone.is_on:
            await self.async_turn_on(
                **{ATTR_BRIGHTNESS: zone.brightness, ATTR_RGBCOLOR: zone.rgb_color}
            )
            return
        await self.async_turn_off()

    @property
    def is_synchro(self) -> bool:
        """Is this zone synchro with another."""
        return self.synchro != self.zone_key

    @property
    def state(self) -> Any:
        """Get the state of the light."""
        if self.is_on:
            return f"RGB({self._rgb}) {int(self._brightness * 100 / 255)}%"
        return "OFF"

    async def _set_rgb(self, rgb: tuple[int, int, int], brightness: int) -> None:
        _LOGGER.debug("Set RGB %s %s", rgb, brightness)
        self._rgb = rgb
        self._brightness = brightness
        await self._set_inmix()

    async def _set_brightness(self, brightness: int) -> None:
        _LOGGER.debug("Set brightness %d", brightness)
        self._brightness = brightness
        await self._set_inmix()

    async def _set_inmix(self) -> None:
        self._ignore_changes = True
        await self._mode_accessor.async_set_value("RGB")
        rgb = self._rgb
        br = self._brightness
        await self._red_accessor.async_set_value(int(rgb[0] * br / 255))
        await self._green_accessor.async_set_value(int(rgb[1] * br / 255))
        await self._blue_accessor.async_set_value(int(rgb[2] * br / 255))
        self._ignore_changes = False
        self._on_change()

    async def async_turn_on(self, **kwargs: Any) -> None:
        """Turn the light ON, but does nothing if it is already ON."""
        _LOGGER.info("On %s", kwargs)
        brightness = kwargs.get(ATTR_BRIGHTNESS, self._brightness)
        if ATTR_RGBCOLOR in kwargs:
            rgb = kwargs.get(ATTR_RGBCOLOR)
            await self._set_rgb(rgb, brightness)
            return
        if ATTR_BRIGHTNESS in kwargs:
            await self._set_brightness(brightness)
            return
        if self.is_on:
            return
        await self._mode_accessor.async_set_value("RGB")

    async def async_turn_off(self, **_kwargs: Any) -> None:
        """Turn the light OFF, but does nothing if it is already OFF."""
        if not self.is_on:
            return
        await self._mode_accessor.async_set_value("STATIC")

    def _get_inmix(self) -> None:
        rgb = (
            self._red_accessor.value,
            self._green_accessor.value,
            self._blue_accessor.value,
        )
        _LOGGER.debug("get_inmix: Got %s", rgb)
        self._brightness: int = max(1, *rgb)
        # Scale the colours from the apparent brightness
        self._rgb = (
            int(255 * rgb[0] / self._brightness),
            int(255 * rgb[1] / self._brightness),
            int(255 * rgb[2] / self._brightness),
        )
        _LOGGER.debug("scaled %s", self._rgb)

    def _on_change(
        self, sender: Any = None, old_value: Any = None, new_value: Any = None
    ) -> None:
        if self._ignore_changes:
            return
        self._get_inmix()
        super()._on_change(sender, old_value, new_value)


class GeckoInMixSynchro(GeckoSelect):
    """Class for the synchro setting."""

    def __init__(self, facade: GeckoAsyncFacade, inmix: GeckoInMix) -> None:
        """Initialize the sync class."""
        super().__init__(facade, "Zone Syncronization", "INMIXSYNC")
        if inmix.number_of_zones == 1:
            return
        self.set_availability(is_available=True)

        # Set of mappings of constants to UI options. There must be at
        # least 2 zones
        mappings = {
            ZONE_KEY_NONE: "None",
            inmix.zone_1.zone_key: "With Zone 1",
            inmix.zone_2.zone_key: "With Zone 2",
        }
        if inmix.number_of_zones == 3:  # noqa: PLR2004
            mappings[inmix.zone_3.zone_key] = "With Zone 3"
        self.set_mapping(mappings)

        self._inmix = inmix
        self._lookup: dict = {ZONE_KEY_NONE: None}
        for zone in inmix.zones:
            self._lookup[zone.zone_key] = zone
            zone.watch(self._on_zone_change)

        self._state = ZONE_KEY_NONE
        self._ignore_changes = False

    def _on_zone_change(
        self, _sender: Any = None, _old_value: Any = None, _new_value: Any = None
    ) -> None:
        if self._ignore_changes:
            return
        try:
            for zone in self._inmix.zones:
                if zone.is_synchro:
                    self._state = zone.synchro
                    return
            self._state = ZONE_KEY_NONE
        finally:
            self._on_change(None, None, None)

    @property
    def state(self) -> str:
        """Get the current state via the mapping."""
        return self.mapping[self._state]

    async def async_set_state(self, new_state: str) -> None:
        """Set the state of the select entity."""
        if new_state in self.reverse:
            new_state = self.reverse[new_state]
        self._state = new_state
        try:
            self._ignore_changes = True
            for zone in self._inmix.zones:
                await zone.set_synchro(self._lookup[self._state])
        finally:
            self._ignore_changes = False

    @property
    def states(self) -> list[str]:
        """Get the possible states."""
        return list(self.mapping.values())


class GeckoInMix(GeckoPower):
    """Gecko inMix support class."""

    def __init__(self, facade: GeckoAsyncFacade) -> None:
        """Initialize the inMix class."""
        super().__init__(facade, "inMix", "INMIX")
        if "InMix-PackType" not in facade.spa.accessors:
            return

        self.struct_begin = facade.spa.struct.inmix_log_class.begin

        self.number_of_zones: int = int(
            facade.spa.accessors["InMix-NumberOfZones"].value
        )
        _LOGGER.debug("Spa has an inMix accessory with %d zones", self.number_of_zones)

        self.set_availability(is_available=True)

        self.zone_1 = GeckoInMixZone(facade, self, 1)
        self.zone_2 = GeckoInMixZone(facade, self, 2)
        self.zone_3 = GeckoInMixZone(facade, self, 3)
        self.syncro = GeckoInMixSynchro(facade, self)

        #
        #   If one zone, then no synchro available
        #   Each zone either preset or user selected
        #   RGB 0-255 per normal
        #

        self.zone_1.watch(self._on_change)
        self.zone_2.watch(self._on_change)
        self.zone_3.watch(self._on_change)
        self.syncro.watch(self._on_change)

        # Start task for
        # facade.taskmanager.add_task(self._in
        facade.taskmanager.add_task(self._inmix_update(), "inix Update", "FACADE")
        self._update_event = asyncio.Event()

    async def _inmix_update(self) -> None:
        _LOGGER.debug("inMix update task started")
        try:
            while True:
                await self._update_event.wait()

                _LOGGER.debug("Perform struct update")
                block_size = len(self.zones) * 7
                data = self.facade.spa.struct.status_block[
                    self.struct_begin : self.struct_begin + block_size
                ]
                await self.facade.spa.async_on_set_value(
                    self.struct_begin, block_size, data
                )
                self._update_event.clear()

        except asyncio.CancelledError:
            _LOGGER.debug("Facade update loop cancelled")
            raise
        except Exception:
            _LOGGER.exception("Facade update loop caught execption")
            raise

    @property
    def zones(self) -> list[GeckoInMixZone]:
        """Get the available zones."""
        return [
            zone
            for zone in [self.zone_1, self.zone_2, self.zone_3]
            if zone.is_available
        ]

    def _on_change(
        self, sender: Any = None, old_value: Any = None, new_value: Any = None
    ) -> None:
        self._update_event.set()
        return super()._on_change(sender, old_value, new_value)
