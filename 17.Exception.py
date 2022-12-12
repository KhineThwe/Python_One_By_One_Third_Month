#exception handling --> try except finally
#error 2 file ma shi
#error 1 --> not permitted
#try:
# မိမိ run ချင်သော code
#except:
#   exception ဖြစ်လာခဲ့ရင်အလုပ်လုပ်မယ်
#else:
# exception မဖြစ်လာခဲ့ရင်အလုပ်လုပ်မယ်
#finally:
# ဘယ်လို အခြေအနေ ပဲဖြစ်ဖြစ်အလုပ်လုပ်မယ်
# try:
#     file = open("data999.txt","r")
# except:
#     print("File cannot open")
# finally:
#     print("This finally statement is running")

try:
    data = int(input("Please enter a number : "))
    if data == 10:
        print("Activating exception")
        raise ZeroDivisionError
    else:
        raise TypeError
except ZeroDivisionError:
    print("From Zero Division Error")
except TypeError:
    print("From Type Error")
except Exception as err:
    print(err)
