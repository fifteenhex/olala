from fifo import *


def SPIController(clk, rst, addr, datain, dataout, notcs, notoe, notwe, si, so, sck, scs):
    states = enum('TRANSFER_IDLE', 'TRANSFER_LOWERCS', 'TRANSFER_TRANSFER', 'TRANSFER_RAISECS')

    ADDR_FIFO = 0
    ADDR_STATUS = 1
    ADDR_TRANSFERSIZE = 2

    addrbits = addr(3, 0)

    transfercounter = Signal(modbv(0, 0, 256))
    transferbitcounter = Signal(modbv(0, 0, 8))
    transferstate = Signal(states.TRANSFER_IDLE)

    fullin = Signal(bool(0))
    fullout = Signal(bool(0))
    emptyin = Signal(bool(0))
    emptyout = Signal(bool(0))
    pushin = Signal(bool(1))
    popout = Signal(bool(1))
    fillin = Signal(intbv(0))
    fillout = Signal(intbv(0))

    fifocs = Signal(bool(1))
    popcsout = Signal(bool(1))
    pushcsin = Signal(bool(0))


    # fifo for data going to the slave
    fifoout = Fifo(256, 8, rst, datain, dataout, fullout, emptyout, notwe, popout, fifocs, popcsout, fillout)
    # fifo for data coming from the slave
    fifoin = Fifo(256, 8, rst, datain, dataout, fullin, emptyin, pushin, notoe, pushcsin, fifocs, fillin)


    @always_comb
    def readlogic():
        if (addrbits == ADDR_FIFO):
            dataout.next = 0
        elif (addrbits == ADDR_STATUS):
            dataout.next = 0
        else:
            dataout.next = None

    @always(notwe.posedge)
    def writelogic():
        if (addrbits == ADDR_TRANSFERSIZE):
            transfercounter.next = datain

    @always_seq(clk.posedge, reset=rst)
    def transferlogic():
        if transferstate == states.TRANSFER_IDLE:
            if transfercounter != 0:
                transferstate.next = states.TRANSFER_LOWERCS
        elif transferstate == states.TRANSFER_LOWERCS:
            scs.next = 0
            transferstate.next = states.TRANSFER_TRANSFER
        elif transferstate == states.TRANSFER_TRANSFER:
            if (transferbitcounter + 1) % transferbitcounter.max == 0:
                if transfercounter - 1 == 0:
                    transferstate.next = states.TRANSFER_RAISECS
                transfercounter.next = transfercounter - 1
            transferbitcounter.next = transferbitcounter + 1
        elif transferstate == states.TRANSFER_RAISECS:
            scs.next = 1
            transferstate.next = states.TRANSFER_IDLE


    return fifoin, fifoout, readlogic, writelogic, transferlogic