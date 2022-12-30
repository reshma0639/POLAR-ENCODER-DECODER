# code written by hamdan for getting logic for implementing in verilog
from math import log2

N = 32
level = int(log2(N))

for i in range(0, level):
    src_cyc = 2**i
    dest_cyc = 2**(i+1)
    for j in range(0, N):
        xor = f"inter_{i+1}[{j}] = inter_{i}[{j}]^inter_{i}[{j+src_cyc}];"
        same = f"inter_{i+1}[{j}] = inter_{i}[{j}];"
        if((j//src_cyc)%2==0):
            print(xor)
        else:
            print(same)
    print("/***************************/")
