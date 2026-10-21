import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import i2c

tca9554_ns = cg.esphome_ns.namespace("tca9554")
TCA9554 = tca9554_ns.class_("TCA9554", cg.Component, i2c.I2CDevice)

# Component schema (only the component itself)
COMPONENT_SCHEMA = cv.Schema({
    cv.GenerateID(): cv.declare_id(TCA9554),
})

# I2C schema (address + i2c_id)
I2C_SCHEMA = i2c.i2c_device_schema(0x20)

# Combined schema
CONFIG_SCHEMA = COMPONENT_SCHEMA.extend(I2C_SCHEMA)

async def to_code(config):
    # Component part
    comp_conf = COMPONENT_SCHEMA(config)
    var = cg.new_Pvariable(comp_conf[cv.GenerateID()])

    # Register component with its own config
    await cg.register_component(var, comp_conf)

    # Register I2C device with the I2C part of the config
    await i2c.register_i2c_device(var, I2C_SCHEMA(config))
