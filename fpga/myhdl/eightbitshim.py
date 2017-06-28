from myhdl import *


""" datain -- the data coming into the module
    dataout -- the data going out of the module
    bytein -- the byte coming into the module
    byteout -- the byte going out of the module
"""


def EightBitShim(datain, dataout, bytein, byteout):
    lowerbyteout = Signal(intbv(0)[8:])
    intdataout = ConcatSignal(byteout, lowerbyteout)

    @always_comb
    def logic():
        bytein.next = datain[16:8]
        dataout.next = intdataout

    return logic