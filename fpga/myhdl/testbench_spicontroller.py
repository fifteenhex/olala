import os

import common
import testbenchcommon
import systemconstants
from spicontroller import *


WRITETEST_SETUPDATA = testbenchcommon.RESETCLOCKS + 2
WRITETEST_LOWERCS = WRITETEST_SETUPDATA + 2
WRITETEST_LOWERWE = WRITETEST_LOWERCS + 2
WRITETEST_RAISEWE = WRITETEST_LOWERWE + 2
WRITETEST_RAISECS = WRITETEST_RAISEWE + 2


def BusDriver():
    @always_comb
    def logic():
        if (testbenchcommon.counter == WRITETEST_SETUPDATA):
            common.addr.next = 0x100002
            datain.next = 0xFFFF
        elif (testbenchcommon.counter == WRITETEST_LOWERCS):
            notcs.next = False
        elif (testbenchcommon.counter == WRITETEST_LOWERWE):
            common.notuwe.next = 0
        elif (testbenchcommon.counter == WRITETEST_RAISEWE):
            common.notuwe.next = 1
        elif (testbenchcommon.counter == WRITETEST_RAISECS):
            notcs.next = True

    return logic


datain = Signal(intbv(0)[systemconstants.DATABUSBITS:])
dataout = TristateSignal(intbv(0)[systemconstants.DATABUSBITS:])
notcs = Signal(bool(1))
readstrobe = Signal(bool(1))

clkdrv = testbenchcommon.ClkDriver(common.clk, -1)
resetdrv = testbenchcommon.ResetDriver()
busdrv = BusDriver()

if os.path.isfile('./SPIController.vcd'):
    os.remove('./SPIController.vcd')
tbspicont = traceSignals(SPIController,
                         common.clk,
                         common.sysreset,
                         common.addr,
                         datain,
                         dataout.driver(),
                         notcs,
                         common.notoe,
                         common.notuwe,
                         common.flashmiso,
                         common.flashmosi,
                         common.flashclk,
                         common.flashcs
                         )

sim = Simulation(clkdrv, resetdrv, busdrv, tbspicont)
sim.run(1000000)