from prorityencoder import *


def InterruptController(ipl,
                        nmi,
                        systickint,
                        uartint):
    interruptspad = Signal(modbv(0)[5:])
    interrupts = ConcatSignal(nmi, interruptspad, systickint, uartint)

    intipl = Signal(intbv(0)[len(ipl):])
    ntonencoder = PriorityEncoder(interrupts, intipl)

    @always_comb
    def logic():
        ipl.next = ~intipl

    return ntonencoder, logic
