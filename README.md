# ESPHome TCA9554 Component

This is a minimal ESPHome external component for the TCA9554PWR
8-bit I2C GPIO expander used on Waveshare ESP32-S3-ETH-8DI-8RO-C boards.

## Usage

```yaml
external_components:
  - source: github://meneerwouters-source/tca9554

tca9554:
  id: relay_expander
  address: 0x20
