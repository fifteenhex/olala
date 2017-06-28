import math

from myhdl import *

import systemconstants


SIZE = 1024 * 2  # 2k
ADDRESSBITS = int(math.log(SIZE, 2)) - 1


def BootRAM(addr, dataout, datain, notcs, notoe, notuwe, notlwe):
    memu = [Signal(intbv(0)[8:]) for i in range(SIZE / systemconstants.BUSBYTES)]
    meml = [Signal(intbv(0)[8:]) for i in range(SIZE / systemconstants.BUSBYTES)]

    ub = Signal(intbv(0)[8:])
    lb = Signal(intbv(0)[8:])
    intdataout = ConcatSignal(ub, lb)

    @always(notuwe.posedge)
    def writeu():
        if (notcs == 0):  # and datain != None):
            memu[addr[ADDRESSBITS:]].next = datain[16:8]

    @always(notlwe.posedge)
    def writel():
        if (notcs == 0):  # and datain != None):
            meml[addr[ADDRESSBITS:]].next = datain[8:]

    @always_comb
    def merge():
        ub.next = memu[addr[ADDRESSBITS:]]
        lb.next = meml[addr[ADDRESSBITS:]]

    @always_comb
    def read():
        if (notcs == 0 and notoe == 0):
            dataout.next = intdataout
        else:
            dataout.next = None

    return writeu, writel, merge, read