from address import Address
from mailing import Mailing

to_address = Address("190013","London","Baker Street","221","1")
from_address = Address("111001","Moscow","Red Square","12","7")

mailing1 = Mailing(to_address,from_address,12000,"Abc123")

print("Отправление ", mailing1.track , "из" , from_address, "в", to_address , ".Стоимость", mailing1.cost, "рублей")