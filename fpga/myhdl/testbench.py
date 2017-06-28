import os

from top import *
import common
import testbenchcommon


def BusDriver():
    datain = common.data.driver()

    @always_comb
    def logic():
       # if (common.notcpureset == 1):
            buscycle = (testbenchcommon.cycle // 4) % 4
            if (buscycle == 0):
                common.addr.next = 0x100000
            elif buscycle == 1:
                common.notas.next = 0
                common.rnotw.next = 0
                common.notuds.next = 0
            elif buscycle == 3:
                common.notas.next = 1
                common.rnotw.next = 1
                common.notuds.next = 1

            if (common.rnotw == 1):
                datain.next = None
            else:
                datain.next = 0


    return logic


clkdrv = testbenchcommon.ClkDriver(common.clk, -1)
rstdrv = testbenchcommon.ResetDriver()

busdrv = BusDriver()

os.remove("./Top.vcd")
tbtop = traceSignals(Top, common.clk,
                     common.cpuclock,
                     common.sysreset,
                     common.button,
                     common.notcpureset,
                     common.notcpuhalt,
                     common.notas,
                     common.rnotw,
                     common.notuds,
                     common.notlds,
                     common.dtack,
                     common.notbr,
                     common.notbg,
                     common.addr,
                     common.data,
                     common.notramcs,
                     common.ipl,
                     common.notoe,
                     common.notuwe,
                     common.notlwe,
                     common.notberr,
                     common.leds,
                     common.rx,
                     common.tx)

sim = Simulation(clkdrv, rstdrv, busdrv, tbtop)
sim.run(400000)