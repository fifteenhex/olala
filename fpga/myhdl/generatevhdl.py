from top import *
import common

notramcs = Signal(bool(1))

interrupts = Signal(intbv(not 0)[8:])

top = toVHDL(Top, common.clk,
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
             notramcs,
             common.ipl,
             common.notoe,
             common.notuwe,
             common.notlwe,
             common.notberr,
             common.notavec,
             common.leds,
             common.rx,
             common.tx,
             common.baudout)
