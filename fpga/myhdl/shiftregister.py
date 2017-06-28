from myhdl import *

"""
    dir == 0
    sin -> pin
    dir == 1
    pout -> sout """


def ShiftRegister(clk, rst, dir, pin, pout, sin, sout):
    incounter = Signal(modbv(0, 0, len(pin)))
    outcounter = Signal(modbv(0, 0, len(pout)))
    inbits = [Signal(bool(0)) for i in range(len(pin))]
    datain = ConcatSignal(*list(reversed(inbits)))

    @always_comb
    def poutlogic():
        pin.next = datain

    @always_seq(clk.posedge, reset=rst)
    def counter():
        incounter.next = incounter + 1
        outcounter.next = outcounter + 1

    @always_seq(clk.posedge, reset=rst)
    def shiftin():
        if dir == 0:
            inbits[incounter].next = sin

    @always_seq(clk.posedge, reset=rst)
    def shifout():
        if dir == 1:
            sout.next = pout[outcounter + 1:outcounter]


    return counter, shifout, shiftin