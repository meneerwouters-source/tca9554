import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import i2c

tca9554_ns = cg.esphome_ns.namespace("tca9554")
TCA9554 = tca9554_ns.class_("TCA9554", cg.Component, i2c.I2CDevice)

CONFIG_SCHEMA = i2c.i2c_device_schema(0x20).extend({
    cv.GenerateID(): cv.declare_id(TCA9554),
})

async def to_code(config):
    var = cg.new_Pvariable(config[cv.GenerateID()])

    # Register component with EMPTY config (no schema)
    await cg.register_component(var, {})

    # Register I2C device with full config
    await i2c.register_i2c_device(var, config)
