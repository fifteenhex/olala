import os

from shiftregister import *
import common
import testbenchcommon


clkdrv = testbenchcommon.ClkDriver(common.clk, -1)
rstdriver = testbenchcommon.ResetDriver()

dir = Signal(bool(True))
pin = Signal(intbv(0)[8:])
pout = Signal(intbv(0xAAAA)[8:])
sin = Signal(bool(False))
sout = Signal(bool(False))

if os.path.isfile('./ShiftRegister.vcd'):
    os.remove('./ShiftRegister.vcd')
tbsr = traceSignals(ShiftRegister,
                    common.clk,
                    common.sysreset,
                    dir,
                    pin,
                    pout,
                    sin,
                    sout,
                    )

sim = Simulation(tbsr, clkdrv, rstdriver)
sim.run(1000000)