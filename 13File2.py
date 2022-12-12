#ReadLine Vs ReadLines
#ReadLine ---> return string
#Readlines ---> list ---> \n
file = open("data.txt","r")
file2 = open("data.txt","r")

if file:
    print("Success")
    data = file.readline()
    print(data)
    print("Reading with readlines")
    data = file2.readlines()
    print(data)
else:
    print("Error")
file.close()
file2.close()
