#this lab will check data from src file, if data is out of the specified range the program will show error

#read src file from location and return data in file as data in array
def readfile(sourcefile):
    with open(sourcefile,'r') as dataSource:
        data = dataSource.read().split()
    return data

#this function will analyze data
def analyzeData(data):
    for i in data:   
       
        if int(i)>=0 and int(i)<2**32:
            continue
        else:            
            return "Error! Data is out of range."
               
    return True

def writefile(data):
         
    with open('ouputLab02.src','w') as datafile:
        for i in data:
            datafile.write(i)
    return 'Done'

def main():
    print('input file')
    source = input('>')
    data = readfile(source)
    result = analyzeData(data)
    if result==True:
        print(writefile(data))
    else:
        print(result)
    

if __name__ == "__main__":
    main()