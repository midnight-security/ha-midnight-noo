"""Config flow for Midnight Alerts."""
import voluptuous as vol
from homeassistant import config_entries
from homeassistant.core import callback
from homeassistant.data_entry_flow import FlowResult
from homeassistant.helpers.aiohttp_client import async_get_clientsession

from .api import MidnightAlertsApiClient, MidnightAlertsApiError, MidnightAlertsAuthError
from .const import CONF_ENABLE_CRASH_REPORTING, DOMAIN, CONF_API_KEY

DATA_SCHEMA = vol.Schema({
    vol.Required(CONF_API_KEY): str,
})


class MidnightAlertsConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Midnight Alerts."""

    VERSION = 1

    async def async_step_user(self, user_input=None) -> FlowResult:
        """Handle the initial step."""
        errors = {}

        if user_input is not None:
            client = MidnightAlertsApiClient(
                user_input[CONF_API_KEY], async_get_clientsession(self.hass)
            )
            try:
                await client.async_validate()
            except MidnightAlertsAuthError:
                errors["base"] = "invalid_auth"
            except MidnightAlertsApiError:
                errors["base"] = "cannot_connect"
            else:
                await self.async_set_unique_id(DOMAIN)
                self._abort_if_unique_id_configured()
                return self.async_create_entry(title="Midnight 911", data=user_input)

        return self.async_show_form(
            step_id="user",
            data_schema=DATA_SCHEMA,
            errors=errors,
        )

    @staticmethod
    @callback
    def async_get_options_flow(
        config_entry: config_entries.ConfigEntry,
    ) -> "MidnightAlertsOptionsFlow":
        """Create the options flow."""
        return MidnightAlertsOptionsFlow()


class MidnightAlertsOptionsFlow(config_entries.OptionsFlowWithReload):
    """Handle options for Midnight Alerts."""

    async def async_step_init(self, user_input=None) -> FlowResult:
        """Manage the options."""
        if user_input is not None:
            return self.async_create_entry(title="", data=user_input)

        return self.async_show_form(
            step_id="init",
            data_schema=vol.Schema(
                {
                    vol.Optional(
                        CONF_ENABLE_CRASH_REPORTING,
                        default=self.config_entry.options.get(
                            CONF_ENABLE_CRASH_REPORTING, False
                        ),
                    ): bool,
                }
            ),
        )
