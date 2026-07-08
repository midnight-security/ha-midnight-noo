"""Midnight Alerts integration."""
from homeassistant.core import HomeAssistant
from homeassistant.config_entries import ConfigEntry

DOMAIN = "midnight_alerts"

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up Midnight Alerts."""
    hass.data.setdefault(DOMAIN, {})
    return True
