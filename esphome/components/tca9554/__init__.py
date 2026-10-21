import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import i2c

tca9554_ns = cg.esphome_ns.namespace("tca9554")
TCA9554 = tca9554_ns.class_("TCA9554", cg.Component, i2c.I2CDevice)

CONFIG_SCHEMA = cv.Schema({
    cv.GenerateID(): cv.declare_id(TCA9554),
    cv.Required("address"): cv.i2c_address,
})

def to_code(config):
    var = cg.new_Pvariable(config[cv.GenerateID()])
    cg.register_component(var, config)
    cg.register_i2c_device(var, config)
