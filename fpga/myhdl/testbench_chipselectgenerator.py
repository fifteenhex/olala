import os

import common
import testbenchcommon
import systemconstants
from chipselectgenerator import *


chipselects = Signal(intbv(0)[16:])


def BusDriver():
    @always_comb
    def logic():
        if testbenchcommon.counter % 2 == 0:
            common.notas.next = 0
        else:
            common.notas.next = 1
            common.addr.next = (testbenchcommon.counter // 2) * ((1024 * 1024) / systemconstants.BUSBYTES)

    return logic


clkdrv = testbenchcommon.ClkDriver(common.clk)
resetdrv = testbenchcommon.ResetDriver()
busdrv = BusDriver()

os.remove('./ChipSelectGenerator.vcd')
tbchipselectgenerator = traceSignals(ChipSelectGenerator, common.notas, common.addr, chipselects)

sim = Simulation(clkdrv, resetdrv, busdrv, tbchipselectgenerator)
sim.run(10000)