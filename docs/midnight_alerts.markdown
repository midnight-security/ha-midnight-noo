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
