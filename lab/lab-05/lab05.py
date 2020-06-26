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


def main():
    sourcefile = input()
    fileData = readfile(sourcefile)
    data = checkBinary(fileData)
    disCode = disassembler(data,dictCode)
    if printError(disCode)==False:
        pass
    else:
        writefile(disCode)
        print('Done.')

if __name__ == "__main__":
    main()