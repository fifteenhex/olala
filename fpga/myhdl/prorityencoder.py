from ntonencoder import *


def PriorityEncoder(input, output):
    outputstmp = []
    for i in range(0, input.max):
        tmp = i
        shifts = 0
        while tmp != 0:
            tmp = tmp >> 1
            shifts += 1

        if (shifts > 0):
            outputstmp.append(1 << (shifts - 1))
        else:
            outputstmp.append(0)

    outputs = tuple(outputstmp)

    maskedinput = Signal(intbv(0)[len(input):])
    ntonencoder = NtoNEncoder(maskedinput, output)

    @always_comb
    def logic():
        maskedinput.next = outputs[input]

    return logic, ntonencoder
