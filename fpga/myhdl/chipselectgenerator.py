import math

import top

from ntondecoder import *

""" 0 == selected """

CHIPSELECT_EXTRAM = 0  # 0x0
CHIPSELECT_UART = 12
CHIPSELECT_SYSTEMREGISTERS = 13
CHIPSELECT_BOOTROM = 14  #
CHIPSELECT_BOOTRAM = 15


def ChipSelectGenerator(notas, addr, bootromdisable, chipselects,
                        extramcs,
                        systemregisterscs, bootromcs, bootramcs, uartcs):
    numchipselectbits = int(math.log(len(chipselects), 2))
    chipselectbits = addr(len(addr), len(addr) - numchipselectbits)
    decoderoutput = Signal(intbv(0)[len(chipselects):])
    decoder = NtoNDecoder(chipselectbits, decoderoutput)

    @always(notas.negedge)
    def logic():
        chipselects.next = ~decoderoutput

    @always_comb
    def bootromextramcslogic():
        extramcs.next = False if (
            bootromdisable and chipselects[CHIPSELECT_EXTRAM + 1:CHIPSELECT_EXTRAM] == 0) else True
        bootromcs.next = False if ((chipselects[CHIPSELECT_BOOTROM + 1: CHIPSELECT_BOOTROM] == 0) and bootromdisable) \
                                  or (((chipselects[CHIPSELECT_BOOTROM + 1: CHIPSELECT_BOOTROM] == 0) or
                                       (chipselects[
                                        CHIPSELECT_EXTRAM + 1: CHIPSELECT_EXTRAM] == 0)) and not bootromdisable) \
            else True

    @always_comb
    def linkage():
        bootramcs.next = chipselects[CHIPSELECT_BOOTRAM + 1:CHIPSELECT_BOOTRAM] == 1
        uartcs.next = chipselects[CHIPSELECT_UART + 1: CHIPSELECT_UART] == 1
        systemregisterscs.next = chipselects[CHIPSELECT_SYSTEMREGISTERS + 1: CHIPSELECT_SYSTEMREGISTERS] == 1

    return logic, bootromextramcslogic, decoder, linkage


def generateHeadersChipselect():
    f = open(top.SYSHEADERSPATH + '/memorymap.h', 'w')
    f.write('#include <stdint.h>\n')
    f.write("#define MEMORYMAP_EXTRAM_BASE (" + str(CHIPSELECT_EXTRAM * (1024 * 1024)) + ")\n")
    f.write("#define MEMORYMAP_UART_BASE (" + str(CHIPSELECT_UART * (1024 * 1024)) + ")\n")
    f.write("#define MEMORYMAP_SYSTEMREGISTERS_BASE (" + str(CHIPSELECT_SYSTEMREGISTERS * (1024 * 1024)) + ")\n")
    f.write("#define MEMORYMAP_BOOTROM_BASE\n")
    f.write("#define MEMORYMAP_BOOTRAM_BASE\n")
