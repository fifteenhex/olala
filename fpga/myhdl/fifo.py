from myhdl import *


def Fifo(DEPTH, WIDTH, rst, datain, dataout, full, empty, push, pop, cspush, cspop, fill):
    inpointer = Signal(modbv(0, 0, DEPTH))
    outpointer = Signal(modbv(0, 0, DEPTH))
    mem = [Signal(intbv(0)[WIDTH:]) for i in range(DEPTH)]

    @always_comb
    def filllogic():
        if (inpointer == outpointer):
            fill.next = 0
        elif (inpointer > outpointer):
            fill.next = inpointer - outpointer
        else:
            fill.next = (inpointer.max - outpointer) + inpointer

    @always_comb
    def emptylogic():
        empty.next = True if (inpointer == outpointer) else False

    @always_comb
    def fulllogic():
        full.next = True if ((inpointer + 1) % inpointer.max) == outpointer else False

    @always_seq(push.posedge, reset=rst)
    def datainlogic():
        if (cspush == False):
            mem[inpointer].next = datain
            if full == False:
                inpointer.next = inpointer + 1

    @always_comb
    def dataoutlogic():
        dataout.next = mem[outpointer]

    @always_seq(pop.posedge, reset=rst)
    def poplogic():
        if cspop == False and empty == False:
            outpointer.next = outpointer + 1

    return filllogic, emptylogic, fulllogic, datainlogic, poplogic, dataoutlogic