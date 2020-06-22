#this lab is reading the .src file and export data to a python file. Next show output from python file.

#read src file from location and return data in file as data variable
def readfile(sourcefile):
    with open(sourcefile,'r') as dataSource:
        data = dataSource.read()
    return data

#write txt file from data
def writefile(data):
    with open('ouputLab01-2.py','w') as datafile:
        pyfile = 'print("'+data+'")'
        return datafile.write(pyfile)

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