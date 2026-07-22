"""Midnight Alerts integration."""
from homeassistant.core import HomeAssistant
from homeassistant.config_entries import ConfigEntry
from homeassistant.exceptions import ConfigEntryAuthFailed, ConfigEntryNotReady
from homeassistant.helpers.aiohttp_client import async_get_clientsession
from homeassistant.loader import async_get_integration

from .api import MidnightAlertsApiClient, MidnightAlertsApiError, MidnightAlertsAuthError
from .const import CONF_ENABLE_CRASH_REPORTING, DOMAIN, CONF_API_KEY

PLATFORMS = ["button"]


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up Midnight Alerts."""
    integration = await async_get_integration(hass, DOMAIN)
    client = MidnightAlertsApiClient(
        entry.data[CONF_API_KEY],
        async_get_clientsession(hass),
        report_errors=entry.options.get(CONF_ENABLE_CRASH_REPORTING, False),
        release=str(integration.version) if integration.version else None,
    )

    try:
        await client.async_validate()
    except MidnightAlertsAuthError as err:
        raise ConfigEntryAuthFailed("Invalid Midnight Alerts API key") from err
    except MidnightAlertsApiError as err:
        raise ConfigEntryNotReady(f"Error connecting to Midnight Alerts: {err}") from err

    hass.data.setdefault(DOMAIN, {})
    hass.data[DOMAIN][entry.entry_id] = client
    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    unloaded = await hass.config_entries.async_unload_platforms(entry, PLATFORMS)
    if unloaded:
        hass.data[DOMAIN].pop(entry.entry_id, None)
    return unloaded
