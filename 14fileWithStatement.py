#with statement
with open("data.txt","r") as file:
    if file:
        data = file.read()
        print(data)
    else:
        print("Error")
