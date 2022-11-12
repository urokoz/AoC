import numpy as np
import pandas as pd


ic = np.array((pd.read_csv("day5.csv", header=None)))[0]


def value(pos, mode):
    if mode == 1:
        val = ic[pos]
    else:
        val = ic[ic[pos]]
    return val


def intcode():
    i = 0
    while i < len(ic):
        instruct = ic[i]

        if instruct == 99:
            break

        instruct = str(instruct)
        try:
            opcode = int(instruct[-2:])
        except:
            opcode = int(instruct[-1])

        try:
            pm1 = int(instruct[-3])
        except IndexError:
            pm1 = 0

        try:
            pm2 = int(instruct[-4])
        except IndexError:
            pm2 = 0

        try:
            pm3 = int(instruct[-5])
        except IndexError:
            pm3 = 0

        if opcode == 1:

            par3 = ic[i + 3]
            int_add = value(i + 1, pm1) + value(i + 2, pm2)
            ic[par3] = int_add
            
            i = i + 4

        elif opcode == 2:
            par3 = ic[i + 3]
            int_mul = value(i + 1, pm1) * value(i + 2, pm2)
            ic[par3] = int_mul
            i = i + 4

        elif opcode == 3:
            while True:
                try:
                    num = int(input("Input integer: "))
                    break
                except ValueError:
                    print("Invalid input - must be number in the menu!")
                    pass
            ic[ic[i + 1]] = num
            i = i + 2

        elif opcode == 4:
            out = value(i + 1, pm1)
            print("")
            print("ErrorValue: {:d}".format(out))
            print("Instruction: {:d}".format(ic[i-4]))
            i = i + 2

        elif opcode == 5:
            if value(i + 1, pm1) != 0:
                i = value(i + 2, pm2)
            else:
                i = i + 3

        elif opcode == 6:
            if value(i + 1, pm1) == 0:
                i = value(i + 2, pm2)
            else:
                i = i + 3

        elif opcode == 7:
            if value(i + 1, pm1) < value(i + 2, pm2):
                ic[ic[i + 3]] = 1
            else:
                ic[ic[i + 3]] = 0
            i = i + 4

        elif opcode == 8:
            if value(i + 1, pm1) == value(i + 2, pm2):
                ic[ic[i + 3]] = 1
            else:
                ic[ic[i + 3]] = 0
            i = i + 4

    return out


print(intcode())