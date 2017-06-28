from myhdl import *


def NtoNDecoder(input, output):
    outputstmp = []
    for i in range(0, input.max):
        outputstmp.append(1 << i)

    outputs = tuple(outputstmp)

    @always_comb
    def logic():
        output.next = outputs[input]

    return logic
