from top import *
import common
import testbenchcommon


def BusDriver():
    @always_comb
    def logic():
        common.addr.next = testbenchcommon.cycle
        common.notas.next = testbenchcommon.cycle % 2 == 0
        common.rnotw.next = 1

    return logic


cs = Signal(bool(True))

clkdrv = testbenchcommon.ClkDriver(common.clk)

busdrv = BusDriver()
tbtop = traceSignals(BootRom, common.addr, common.data.driver(), common.rnotw, cs)

# os.remove('./Bootrom.vcd')
sim = Simulation(clkdrv, busdrv, tbtop)
sim.run(100000)