from myhdl import *


def BusGlue(notas, rnotw, notuds, notlds, dtack, notbr, notbg, notoe, notuwe, notlwe, readstrobe):
    @always_comb
    def logic():
        notoe.next = not rnotw
        readstrobe.next = not (rnotw and not notuds)
        notuwe.next = not ((not rnotw) and (not notuds))
        notlwe.next = not ((not rnotw) and (not notlds))

    return logic


