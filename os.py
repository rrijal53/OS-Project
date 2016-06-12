import sys
def read(ir,M):
    ir[3].__add__("0")
    start = 0
    x = int(ir[2:4])
    buf = f.readline()
    for i in range(x, x + 10):
         	M[i] = buf[start:start + 4]
         	start += 4
         	x+=1
def write(ir,M,r,c,ic):
    ir[3].__add__("0")
    x = int(ir[2:4])
    for i in range(x, x + 10):
        fo.write(M[i])
    fo.write("\n")
    executeUserProgram(ir,M,r,c,ic)
def terminate(ir,M,r,c):
    fo.write("\n\n")
    M = ["" for x in range(100)]
    si=3
    r = ""
    c=""
    ir = "    "
    loadData(ir,M,r,c)
def executeUserProgram(ir,M,r,c,ic):
    tempMem = 0
    while 1:
        try:
            ir = M[ic]
        except:
            sys.exit("Execution finished ")
        ic += 1
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
                c= "F"
        elif ir[0:2] == "BT":
            if c == "T":
                ic = int(ir[2:4])
        elif ir[0:2] == "GD":
            si=1
            master(si,ir,M,r,c,ic)
        elif ir[0:2] == "PD":
            si=2
            master(si,ir,M,r,c,ic)
        elif ir[0:2] == "H ":
            si=3
            master(si,ir,M,r,c,ic)

def loadData(ir,M,r,c):
    m = 0
    a = f.readline()
    while a:
        a = f.readline()
        if a=="\n\r" or a=="":
            break
        buffer = a
        if buffer[0:4] == "$AMJ":
            continue
        elif buffer[0:4] == "$DTA":
            ic = 0
            executeUserProgram(ir,M,r,c,ic)
        elif buffer[0:4] == "$END":
            si = 3
            ic = 0
            M = ["" for x in range(100)]
            r = "    "
            c=" "
            ir = "    "
            continue
        else:
            start = 0
            for i in range(m, m + 10):
                if(m>=100):
                    print("Memory Exceeds")
                    break
                if buffer[start:start + 4] != "" or buffer[start:start + 4] != "\r\n":
                    M[i] = buffer[start:start + 4]
                    start += 4
            m += 10
    

def master(si,ir,M,r,c,ic):
    if(si==1):
        read(ir,M)
    elif(si==2):
        write(ir,M,r,c,ic)
    elif si==3:
        terminate(ir,M,r,c)


global r, c, ic,ir, si, m, a
line = ""
r = "    "
c=" "
ir = "    "
fo = open("output.txt", "w+")
f = open("input.txt", "r")
si = 3
ic = 0
M = ["" for x in range(100)]
master(si,ir,M,r,c,ic)
