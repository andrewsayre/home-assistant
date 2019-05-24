"""Test setup and fixtures for the firmata integration."""
from asynctest.mock import Mock, patch as patch
import pytest

from homeassistant.components.firmata import CONF_BOARDS
from homeassistant.components.firmata.const import DOMAIN, CONF_SERIAL_PORT
from homeassistant.const import CONF_NAME


@pytest.fixture(name="config")
def config_fixture():
    """Create configuration for testing."""
    return {
        DOMAIN: {
            CONF_BOARDS: [
                {
                    CONF_NAME: "Test Board",
                    CONF_SERIAL_PORT: "/dev/ttyACM0"
                }
            ]
        }
    }

@pytest.fixture(name="board")
def board_fixture():
    """Create a mock PymataCore instance."""
    with patch("homeassistant.components.firmata.board.PymataCore", autospec=True) as mock:
        mock_board = mock.return_value
        yield mock_board
