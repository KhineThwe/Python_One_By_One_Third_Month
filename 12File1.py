#file handling mechanism
#1.File open ---> mode "r" "w" "a"
#r ---> IOError file shi yin open ----> ma shi yin error
#w ---> create ---> Mg Mg
#a ---> Mg Mg Ag Ag
#rb ----> binary format
#r+ ---> read,write
#rb+ ----> read,write
#2.File close
#file obj return
file = open("data.txt","r")
if file:
    print("Success of opening file")
    data = file.read(8)#no para ---> all read
    print(data)
else:
    print("Fail of opening file")
file.close()

