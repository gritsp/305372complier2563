dictCode = ['ADD','SUB','STO','STA','LOAD','B','BZ','BP']

#read src file from location and return data in file as data in array
def readfile(sourcefile):
    with open(sourcefile,'r') as dataSource:
        data = dataSource.read().split()
    return data

def writefile(data):           
    with open('ouputLab06.src','w') as datafile:
        for i in data:
            datafile.write(i+'\n')
    return True

def disassembler(data,dictCode):
    asm = []
    temp = []
    for i in data:
        if len(i) == 4:
            if i == '0000':
                asm.append('STOP')
            elif int(i[0]) in range(1,9):
                asm.append(dictCode[int(i[0])-1]+' %s%s' %(i[2],i[3]))
            elif i == '9001':
                asm.append('READ')
            elif i == '9002':
                asm.append('PRINT')
            else:
                temp.append([data.index(i),i])
    if temp == []:
        return asm
    else:
        return (False,temp)

def printError(disCode):
    if disCode==[]:
        return False
    if disCode[0]==False:
        print('Error!!!')
        for i in disCode[1]:
            print('Line %s: Invalid machine code %s.' %(i[0],i[1]))
        return False
    return True

def checkBinary(data):
    temp = []
    for i in data:
        if len(i)>4:
            temp.append(str(int(i,16)))
    if temp==[]:
        return data
    else:
        return temp

def dump(ac,pc,ir,mem):
    if pc>0:
        pc = '\033[91m'+str(pc).zfill(4)+'\033[0m'
        ac = '\033[91m'+str(ac).zfill(4)+'\033[0m'
        ir = '\033[91m'+str(ir).zfill(4)+'\033[0m'
    print('REGISTERS:')
    print('Accumulator (AC): %s'%str(ac).zfill(4))
    print('Program Counter (PC): %s'%str(pc).zfill(4))
    print('Instuction Registers (IR): %s'%str(ir).zfill(4))
    print('\nMEMORY:')
    print('       0    1    2    3    4    5    6    7    8    9')
    text = ''
    for i in range(0,100):
        if i == 0:
            text = ' 0  %s '%mem[i]
        elif i%10==0:
            text += '%s  %s '%(i,mem[i])
        elif i%10==9:
            text += '%s\n'%mem[i]
        else:
            text += '%s '%mem[i]
    print(text)

def dataMemory(data):
    mem = [i for i in data]
    return mem

def emulator(ac,pc,ir,dm,mem):
    pc -=1
    ir = mem[pc]
    if dm[pc] == '9001':
        ac = input('input>')
    if dm[pc] == '9002':
        print(ac)
    if dm[pc][0] == '3':
        index = dm[pc][1]+dm[pc][2]+dm[pc][3]
        if len(dm)<=int(index):
            mem[int(index)] = '\033[92m'+str(ac).zfill(4)+'\033[0m'
    if dm[pc][0] == '1':
        index = dm[pc][1]+dm[pc][2]+dm[pc][3]
        ac = int(ac)+int(mem[int(index)].strip('\033[92m').strip('\033[0m'))

    return [ac,ir,mem]
def main():
    sourcefile = '.\sourcefile.lmc'
    fileData = readfile(sourcefile)
    data = checkBinary(fileData)
    disCode = disassembler(data,dictCode)
    # printError(disCode)    
    pc = 0
    ir = 0
    ac = 0
    mem = [str('0').zfill(4) for i in range(0,100)]
    print('*** Welcome to anExtended Little ManComputerEmulator! ***')
    if printError(disCode)==False:
        pass
    else:
        writefile(disCode)
        while(True):
            cm = input('>')
            if cm == 'quit' or cm=='exit':
                break
            elif cm == 'dump':
                dump(ac,pc,ir,mem)
            elif cm == 'load':
                dataMem = dataMemory(data)
                for i in range(0,len(dataMem)):
                    mem[i] = '\033[91m'+str(dataMem[i]).zfill(4)+'\033[0m' 
            elif cm == 'step':
                pc+=1
                temp = emulator(ac,pc,ir,dataMem,mem)
                ac = temp[0]
                ir = temp[1]
                mem = temp[2]
                if(pc>=len(dataMem)):
                    print('Done')
                    ac = 0
                    pc = 0
                    ir = 0
                    mem = [str('0').zfill(4) for i in range(0,100)]
                    dataMem =[]
            elif cm == 'reset':
                ac = 0
                pc = 0
                ir = 0
                mem = [str('0').zfill(4) for i in range(0,100)]
                dataMem = []
                print('Memory is reset already')
            elif cm == 'run':
                for i in dataMem:
                    pc+=1
                    temp = emulator(ac,pc,ir,dataMem,mem)
                    ac = temp[0]
                    ir = temp[1]
                    mem = temp[2]
                dump(ac,pc,ir,mem)
                if(pc>=len(dataMem)):
                    print('Done')
                    ac = 0
                    pc = 0
                    ir = 0
                    mem = [str('0').zfill(4) for i in range(0,100)]
                    dataMem =[]
            else:
                print('Command not found!!!')
 

if __name__ == "__main__":
    main()