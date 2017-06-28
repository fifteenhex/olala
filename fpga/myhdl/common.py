from myhdl import *

import systemconstants

cpuclock = Signal(bool(1))
notramcs = Signal(bool(1))
notoe = Signal(bool(1))
notlwe = Signal(bool(1))
notuwe = Signal(bool(1))

# m68k stuff
ipl = Signal(intbv(~0)[3:])
dtack = Signal(bool(1))
notbr = Signal(bool(1))
notbg = Signal(bool(1))
data = TristateSignal(intbv(0)[systemconstants.DATABUSBITS:])
addr = Signal(modbv(0)[systemconstants.ADDRESSBUSBITS:])
rnotw = Signal(bool(1))
notuds = Signal(bool(1))
notlds = Signal(bool(1))
notas = Signal(bool(1))
notcpureset = TristateSignal(bool(0))
notcpuhalt = TristateSignal(bool(0))
notberr = Signal(bool(1))
notavec = Signal(bool(0))

# board stuff
clk = Signal(bool(1))
sysreset = ResetSignal(0, active=1, async=True)
button = Signal(bool(False))
leds = Signal(intbv(1)[8:])
rx = Signal(bool(1))
tx = Signal(bool(1))

flashmosi = Signal(bool(1))
flashmiso = Signal(bool(1))
flashcs = Signal(bool(1))
flashclk = Signal(bool(1))

baudout = Signal(bool(1))

