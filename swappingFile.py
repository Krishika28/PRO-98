def swapFileData  ():
    fileName1 = input("Enter the file name: ")
    fileName2 = input("Enter the file name: ")

    with open(fileName1,'r') as a:
        data_a = a.read()
    with open(fileName2,'r') as a:
        data_b = a.read()
    with open(fileName1,'w') as a:
        a.write(data_b)
    with open(fileName2,'w') as a:
        a.write(data_a)

swapFileData()   