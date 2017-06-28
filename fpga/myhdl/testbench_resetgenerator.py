import os

import common
import testbenchcommon
from resetgenerator import *


clkdrv = testbenchcommon.ClkDriver(common.clk)
resetdrv = testbenchcommon.ResetDriver()

os.remove('./ResetGenerator.vcd')
tbrstgen = traceSignals(ResetGenerator, common.clk, common.sysreset, common.notcpureset, common.notcpuhalt)

sim = Simulation(clkdrv, resetdrv, tbrstgen)
sim.run(1000000)