
'''
this file explains the inner working of xor algorithm whenever we use xor in genral standards we use 8 bit binary digit as mandatory '''


def eight_bit_converter(bits):
    if len(bits)==8:
        pass
    else:
        bits="".join(["0" for i in range(8-(len(bits)))])+bits
    return bits
eight_bit_converter(bin(13)[2:])
def xor(bit1,bit2):
    bit1=eight_bit_converter(bit1)
    bit2=eight_bit_converter(bit2)
    OR=lambda x,y: 1 if 1 in [x,y] else 0
    AND=lambda x,y: 0 if 0 in [x,y] else 1
    complement= lambda bit: 1 if bit==0 else 0
    l1=[OR(AND(int(bit1[i]),complement(int(bit2[i]))),AND(complement(int(bit1[i])),int(bit2[i]))) for i in range(8)]
    return sum([l1[i]**i for i in range(8)])

x=bin(65)[2:]
y=bin(66)[2:]
xor(x,y)