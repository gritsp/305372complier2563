#this lab is reading the .src file and export data to a python file. Next show output from C# file.

#read src file from location and return data in file as data variable
def readfile(sourcefile):
    with open(sourcefile,'r') as dataSource:
        data = dataSource.read()
    return data

#write C# file from data
def writefile(data):
    with open('ouputLab01-5.cs','w') as datafile:
        csfile = 'using System;\n\
            namespace Lab015{\n\
                class Program{\n\
                    static void Main(string[] args){\n\
                        Console.Write("'+data+'");\n\
                            }}}'
        return datafile.write(csfile)

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