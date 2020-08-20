import pytest


from sengen.data_generator import SensorDataGenerator as sdg


def test_sensor_data_gen():
    dg = sdg()
    dg.generation_input.add_option(sensor_names="HelloGauss",
                                   distribution="normal",
                                   mu=0,
                                   sigma=1)
    dg.generate(sample_size=1000)
