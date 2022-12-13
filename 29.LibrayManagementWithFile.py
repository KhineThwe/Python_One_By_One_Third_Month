import datetime
import os
import random

class LMS:
    """This class is used to keep record of books library
       It has total four module.
       1.Display Books
       2.Issue Books
       3.Return Books
       4.Add Books
    """
    def __init__(self,list_of_books,library_name):
        self.list_of_books = list_of_books
        self.library_name = library_name
        self.books_dict = {}
        id = random.randint(100,999)
        with open(self.list_of_books) as bk:
            content = bk.readlines()
        for line in content:
            self.books_dict.update({str(id):{"books_title":line.replace("\n",""),
                                             "lender_name":"",
                                             "Issue_date":"",
                                             "Status":"Available"}})
            # print(self.books_dict)
            id += 1

    def display_books(self):
        print("_______________List Of Books__________________")
        print("Books ID","\t","Title")
        print("______________________________________________")
        for key,value in self.books_dict.items():
            print(key,"\t\t",value.get("books_title"),"-[",value.get("Status"),"]")

    def Issue_books(self):
        books_id = input("Enter books Id: ")
        current_date = datetime.datetime.now().strftime("%Y-%m_%d %H:%M:%S")
        if books_id in self.books_dict.keys():
            if self.books_dict[books_id]["Status"] == "Available":
                your_name = input("Enter your name")
                self.books_dict[books_id]["lender_name"] = your_name
                self.books_dict[books_id]["Issue_date"] = current_date
                self.books_dict[books_id]["Status"] = "Already Issued"
                print("Books Issued Successfully!")
            elif self.books_dict[books_id]["Status"] == "Already Issued":
                print(f'This books is already issued to {self.books_dict[books_id]["lender_name"]} on'
                      f'{self.books_dict[books_id]["Issue_date"]}')
                return self.Issue_books()
        else:
            print("Book Id Not Found!!!")
            return self.Issue_books()


if __name__ == "__main__":
    try:
        myLMS = LMS("List_of_books.txt","Python's Library")
        myLMS.display_books()
        myLMS.Issue_books()
        myLMS.display_books()
    except Exception as e:
        print("Something wrong!Please Check your input!")
