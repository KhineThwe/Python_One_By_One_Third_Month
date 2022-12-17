#abstraction
from abc import ABC,abstractmethod
class Price(ABC):
    def print_slip(self,amount):
        print('Payment amount $',amount)

    @abstractmethod
    def payment(self):
        print("This is important from abstract method")

class CreditPayment(Price):
    def payment(self,amount):
        super().payment()
        print("Payment with credit card $",amount)
class MobileBanking(Price):
    def payment(self,amount):
        super().payment()
        print("Payment with credit card $", amount)

obj = CreditPayment()
obj.print_slip(1000)
obj.payment(1000)

obj = MobileBanking()
obj.print_slip(2000)
obj.payment(2000)
