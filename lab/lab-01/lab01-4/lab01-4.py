#this lab is reading the .src file and export data to a python file. Next show output from C++ file.

#read src file from location and return data in file as data variable
def readfile(sourcefile):
    with open(sourcefile,'r') as dataSource:
        data = dataSource.read()
    return data

#write cpp file from data
def writefile(data):
    with open('ouputLab01-4.cpp','w') as datafile:
        cppfile = '#include<iostream>\n\
        using namespace std;\n\
        int main() {\n\
            cout <<"'+data+'";\n\
            return 0;\n}'
        return datafile.write(cppfile)

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