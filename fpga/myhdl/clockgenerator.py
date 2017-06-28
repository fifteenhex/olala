from myhdl import *


def ClockGenerator(clk, cpuclock, reset, dividerbit):
    cpuclockcounterwidth = 2
    counter = Signal(modbv(~0)[cpuclockcounterwidth:])

    @always_comb
    def bleah():
        cpuclock.next = True if (counter[dividerbit + 1: dividerbit] == 1) else False

    @always_seq(clk.posedge, reset=reset)
    def cpuclockgen():
        counter.next = counter + 1

    return bleah, cpuclockgen
