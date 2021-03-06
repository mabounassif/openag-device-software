# Import standard python libraries
import os, sys, pytest, threading

# Set system path
sys.path.append(os.environ["PROJECT_ROOT"])

# Import mux simulator
from device.utilities.communication.i2c.mux_simulator import MuxSimulator

# Import peripheral driver
from device.peripherals.modules.atlas_co2.driver import AtlasCo2Driver


def test_init() -> None:
    driver = AtlasCo2Driver(
        name="Test",
        i2c_lock=threading.RLock(),
        bus=2,
        address=0x77,
        simulate=True,
        mux_simulator=True,
    )


def test_read_co2() -> None:
    driver = AtlasCo2Driver(
        name="Test",
        i2c_lock=threading.RLock(),
        bus=2,
        address=0x77,
        simulate=True,
        mux_simulator=True,
    )
    co2 = driver.read_co2()
    assert co2 == 490.0
