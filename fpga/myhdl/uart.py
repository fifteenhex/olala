from fifo import *
from eightbitshim import *
import top
from headertools import *

ADDR_FIFO = 0
ADDR_CLOCKSCALER1 = 1
ADDR_CLOCKSCALER2 = 2
ADDR_STATUS = 3
ADDR_CONFIG = 4
ADDR_FILL = 5


def Uart(clk, reset, rx, tx,
         notoe,
         notwe,
         notcs,
         addr,
         datain,
         dataout,
         baudout,
         readstrobe,
         interrupt):
    FIFODEPTH = 16

    ADDR_BITS = 3

    clockscaler1 = Signal(modbv(0)[8:])
    clockscaler2 = Signal(modbv(0)[8:])
    clockscalercounter1 = Signal(modbv(0)[8:])
    clockscalercounter2 = Signal(modbv(0)[8:])

    rxfull = Signal(bool(0))
    rxempty = Signal(bool(1))
    rxpush = Signal(bool(1))
    rxpushcs = Signal(bool(1))

    txfull = Signal(bool(0))
    txempty = Signal(bool(1))
    txpop = Signal(bool(1))
    txpopcs = Signal(bool(1))

    rxdataout = Signal(intbv(0)[8:])
    rxdatainbits = [Signal(bool(0)) for i in range(8)]
    rxdatain = ConcatSignal(*list(reversed(rxdatainbits)))

    txdataout = Signal(intbv(0)[8:])
    txdatain = Signal(intbv(0)[8:])

    fifocs = Signal(bool(1))

    txfill = Signal(modbv(0, 0, FIFODEPTH))
    rxfill = Signal(modbv(0, 0, FIFODEPTH))

    rxfifo = Fifo(FIFODEPTH, 8, reset, rxdatain, rxdataout, rxfull, rxempty, rxpush, readstrobe, rxpushcs, fifocs,
                  rxfill)
    txfifo = Fifo(FIFODEPTH, 8, reset, txdatain, txdataout, txfull, txempty, notwe, txpop, fifocs, txpopcs, txfill)

    status = ConcatSignal(rxfull, rxempty, txfull, txempty)
    fill = ConcatSignal(rxfill, txfill)

    config = Signal(intbv(0)[8:])

    registeraddrbits = addr(ADDR_BITS, 0)

    upperbytein = Signal(intbv(0)[8:])
    upperbyteout = Signal(intbv(0)[8:])
    intdataout = Signal(intbv(0)[16:])

    shim = EightBitShim(datain, intdataout, upperbytein, upperbyteout)

    baudclock = Signal(bool(1))

    @always_comb
    def registeroutmux():
        if (registeraddrbits == ADDR_FIFO):
            upperbyteout.next = rxdataout
        elif (registeraddrbits == ADDR_CLOCKSCALER1):
            upperbyteout.next = clockscaler1
        elif (registeraddrbits == ADDR_CLOCKSCALER2):
            upperbyteout.next = clockscaler2
        elif (registeraddrbits == ADDR_STATUS):
            upperbyteout.next = status
        elif (registeraddrbits == ADDR_CONFIG):
            upperbyteout.next = config
        elif (registeraddrbits == ADDR_FILL):
            upperbyteout.next = fill
        else:
            upperbyteout.next = 0

    @always_comb
    def readlogic():
        if (notcs == 0 and notoe == 0):
            dataout.next = intdataout
        else:
            dataout.next = None

    @always_comb
    def txdatainlogic():
        txdatain.next = upperbytein

    @always_seq(notwe.posedge, reset=reset)
    def writelogic():
        if (not notcs):
            if (registeraddrbits == ADDR_CLOCKSCALER1):
                clockscaler1.next = upperbytein
            elif (registeraddrbits == ADDR_CLOCKSCALER2):
                clockscaler2.next = upperbytein
            elif (registeraddrbits == ADDR_CONFIG):
                config.next = upperbytein

    @always_comb
    def fifopushpop():
        fifocs.next = False if (notcs == 0) and (registeraddrbits == ADDR_FIFO) else True

    @always_seq(clk.posedge, reset=reset)
    def baudgenerator():
        if clockscalercounter1 == clockscaler1:
            clockscalercounter1.next = 0
            if clockscalercounter2 == clockscaler2:
                clockscalercounter2.next = 0
                baudclock.next = not baudclock
            else:
                clockscalercounter2.next = clockscalercounter2 + 1
        else:
            clockscalercounter1.next = clockscalercounter1 + 1

    @always_comb
    def baudoutput():
        baudout.next = baudclock

    rxstates = enum('RXSTATE_IDLE', 'RXSTATE_START', 'RXSTATE_DATA', 'RXSTATE_STOP')
    rxstate = Signal(rxstates.RXSTATE_IDLE)
    rxcounter = Signal(modbv(0, min=0, max=16))
    rxbitcounter = Signal(modbv(0, min=0, max=8))

    @always_seq(baudclock.posedge, reset=reset)
    def receiver():
        if rxstate == rxstates.RXSTATE_IDLE:
            if (not rxfull):
                if (rx == 0):
                    rxpushcs.next = 0
                    rxstate.next = rxstates.RXSTATE_START
        elif rxstate == rxstates.RXSTATE_START:
            if rxcounter == 0:
                rxpush.next = 0
            if (rxcounter + 1) % rxcounter.max == 0:
                rxstate.next = rxstates.RXSTATE_DATA
            rxcounter.next = rxcounter + 1
        elif rxstate == rxstates.RXSTATE_DATA:
            if (rxcounter + 1) % rxcounter.max == 0:
                if ((rxbitcounter + 1) % rxbitcounter.max == 0):
                    rxstate.next = rxstates.RXSTATE_STOP
                rxbitcounter.next = rxbitcounter + 1
            elif (rxcounter == rxcounter.max // 2):
                rxdatainbits[rxbitcounter].next = rx

            rxcounter.next = rxcounter + 1
        elif rxstate == rxstates.RXSTATE_STOP:
            if (rxcounter == 0):
                rxpush.next = 1
            if (rxcounter + 1) % rxcounter.max == 0:
                rxpushcs.next = 1
                rxstate.next = rxstates.RXSTATE_IDLE
            rxcounter.next = rxcounter + 1

    txstates = enum('TXSTATE_IDLE', 'TXSTATE_START', 'TXSTATE_DATA', 'TXSTATE_STOP')
    txstate = Signal(txstates.TXSTATE_IDLE)
    txcounter = Signal(modbv(0, min=0, max=16))
    txbitcounter = Signal(modbv(0, min=0, max=8))

    @always_seq(baudclock.posedge, reset=reset)
    def transmitter():
        if (txstate == txstates.TXSTATE_IDLE):
            if (not txempty):
                txpopcs.next = 0
                txstate.next = txstates.TXSTATE_START
        elif (txstate == txstates.TXSTATE_START):
            if (txcounter == 0):
                tx.next = 0
                txpop.next = 0
            if (txcounter + 1) % txcounter.max == 0:
                txstate.next = txstates.TXSTATE_DATA
            txcounter.next = txcounter + 1
        elif (txstate == txstates.TXSTATE_DATA):
            txbit = intbv(0)[len(txbitcounter) + 1:]
            txbit[:] = txbitcounter
            if (txcounter == 0):
                if txdataout[txbit + 1: txbit] == 1:
                    tx.next = True
                else:
                    tx.next = False

            if (txcounter + 1) % txcounter.max == 0:
                if (txbitcounter + 1) % txbitcounter.max == 0:
                    txstate.next = txstates.TXSTATE_STOP
                txbitcounter.next = txbitcounter + 1
            txcounter.next = txcounter + 1
        elif (txstate == txstates.TXSTATE_STOP):
            # generate 2 stop bits
            if (txcounter == 0 and txbitcounter == 0):
                tx.next = 1
                txpop.next = 1
            elif (txcounter + 1) % txcounter.max == 0:
                if (txbitcounter == 1):
                    txbitcounter.next = 0
                    txstate.next = txstates.TXSTATE_IDLE
                    txpopcs.next = 1
                else:
                    txbitcounter.next = txbitcounter + 1
            txcounter.next = txcounter + 1

    return rxfifo, \
           txfifo, \
           shim, \
           registeroutmux, \
           readlogic, \
           writelogic, \
           baudgenerator, \
           baudoutput, \
           receiver, \
           transmitter, \
           fifopushpop, \
           txdatainlogic


def generateHeadersUart():
    f = open(top.SYSHEADERSPATH + '/uart.h', 'w')
    f.write('#include "memorymap.h"\n')
    addRegisterDefine(f, "uart_fifo", 8, "MEMORYMAP_UART_BASE", ADDR_FIFO * 2)
    addRegisterDefine(f, "uart_clockscaler1", 8, "MEMORYMAP_UART_BASE", ADDR_CLOCKSCALER1 * 2)
    addRegisterDefine(f, "uart_clockscaler2", 8, "MEMORYMAP_UART_BASE", ADDR_CLOCKSCALER2 * 2)
    addRegisterDefine(f, "uart_status", 8, "MEMORYMAP_UART_BASE", ADDR_STATUS * 2)
    addRegisterDefine(f, "uart_config", 8, "MEMORYMAP_UART_BASE", ADDR_CONFIG * 2)
    addRegisterDefine(f, "uart_fill", 8, "MEMORYMAP_UART_BASE", ADDR_FILL * 2)
    f.write('#define UART_TXEMPTY    1\n')
    f.write('#define UART_TXFULL     (1 << 1)\n')
    f.write('#define UART_RXEMPTY    (1 << 2)\n')
    f.write('#define UART_RXFULL     (1 << 3)\n')
