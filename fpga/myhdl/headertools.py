def addRegisterDefine(headerfile, registername, registersize, registerbase, registeroffset):
    headerfile.write(
        '#define ' + registername + ' *(volatile uint' + str(registersize) + '_t*)(' + registerbase + ' + ' + str(
            registeroffset) + ')\n')


def addBitMask(headerfile, maskname, bit):
    headerfile.write('#define ' + maskname + ' (1 << ' + str(bit) + ')\n')
