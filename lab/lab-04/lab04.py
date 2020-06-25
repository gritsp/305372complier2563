#this lab will check data from src file, if data is out of the specified range the program will show error

#read src file from location and return data in file as data in array
def readfile(sourcefile):
    with open(sourcefile,'r') as dataSource:
        data = dataSource.read().split()
    return data

#this function is semantic analysis
def semanticAnalyze(data):
    temp = []
    for i in data:       
        if i.isdigit() and int(i)>=0 and int(i)<2**32:
            continue
        else:            
            temp.append(i)               
    if temp==[]:
        return True
    else:
        return temp

#this is syntax analysis
def syntaxAnalyze(data):
    temp = []
    for i in data:
        if i.isdigit() == False:
            temp.append(i)
    if temp==[]:
        return True
    else:
        return temp

#this is syntax analysis combined with semantic analysis
# def analysisData(data):
#     for i in data:
#         if i.isdigit()==True:
#             if int(i)>=0 and int(i)<2**32:
#                 continue
#             else:            
#                 return i+" is not in range 0–2,147,483,647."
#         else:
#             return "'"+i+"' is not a number."
#     return True

def lexicalAnalyze(data):
    alp = ['+','-','*','/','(',')']
    temp = []
    for i in data:
        if i.isnumeric()==False and i[0] not in alp and i[0].isalpha()==False:
            temp.append(i)
    if temp==[]:
        return True
    else:
        return temp

def writefile(data):           
    with open('ouputLab04.src','w') as datafile:
        for i in data:
            datafile.write(i+' ')
    return True

def main():
    print('input file')
    source = input('>')
    data = readfile(source)
    lexAna = lexicalAnalyze(data)
    syntAna = syntaxAnalyze(data)
    semtAna = semanticAnalyze(data)
    if lexAna != True:
        for i in lexAna:
            print(i+' is not valid.')
    if syntAna != True:
        for i in syntAna:
            print("'"+i+"' is not a number.")
    if semtAna != True:
        for i in semtAna:
            print(i+' is out of range 0-2,147,483,647.')
    if lexAna==True and syntAna==True and semtAna==True:
        writefile(data)
        print('Done')   

    

if __name__ == "__main__":
    main()