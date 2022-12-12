#seek က file pointer ကိုယ်လိုချင်သလို ရွေ့ ချင်တဲ့အခါသုံး
#seek function ---> parameter 2 --> offset,whence ---> 2,0 or 1 or 2
#2,1-->1 current 0 start 2 file end
#2,2
#python 3 --> os module
#file.seek(0,os.SEEK_SET)
#file.seek(0,os.SEEK_END)
import os
with open("data.txt","a+") as file:
    if file:
        print("Current Position",file.tell())
        file.seek(2,os.SEEK_SET)
        print("Current moving 2 position",file.tell())
        file.seek(0,os.SEEK_END)
        print("Current position",file.tell())#5
        file.seek(file.tell()-5, os.SEEK_SET)
        print("Current position", file.tell())
        file.seek(15,os.SEEK_SET)
        print("Current position", file.tell())

    else:
        print("Something wrong")
