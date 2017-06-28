import os
import shutil

from clockgenerator import *
from resetgenerator import *
from chipselectgenerator import *
from interruptcontroller import *
from busglue import *
from bootrom import *
from bootram import *
from uart import *
from systemregisters import *


def Top(clk,
        cpuclock,
        sysreset,
        button,
        notcpureset,
        notcpuhalt,
        notas,
        rnotw,
        notuds,
        notlds,
        dtack,
        notbr,
        notbg,
        addr,
        data,
        notextramcs,
        ipl,
        notoe,
        notuwe,
        notlwe,
        notberr,
        notavec,
        leds,
        rx,
        tx,
        baudout):
    internalreset = ResetSignal(0, active=0, async=True)

    intcpuclock = Signal(bool(0))
    intnotoe = Signal(bool(0))
    intnotlwe = Signal(bool(0))
    intnotuwe = Signal(bool(0))
    readstrobe = Signal(bool(0))

    chipselects = Signal(intbv(~0)[16:])
    bootromdisable = Signal(bool(0))
    sysregcs = Signal(bool(1))
    bootromcs = Signal(bool(1))
    bootramcs = Signal(bool(1))
    uartcs = Signal(bool(1))

    nmi = Signal(bool(0))
    systickint = Signal(bool(0))
    uartint = Signal(bool(0))

    ledsregister = Signal(intbv(0)[8:])

    @always_comb
    def ledlogic():
        leds.next = addr[8:] if button == 1 else ledsregister

        dtack.next = 0
        notbr.next = 1

        cpuclock.next = intcpuclock
        notoe.next = intnotoe
        notlwe.next = intnotlwe
        notuwe.next = intnotuwe
        notberr.next = True

    dividerbit = Signal(intbv(1)[8:])
    clockgenerator = ClockGenerator(clk, intcpuclock, sysreset, dividerbit)

    resetgenerator = ResetGenerator(intcpuclock, sysreset, notcpureset, notcpuhalt, internalreset)

    notbg.read = True

    chipselectgenerator = ChipSelectGenerator(notas, addr, bootromdisable, chipselects, notextramcs, sysregcs,
                                              bootromcs, bootramcs,
                                              uartcs)
    interruptcontroller = InterruptController(ipl, nmi, systickint, uartint)
    busglue = BusGlue(notas, rnotw, notuds, notlds, dtack, notbr, notbg, intnotoe, intnotuwe, intnotlwe, readstrobe)

    systemregisters = SystemRegisters(clk, internalreset, addr, data, data.driver(), sysregcs, intnotoe, intnotuwe,
                                      intnotlwe, ledsregister, dividerbit, bootromdisable, systickint)

    bootrom = BootRom(addr, data.driver(), intnotoe, bootromcs)
    bootram = BootRAM(addr, data.driver(), data, bootramcs, intnotoe, intnotuwe, intnotlwe)

    uart = Uart(intcpuclock, internalreset, rx, tx, intnotoe, intnotuwe, uartcs, addr, data, data.driver(), baudout,
                readstrobe, uartint)

    return clockgenerator, resetgenerator, systemregisters, ledlogic, chipselectgenerator, interruptcontroller, busglue, bootrom, bootram, uart


SYSHEADERSPATH = "./sysheaders"


def generateHeaders():
    if os.path.isdir(SYSHEADERSPATH):
        shutil.rmtree(SYSHEADERSPATH)
    os.mkdir(SYSHEADERSPATH)
    generateHeadersChipselect()
    generateHeadersSystemRegisters()
    generateHeadersUart()
