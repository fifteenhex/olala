from myhdl import *


def NtoNEncoder(input, output):
    outputstmp = []
    for i in range(0, input.max):
        ones = 0
        for j in range(0, len(input)):
            if i & (1 << j):
                ones = ones + 1
        if ones == 1:
            zeros = 0
            for j in range(0, len(input)):
                if not (i & (1 << j)):
                    zeros += 1
                else:
                    break
            if(zeros + 1 < output.max):
                outputstmp.append(zeros + 1)
            else:
                outputstmp.append(0)
        else:
            outputstmp.append(0)

    outputs = tuple(outputstmp)

    @always_comb
    def logic():
        output.next = outputs[input]

    return logic