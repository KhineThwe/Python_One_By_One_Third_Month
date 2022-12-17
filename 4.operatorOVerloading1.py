class Number:
    def __init__(self,num):
        self.num = num
    def __neg__(self):
        print("negative operator")
        return self.num

n1 = Number(5)
print(-n1)
