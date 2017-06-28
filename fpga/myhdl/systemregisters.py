import math

from myhdl import *

from headertools import *
import top

ADDR_LEDS = 0
ADDR_DIVIDERBIT = 1
ADDR_SYSCONFIG = 2

ADDR_SYSTICKHIGH = 4
ADDR_SYSTICKLOW = 5
ADDR_SYSTICKINTERVAL = 6

SYSCONFIG_BOOTROMDISABLE = 0
SYSCONFIG_SYSTICKINT = 1


def SystemRegisters(clk,  # main clock
                    rst, addr, datain, dataout, registerscs, notoe, notuwe, notlwe,
                    # outputs
                    ledsregister,
                    dividerbit,
                    bootromdisable,
                    systickinterrupt):
    # how many address bits do we need to decode all of the registers?
    ADDR_BITS = int(math.ceil(math.log(ADDR_SYSTICKLOW + 1, 2)))
    # get just the bits we need
    registeraddrbits = addr(ADDR_BITS, 0)

    ledslower = Signal(intbv(0)[8:])
    expandedledregister = ConcatSignal(ledsregister, ledslower)

    # sysconfig register

    systickintenabled = Signal(bool(0))

    sysconfigpadding = Signal(modbv(0)[14:])
    sysconfig = ConcatSignal(sysconfigpadding, systickintenabled, bootromdisable)

    # systick register; provides a register that increments at an interval of 1ms
    systickprescaler = Signal(modbv(0)[16:])
    systickcounter = Signal(modbv(0)[32:])
    systickinterval = Signal(modbv(0)[16:])

    @always_seq(clk.posedge, reset=rst)
    def systick():
        if (systickprescaler + 1 == 50000):
            systickprescaler.next = 0
            systickcounter.next = systickcounter + 1

            if (registerscs == False and notuwe == False and registeraddrbits == ADDR_SYSTICKINTERVAL):
                systickinterval.next = datain
            else:
                # if the systickint is enabled generate an interrupt whenever systickinterval gets to 0
                # if systickinterval isn't 0 decrement it
                # this gives us an interrupt after N systicks that can be reset by writing the interval again
                if systickintenabled == True:
                    if (systickinterval == 0):
                        systickinterrupt.next = True
                    else:
                        systickinterval.next = systickinterval - 1
                        systickinterrupt.next = False
                else:
                    systickinterrupt.next = False

        else:
            systickprescaler.next = systickprescaler + 1

    @always(notuwe.posedge)
    def writeupperbytelogic():
        if (not registerscs):  # and data != None):
            if (registeraddrbits == ADDR_LEDS):
                ledsregister.next = datain[16:8]
            elif (registeraddrbits == ADDR_DIVIDERBIT):
                dividerbit.next = datain[16:8]
            elif (registeraddrbits == ADDR_SYSCONFIG):
                if datain[SYSCONFIG_BOOTROMDISABLE + 1: SYSCONFIG_BOOTROMDISABLE] == 1:
                    bootromdisable.next = True
                else:
                    bootromdisable.next = False

                if (datain[SYSCONFIG_SYSTICKINT + 1: SYSCONFIG_SYSTICKINT] == 1):
                    systickintenabled.next = True
                else:
                    systickintenabled.next = False

    @always_comb
    def readlogic():
        if not registerscs and not notoe:
            if registeraddrbits == ADDR_LEDS:
                dataout.next = expandedledregister
            elif registeraddrbits == ADDR_DIVIDERBIT:
                dataout.next = dividerbit
            elif registeraddrbits == ADDR_SYSCONFIG:
                dataout.next = sysconfig
            elif registeraddrbits == ADDR_SYSTICKHIGH:
                dataout.next = systickcounter[32:16]
            elif registeraddrbits == ADDR_SYSTICKLOW:
                dataout.next = systickcounter[16:]
            elif registeraddrbits == ADDR_SYSTICKINTERVAL:
                dataout.next = systickinterval
            else:
                dataout.next = 0
        else:
            dataout.next = None

    return systick, writeupperbytelogic, readlogic


def generateHeadersSystemRegisters():
    f = open(top.SYSHEADERSPATH + '/systemregisters.h', 'w')
    f.write('#include "memorymap.h"\n')
    addRegisterDefine(f, "systemregisters_leds", 8, "MEMORYMAP_SYSTEMREGISTERS_BASE", ADDR_LEDS * 2)
    addRegisterDefine(f, "systemregisters_dividerbit", 8, "MEMORYMAP_SYSTEMREGISTERS_BASE", ADDR_DIVIDERBIT * 2)
    addRegisterDefine(f, "systemregisters_sysconfig", 16, "MEMORYMAP_SYSTEMREGISTERS_BASE", ADDR_SYSCONFIG * 2)
    addRegisterDefine(f, "systemregisters_systick", 32, "MEMORYMAP_SYSTEMREGISTERS_BASE", ADDR_SYSTICKHIGH * 2)
    addRegisterDefine(f, "systemregisters_systickinterval", 16, "MEMORYMAP_SYSTEMREGISTERS_BASE",
                      ADDR_SYSTICKINTERVAL * 2)

    addBitMask(f, "SYSTEMREGISTERS_SYSCONFIG_DISABLEBOOTROM", SYSCONFIG_BOOTROMDISABLE)
