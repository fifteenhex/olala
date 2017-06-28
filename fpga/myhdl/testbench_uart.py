import os

import common
import testbenchcommon
import systemconstants
from uart import *


WRITETEST_SETUPDATA = testbenchcommon.RESETCLOCKS + 2
WRITETEST_LOWERCS = WRITETEST_SETUPDATA + 2
WRITETEST_LOWERWE = WRITETEST_LOWERCS + 2
WRITETEST_RAISEWE = WRITETEST_LOWERWE + 2
WRITETEST_RAISECS = WRITETEST_RAISEWE + 2


def BusDriver():
    @always_comb
    def logic():
        if (testbenchcommon.counter == WRITETEST_SETUPDATA):
            common.addr.next = 0x100000
            datain.next = 0xAAAA
        elif (testbenchcommon.counter == WRITETEST_LOWERCS):
            notcs.next = False
        elif (testbenchcommon.counter == WRITETEST_LOWERWE):
            common.notuwe.next = 0
        elif (testbenchcommon.counter == WRITETEST_RAISEWE):
            common.notuwe.next = 1
        elif (testbenchcommon.counter == WRITETEST_RAISECS):
            notcs.next = True

    return logic


def RXDriver():
    clkcounter = Signal(modbv(0, 0, 16))
    bitcounter = Signal(modbv(0, 0, 10))

    @always_seq(common.baudout.posedge, reset=common.sysreset)
    def logic():
        if (bitcounter == 0):
            common.rx.next = False
        else:
            common.rx.next = True

        if (clkcounter + 1) % clkcounter.max == 0:
            bitcounter.next = bitcounter + 1
        clkcounter.next = clkcounter + 1

    return logic


datain = Signal(intbv(0)[systemconstants.DATABUSBITS:])
dataout = TristateSignal(intbv(0)[systemconstants.DATABUSBITS:])
notcs = Signal(bool(1))
readstrobe = Signal(bool(1))

clkdrv = testbenchcommon.ClkDriver(common.clk, -1)
resetdrv = testbenchcommon.ResetDriver()
busdrv = BusDriver()
rxdrv = RXDriver()

if os.path.isfile('./Uart.vcd'):
    os.remove('./Uart.vcd')
tbuart = traceSignals(Uart,
                      common.clk,
                      common.sysreset,
                      common.rx,
                      common.tx,
                      common.notoe,
                      common.notuwe,
                      notcs,
                      common.addr,
                      datain,
                      dataout.driver(),
                      common.baudout,
                      readstrobe)

sim = Simulation(clkdrv, resetdrv, busdrv, rxdrv, tbuart)
sim.run(1000000)