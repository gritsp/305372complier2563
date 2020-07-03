dictCode = ['ADD','SUB','STO','STA','LOAD','B','BZ','BP']

def readfile(source):
    with open(source,'r') as dataSource:
        data = [line.strip().split() for line in dataSource]
    return data

def writefile(data):           
    with open('ouputLab07.src','w') as datafile:
        for i in data:
            if i == data[len(data)-1]:
                datafile.write(str(i))
            else:
                datafile.write(str(i)+'\n')
        print('Done!!!')
    return True

def assembler(data):
    temp = []
    label = []
    for i in data:
        idx = data.index(i)
        for j in i:
            if j[0] == ';':
                data[idx] = data[idx][:i.index(j)]
    for i in data:
        if i==[]:
            data.remove(i)

    for i in data:        
        if i[0] not in dictCode and i[0] not in ['STOP','READ','PRINT','DAT']:
            idx = data.index(i)
            label.append([i[0],idx+1])
            data[idx].pop(0)

    for i in data:        
        if i[0] == 'STOP':
            temp.append('0000'.zfill(4))
        elif i[0] == 'READ':
            temp.append('9001')
        elif i[0] == 'PRINT':
            temp.append('9002')
        elif i[0] == 'DAT':
            temp.append(str(i[1]).zfill(4))
        else:
            for j in range(0,len(dictCode)):
                if i[0] == dictCode[j]:
                    # if i[1] not in label:
                    #     temp.append('%s'%(j+1+'%s'%(str(i[1])).zfill(3))                    
                    for m in label:
                        if i[1]==m[0]:
                            temp.append('%s'%(j+1)+'%s'%(str(m[1])).zfill(3))
                        else:
                            temp.append('%s'%(j+1)+'%s'%(str(i[1])).zfill(3))

    # print(label)        
    # print(data)
        
    return temp



def main():
    data = readfile(input('>'))
    # print(data)
    asm = assembler(data)
    wr = writefile(asm)

if __name__ == "__main__":
    main()