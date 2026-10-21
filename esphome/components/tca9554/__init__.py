import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import i2c

tca9554_ns = cg.esphome_ns.namespace("tca9554")
TCA9554 = tca9554_ns.class_("TCA9554", cg.Component, i2c.I2CDevice)

CONFIG_SCHEMA = i2c.i2c_device_schema().extend({
    cv.GenerateID(): cv.declare_id(TCA9554),
})

async def to_code(config):
    var = cg.new_Pvariable(config[cv.GenerateID()])
    await cg.register_component(var)
    await i2c.register_i2c_device(var, config)
