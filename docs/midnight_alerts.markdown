---
title: Midnight 911
description: Instructions on how to set up the Midnight 911 integration.
ha_category:
  - Safety
ha_release: 0.4.0
ha_iot_class: Cloud Push
ha_config_flow: true
ha_codeowners:
  - '@midnight-security/midnight-team'
ha_domain: midnight_alerts
ha_platforms:
  - button
ha_integration_type: service
---

> **DRAFT** — this file is a working draft of the documentation that will be
> submitted to [home-assistant/home-assistant.io](https://github.com/home-assistant/home-assistant.io)
> once the integration meets Bronze tier and moves toward Home Assistant
> Core. See [`CORE_INTEGRATION.md`](../CORE_INTEGRATION.md) for the full
> checklist. Front matter fields (`ha_release`, etc.) will need updating at
> submission time to match whatever's actually true then.

The **Midnight 911** integration connects Home Assistant to
[Midnight Security](https://www.midnight.security), a professional security
monitoring service. It lets you add a button or automation that sends an
alert to Midnight's US-based monitoring center. Midnight works in
partnership with [RapidSOS](https://www.rapidsos.com) to validate alerts and
reach the 911 center associated with your address, contacting local
emergency services on your behalf if the alert is validated or goes without
a response from you.

<div class='note warning'>

This integration can result in a real dispatch to emergency services.
Configure and test it carefully, and always keep your monitored address
up to date.

</div>

## Use cases

A common setup is wiring the **Trigger Alert** button into an automation
instead of pressing it directly — for example, triggering it when a
glass-break or smoke sensor fires and nobody dismisses the automation's
confirmation prompt within a couple of minutes. This gives you a monitored
safety net on top of sensors Home Assistant already has, without needing a
dedicated alarm panel.

## Prerequisites

1. Sign up for a [Midnight Security](https://www.midnight.security) account.
2. Generate an API key from your Midnight Security account.
3. Make sure Home Assistant has an active internet connection — it must be
   able to reach Midnight's API for both setup and alert delivery.

{% include integrations/config_flow.md %}

## Configuration

During setup you'll be asked for:

| Field | Description |
| --- | --- |
| API Key | The API key from your Midnight Security account. |

Once configured, the integration provides a **Trigger Alert** button entity.
Pressing it (directly, or via an automation) sends an alert to Midnight's
monitoring center for the address on file with your account.

## Supported functions

| Entity | Type | Description |
| --- | --- | --- |
| Trigger Alert | Button | Sends an alert to Midnight's monitoring center for the address on your account. This is the integration's only entity. |

## Data updates

This integration is push-only (`cloud_push`) — it never polls Midnight or
fetches state on a schedule. Pressing **Trigger Alert** (directly or via
automation) sends a single request to Midnight's API at that moment; there
is no ongoing background communication otherwise.

## Examples

A typical automation triggers the alert button when a security-relevant
sensor fires without being acknowledged, for example:

```yaml
automation:
  - alias: "Escalate unacknowledged glass break to Midnight"
    trigger:
      - trigger: state
        entity_id: binary_sensor.living_room_glass_break
        to: "on"
    condition:
      - condition: state
        entity_id: input_boolean.alert_acknowledged
        state: "off"
    action:
      - delay: "00:02:00"
      - condition: state
        entity_id: input_boolean.alert_acknowledged
        state: "off"
      - action: button.press
        target:
          entity_id: button.midnight_911_trigger_alert
```

<div class='note'>

There isn't yet a published blueprint for this on the community blueprint
exchange — the YAML above is a starting point to adapt, not a ready-made
blueprint link.

</div>

## Troubleshooting

### Can't set up the integration

#### Symptom: "Invalid API key"

The config flow shows an `invalid_auth` error.

##### Resolution

Double-check the API key was copied in full from your Midnight Security
account, with no extra whitespace. If it still fails, generate a new key
and try again.

#### Symptom: "Failed to connect to Midnight Alerts"

The config flow shows a `cannot_connect` error.

##### Resolution

1. Confirm Home Assistant has an active internet connection.
2. Check [Midnight Security's status](https://www.midnight.security) for
   any ongoing service disruption.
3. Try again after a few minutes.

### Pressing the button doesn't seem to do anything

Check the Home Assistant logs for `custom_components.midnight_alerts` — a
failed alert logs an error there rather than surfacing a UI notification.
This is almost always the same connectivity or account issue as above,
just happening at alert time instead of setup time.

## Removing the integration

This integration follows standard integration removal. After removing it,
no further alerts can be sent by Home Assistant until it's re-added.

{% include integrations/remove_device_service.md %}

Removing the integration from Home Assistant does not cancel your Midnight
Security account or monitoring plan — manage or cancel that separately at
[midnight.security](https://www.midnight.security).

## Availability

- **United States** only today, with Canada planned.
- Requires an active internet connection at the time an alert is triggered.

## Known limitations

- No automatic re-delivery or retry queue on temporary connectivity loss —
  a failed alert must be triggered again once connectivity is restored.
- Only a single Midnight Security account (config entry) is supported per
  Home Assistant instance.
