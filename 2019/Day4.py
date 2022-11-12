
count = 0
for i in range(146810, 612564):
    if (int(str(i)[0]) <= int(str(i)[1]) <= int(str(i)[2]) <= int(str(i)[3]) <= int(str(i)[4]) <= int(str(i)[5])) and \
            ((int(str(i)[0]) == int(str(i)[1]) < int(str(i)[2])) or
             (int(str(i)[0]) < int(str(i)[1]) == int(str(i)[2]) < int(str(i)[3])) or
             (int(str(i)[1]) < int(str(i)[2]) == int(str(i)[3]) < int(str(i)[4])) or
             (int(str(i)[2]) < int(str(i)[3]) == int(str(i)[4]) < int(str(i)[5])) or
             (int(str(i)[3]) < int(str(i)[4]) == int(str(i)[5]))):
        count += 1

print(count)