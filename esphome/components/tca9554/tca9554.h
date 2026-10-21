#pragma once

#include "esphome.h"
#include "esphome/components/i2c/i2c.h"

namespace esphome {
namespace tca9554 {

class TCA9554 : public Component, public i2c::I2CDevice {
 public:
  void setup() override {
    // Configure all 8 pins as outputs (0 = output)
    write_register(0x03, 0x00);

    // Initialize output register to all OFF
    state_ = 0x00;
    write_register(0x01, state_);
  }

  void set_pin(uint8_t pin, bool value) {
    if (value)
      state_ |= (1 << pin);
    else
      state_ &= ~(1 << pin);

    write_register(0x01, state_);
  }

 protected:
  uint8_t state_{0};

  void write_register(uint8_t reg, uint8_t value) {
    uint8_t data[2] = {reg, value};
    this->write(data, 2);
  }
};

}  // namespace tca9554
}  // namespace esphome
