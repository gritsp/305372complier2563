#this lab is reading the .src file and export data to a text file

#read src file from location and return data in file as data variable
def readfile(sourcefile):
    with open(sourcefile,'r') as dataSource:
        data = dataSource.read()
    return data

#write txt file from data
def writefile(data):
    with open('ouputLab01-1.txt','w') as datafile:
        return datafile.write(data)

def main():
    print('input file')
    source = input('')
    data = readfile(source)
    try:
        writefile(data)
        print("done")
    except:
        print("fail")

if __name__ == "__main__":
    main()