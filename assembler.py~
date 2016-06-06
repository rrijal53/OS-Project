f = open("input.txt", "r")

global M
global ic
global r
global c, ir, m


def loadData():
    global r, c, ic, si
    M = ["" for x in range(100)]
    m = 0
    si=3
    a = f.readline()
    while a:
        # print(a)
        a = f.readline()
        buffer = a
        if buffer[0:4] == "$AMJ":
            # print("Milyo" + buffer[0:4])
            continue
        elif buffer[0:4] == "$DTA":
            ic = 0
            tempMem = 0
            while ic<100:
                ir = M[ic]
                ic += 1
                # print(ir[2:4])
                if ir[0:2] == "LR":
                    tempMem = int(ir[2:4])
                    r = M[tempMem]
                elif ir[0:2] == "SR":
                    tempMem = int(ir[2:4])
                    M[tempMem] = r
                elif ir[0:2] == "CR":
                    tempMem = int(ir[2:4])
                    if r == M[tempMem]:
                        c = "T"
                    else:
                        c = "F"
                elif ir[0:2] == "BT":
                    if c == "T":
                        ic = int(ir[2:4])
                elif ir[0:2] == "GD":
                    si=1
                    ir[3].__add__("0")
                    start = 0
                    x = int(ir[2:4])
                    # print("x=")
                    # print(x)
                    buf = f.readline()
                    for i in range(x, x + 9):
                        if buf[start:start + 4] != "\r\n":
                            print(i)
                            M[i] = buf[start:start + 4]
                            start += 4
                            x+=1
                            # print(M)
                elif ir[0:2] == "PD":
                    si=2
                    print(ir)
                    ir[3].__add__("0")
                    x = int(ir[2:4])
                    for i in range(x, x + 10):
                        print(M[i])
                        fo.write(M[i])
                elif ir[0:2] == "H":
                    si=3
                    break
        elif buffer[0:4] == "$END":
            break
        else:
            start = 0
            # print("else part")
            # print("inside while")
            for i in range(m, m + 10):
                if buffer[start:start + 4] != "" or buffer[start:start + 4] != "\r\n":
                    M[i] = buffer[start:start + 4]
                    start += 4
                    # print(M)
            m += 10


fo = open("output.txt", "w+")
loadData()
