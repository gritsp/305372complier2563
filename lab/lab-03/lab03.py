#this lab will check data from src file, if data is out of the specified range the program will show error

#read src file from location and return data in file as data in array
def readfile(sourcefile):
    with open(sourcefile,'r') as dataSource:
        data = dataSource.read().split()
    return data

#this function is semantic analysis
def semanticAnalyze(data):
    for i in data:       
        if int(i)>=0 and int(i)<2**32:
            continue
        else:            
            return False
               
    return True

#this is syntax analysis
def syntaxAnalyze(data):
    for i in data:
        if i.isdigit() == False:
            return True
    return False

#this is syntax analysis combined with semantic analysis
def analysisData(data):
    for i in data:
        if i.isdigit()==True:
            if int(i)>=0 and int(i)<2**32:
                continue
            else:            
                return i+" is not in range 0–2,147,483,647."
        else:
            return "'"+i+"' is not a number."
    return True

def writefile(data):           
    with open('ouputLab03.src','w') as datafile:
        for i in data:
            datafile.write(i)
    return True

def main():
    print('input file')
    source = input('>')
    data = readfile(source)
    anaData = analysisData(data)
    if anaData==True:
        writefile(data)
    else:
        print(anaData)

    # print(writefile(data,result))
    

if __name__ == "__main__":
    main()