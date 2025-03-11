import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
import pytest
from dotenv import load_dotenv
from eg4_inverter_api import EG4InverterAPI, EG4AuthError, EG4APIError

# Load environment variables for testing
load_dotenv(".env")

USERNAME = os.getenv("EG4_USERNAME")
PASSWORD = os.getenv("EG4_PASSWORD")
SERIAL_NUMBER = os.getenv("EG4_SERIAL_NUMBER")
PLANT_ID = os.getenv("EG4_PLANT_ID")
BASE_URL = os.getenv("EG4_BASE_URL", "https://monitor.eg4electronics.com")
IGNORE_SSL = os.getenv("EG4_DISABLE_VERIFY_SSL", "1") == "1"

@pytest.mark.asyncio
async def test_login():
    """Test successful login."""

    api = EG4InverterAPI(USERNAME, PASSWORD, BASE_URL)
    await api.login(ignore_ssl=IGNORE_SSL)
    api.set_selected_inverter(inverterIndex=0)
    assert api.jsessionid is not None
    data = await api.get_inverter_runtime_async()
    assert data.success
    assert data.statusText is not None

    await api.close()

@pytest.mark.asyncio
async def test_get_inverter_runtime():
    """Test retrieving inverter runtime data."""
    api = EG4InverterAPI(USERNAME, PASSWORD, BASE_URL)
    await api.login(ignore_ssl=IGNORE_SSL)
    api.set_selected_inverter(inverterIndex=0)
    data = await api.get_inverter_runtime_async()
    assert data.success
    assert data.statusText is not None
    await api.close()

@pytest.mark.asyncio
async def test_get_inverter_energy():
    """Test retrieving inverter energy data."""
    api = EG4InverterAPI(USERNAME, PASSWORD, BASE_URL)
    await api.login(ignore_ssl=IGNORE_SSL)
    api.set_selected_inverter(inverterIndex=0)
    data = await api.get_inverter_energy_async()
    assert data.success
    await api.close()

@pytest.mark.asyncio
async def test_invalid_login():
    """Test handling of invalid credentials."""
    api = EG4InverterAPI(USERNAME, "xxx", BASE_URL)
    with pytest.raises(EG4AuthError):
        await api.login(ignore_ssl=IGNORE_SSL)

@pytest.mark.asyncio
async def test_get_inverter_battery():
    """Test retrieving inverter battery data."""
    api = EG4InverterAPI(USERNAME, PASSWORD, BASE_URL)
    await api.login(ignore_ssl=IGNORE_SSL)
    api.set_selected_inverter(inverterIndex=0)
    data = await api.get_inverter_battery_async()
    assert data.remainCapacity is not None
    await api.close()