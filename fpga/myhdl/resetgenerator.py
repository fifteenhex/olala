from myhdl import *


def OpenDrainOutput(input, output):
    outputdriver = output.driver()

    @always_comb
    def logic():
        if input == False:
            outputdriver.next = False
        else:
            outputdriver.next = None

    return logic


def ResetGenerator(clk, notsysreset, notcpureset, notcpuhalt, internalreset):
    resetclocks = 127
    counter = Signal(modbv(0, min=0, max=resetclocks + 1))

    notcpuhalt.read = True
    notcpureset.read = True

    intnotcpureset = Signal(bool(0))
    intnotcpuhalt = Signal(bool(0))

    resetod = OpenDrainOutput(intnotcpureset, notcpureset)
    haltod = OpenDrainOutput(intnotcpuhalt, notcpuhalt)

    @always_seq(clk.posedge, reset=notsysreset)
    def logic():
        if counter < resetclocks:
            counter.next = counter + 1
        if counter >= resetclocks:
            intnotcpureset.next = True
            intnotcpuhalt.next = True
            internalreset.next = not internalreset.active

    return resetod, haltod, logic