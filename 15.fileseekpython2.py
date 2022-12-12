with open("data.txt","r") as file:
    if file:
        print("The file pointer at byte: ",file.tell())
        file.seek(2,1)#current position
        print("The file pointer after 2 moves: ", file.tell())
        file.seek(5,0)#start
        print("Fp from 0 after 5 moved pos: ",file.tell())
        file.seek(5,1)#1 next current
        print("Current file pointer ",file.tell())
        file.seek(1,2)#end
        print("Going to the end",file.tell())
        file.seek(20,2)
        print("Going to the end",file.tell())
        
    else:
        print("something wrong")
