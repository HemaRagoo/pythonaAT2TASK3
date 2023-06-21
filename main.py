from human import Customer, Postie
from postoffice import PostOffice

hema = Customer("Hema", 19, "Female", "36C Gardiner Street East Perth")
mustafa = Customer("Mustafa", 19, "Male", "12BN Adelaide Tce Balga")
hema.create_letter("Hi Mustafa", mustafa)


charli = Postie("Charli",18, "Male")

postoffice=PostOffice("12 Belmont Way")

hema.send_letter(postoffice)
charli.collect_from_postoffice(postoffice)
charli.deliver_mail(mustafa)

mustafa.read_letter()
print(mustafa.letterbox.sent_letter)
