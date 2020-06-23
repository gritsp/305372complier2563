#this lab is reading the .src file and export data to a python file. Next show output from C file.

#read src file from location and return data in file as data variable
def readfile(sourcefile):
    with open(sourcefile,'r') as dataSource:
        data = dataSource.read()
    return data

#write c file from data
def writefile(data):
    with open('ouputLab01-3.c','w') as datafile:
        cfile = '#include<stdio.h>\n\
        void main(){\n\
            printf("'+data+'");\n}'
        return datafile.write(cfile)

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