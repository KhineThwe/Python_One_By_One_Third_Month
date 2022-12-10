def print_info(header,info):
    print('******{0}****'.format(header))
    for key,value in info.items():
        print(key,value)
    print("End of information")

print_info('using global function',globals())

if __name__ == "__main__":
    print("Name was changed to main")
else:
    print("They are not changed")
