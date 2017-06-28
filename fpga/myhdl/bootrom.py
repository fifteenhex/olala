import array
import math

from myhdl import *

import systemconstants


BOOTROMSIZE = 4084
ADDRESSBITS = int(math.log(BOOTROMSIZE, 2)) - 1


def BootRom(addr, dataout, notoe, notcs):
    bootromfile = open('../../bootrom/prog.bin', 'rb')
    bootromdatatmp = array.array('H')
    bootromdatatmp.fromfile(bootromfile, BOOTROMSIZE / systemconstants.BUSBYTES)
    bootromdatatmp.byteswap()

    bootromdata = tuple(bootromdatatmp)

    @always_comb
    def logic():
        if (notcs == 0 and notoe == 0):
            dataout.next = bootromdata[addr[ADDRESSBITS:]]
        else:
            dataout.next = None

    return logic