from myhdl import *

import common

RESETCLOCKS = 8 * 2

counter = Signal(modbv(0, max=1024))
cycle = Signal(modbv(0, max=1024))


def ClkDriver(clk, COUNTERROLLOVER):
    halfperiod = delay(20)

    @always(halfperiod)
    def logic():
        clk.next = not clk
        if counter % 2 == 0:
            cycle.next = cycle + 1
        if (COUNTERROLLOVER == -1 or counter < COUNTERROLLOVER):
            counter.next = counter + 1
        else:
            counter.next = 0

    return logic


def ResetDriver():
    @always_comb
    def logic():
        if counter > RESETCLOCKS:
            common.sysreset.next = not common.sysreset.active
        else:
            common.sysreset.next = common.sysreset.active

    return logic