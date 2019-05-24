"""Tests for the firmata init module."""
from asynctest import patch
import pytest

from homeassistant.components.firmata.const import DOMAIN
from homeassistant.const import STATE_OFF, ATTR_FRIENDLY_NAME
from homeassistant.setup import async_setup_component


async def test_async_setup_loads_platform(hass, board, config):
    """Test component setup loads the switch platform."""
    assert await async_setup_component(hass, DOMAIN, config)
    await hass.async_block_till_done()

    state = hass.states.get("switch.test_board")
    assert state is not None
    assert state.state == STATE_OFF
    assert state.attributes[ATTR_FRIENDLY_NAME] == "Test Board"
