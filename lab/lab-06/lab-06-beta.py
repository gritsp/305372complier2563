dictCode = ['ADD','SUB','STO','STA','LOAD','B','BZ','BP']

#read src file from location and return data in file as data in array
def readfile(sourcefile):
    with open(sourcefile,'r') as dataSource:
        data = dataSource.read().split()
    return data

def writefile(data):           
    with open('ouputLab05.src','w') as datafile:
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
    if pc == 0:
        ac = '0000'.zfill(4)
        pc = 0
        ir = '0000'.zfill(4)
    else:
        ir = '\033[91m'+str(mem[pc-1]).zfill(4)+'\033[0m'
        ac = '\033[91m'+str(ac).zfill(4)+'\033[0m'
        pc = '\033[91m'+str(pc).zfill(4)+'\033[0m'
        
        
    
    print('REGISTER:\nAccumulator (AC): %s\nProgram Cunter (PC): %s\nInstruction Register (IR): %s\n\nMEMORY:' %(ac,str(pc).zfill(4),ir))
    print('       0    1    2    3    4    5    6    7    8    9')
    text = ''
    for i in range(0,100):
        if i ==0:
            text +=str(' 0  '+str(mem[i]).zfill(4)+' ')
        elif i%10==9:
            text +='%s \n'%mem[i].zfill(4)
        elif i%10==0:
            text +=str('%s  %s '%(i,str(mem[i]).zfill(4)))
        else:
            # print('%s0  '%i +text)
            text +=str(mem[i]).zfill(4) + ' '
    
    # print(text)
    return text     

def dataMemory(ac):
    temp = []
    temp.append(ac)
    return temp

def instuctionMemory(data):
    mem = []
    for i in data:
        mem.append(i)    
    return mem

def memory(im,dm):
    mem = []
    for i in im:
        mem.append('\033[91m'+str(i).zfill(4)+'\033[0m')
    for i in dm:
        mem.append('\033[92m'+str(i).zfill(4)+'\033[0m')
    for i in range(len(mem),100):
        mem.append('0000')
    return mem

def emulator(pc,im,dm,ac):
    if im[pc]=='9001':
        ac = input('input>')
    if im[pc][0]=='3':
        i = str(im[pc][1])+str(im[pc][2])+str(im[pc][3])
def main():
    sourcefile = '.\sourcefile.lmc'
    fileData = readfile(sourcefile)
    data = checkBinary(fileData)
    disCode = disassembler(data,dictCode)
    if printError(disCode)==False:
        pass
    else:
        writefile(disCode)
     
    ac = '1234'
    pc = 0
    ir = ''
    mem = []   
    
    print('*** Welcome to anExtended Little ManComputerEmulator! ***')
           
    while(True):
        cm = input('>')
        if cm=='quit'or cm=='exit':            
            break
        if cm == 'dump':
            disp = dump(ac,pc,ir,mem)            
            print(disp)
        if cm == 'load':
            im = instuctionMemory(data)
            dm = dataMemory(ac)
            mem = memory(im,'')
        if cm=='step':
            mem = memory(im,dm)
            pc+=1
        if cm == 'reset':
            data = ''
            ac = ''
            im = instuctionMemory(data)
            dm = dataMemory(ac)
            mem = memory(im,'')
            pc = 0
            
        # else:
        #     print("Command error! "+cm+" not in command")

if __name__ == "__main__":
    main()