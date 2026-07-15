# Midnight 911 for Home Assistant

[![HA and HACS Validate](https://github.com/midnight-security/ha-midnight-noo/actions/workflows/ha_and_hacs_validate.yml/badge.svg)](https://github.com/midnight-security/ha-midnight-noo/actions/workflows/ha_and_hacs_validate.yml)
[![hacs_badge](https://img.shields.io/badge/HACS-Default-orange.svg)](https://github.com/hacs/integration)

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris.

> **Note:** This integration is currently available in the United States only.

---

## How it Works

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.

Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident.

---

## Installation

### HACS (Recommended)

1. Open HACS in your Home Assistant instance
2. Go to **Integrations**
3. Click the **+** button and search for "Midnight 911"
4. Click **Install**
5. Restart Home Assistant

### Manual

1. Copy the `custom_components/midnight_alerts` folder to your Home Assistant `custom_components` directory
2. Restart Home Assistant

---

## Configuration

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Add the integration via **Settings > Devices & Services > Add Integration** and search for "Midnight 911".

| Parameter | Required | Description |
|-----------|----------|-------------|
| `api_key` | Yes | Your Midnight Security API key |

---

## Usage

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Once configured, a **Trigger Alert** button entity will appear in your Home Assistant dashboard.

### Automation Example

```yaml
automation:
  - alias: "Lorem ipsum trigger alert"
    trigger:
      - platform: state
        entity_id: binary_sensor.your_sensor
        to: "on"
    action:
      - service: button.press
        target:
          entity_id: button.midnight_911_trigger_alert
```

---

## Warnings & Disclaimers

Requires an Internet connection! Home Assistant must have an active internet connection for this to work!

NO GUARANTEE
This integration is provided as-is without warranties of any kind. Using Noonlight with Home Assistant involves multiple service providers and potential points of failure, including (but not limited to) your internet service provider, 3rd party hosting services such as Amazon Web Services, and the Home Assistant software platform. Please read and understand the [Midnight terms of use](https:www.midnight.security/#tou) and [Home Assistant Terms of Service](https://www.home-assistant.io/tos/) both of which include important limitations of liability and indemnification provisions.

---

## License

Copyright 2026 Midnight Security

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
