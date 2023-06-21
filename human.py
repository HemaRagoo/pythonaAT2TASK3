from letterbox import Letterbox
from letter import Letter
from postoffice import PostOffice


class Human:

    def __init__(self, name: str, age: int, gender: str):
        self.name = name
        self.age = age
        self.gender = gender




class Customer(Human):

    def __init__(self, name: str, age: int, gender: str, address: str):
        super().__init__(name, age, gender)
        self.letterbox = Letterbox()
        self.senders_letter = None
        self.address = address

    def create_letter(self, message: str, receiver):
        if self.letterbox.sent_letter is None:
            self.senders_letter = Letter(self, message, receiver)

    def send_letter(self, receiver: PostOffice):
        receiver.mailbox = self.senders_letter

    def read_letter(self):
        if self.letterbox.sent_letter is not None:
            self.letterbox.sent_letter.is_read = True
        self.letterbox.sent_letter = None

class Postie(Human):

    def __init__(self, name: str, age: int, gender: str):
        super().__init__(name, age, gender)
        self.senders_letter = None


    def collect_from_postoffice(self, postoffice: PostOffice):
        #if postoffice mailbox isnt empty then the letter is in the mailbox
        if postoffice.mailbox:
            self.senders_letter = postoffice.mailbox

    def deliver_mail(self, receiver: Customer):
        if not receiver.letterbox.sent_letter:
            receiver.letterbox.sent_letter = self.senders_letter


if __name__ == '__main__':
    alice = Human("Alice", 19, "Female")
    bob = Human("Bob", 18, "Male")
    charli = Human("Charli", 18, "Male")



