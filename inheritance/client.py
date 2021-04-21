from mobile_tech import Mobile
from laptop_tech import Laptop
from tech_product import Tech
from sales_person import SalesPerson
from datetime import date, datetime

phone_1 = Mobile("Iphone 11", 60000, 500, 'Black', '1920-1080', 10)
phone_2 = Mobile("Iphone 12", 70000, 530, 'Black', '1920-1080', 12)
phone_3 = Mobile("Iphone 13", 80000, 550, 'Black', '1920-1080', 13)

laptop_1 = Laptop("asdf 11", 160333, 1.6, 'fflack', 8, 'ryzen', 512)
laptop_2 = Laptop("asdf 11", 260333, 530, 'fflack', 8, 'ryzen', 512)
laptop_3 = Laptop("asdf 11", 233343, 530, 'fflack', 8, 'ryzen', 512)

print(laptop_1)
print(phone_1)

phone_1.apply_discount()
print(phone_1.price)

print(Tech.get_total_products())

print(laptop_3.calculate_shipping_cost(10))

print(laptop_1.price)
laptop_1.set_double_price()
print(laptop_1.price)

print(laptop_3)
laptop_3.change_specs(32, 1000, 256)
print(laptop_3)

sales_person_1 = SalesPerson(
    'Majid', 'Ali', 40000, date(2020, 5, 1)
)

sales_person_1.sell_products(phone_1)
sales_person_1.sell_products(phone_2)
sales_person_1.sell_products(laptop_1)
sales_person_1.sell_products(laptop_2)

print(sales_person_1.total_products_sold())

sales_person_1.display_sales()

print(sales_person_1.calculate_commission(0.2))

sales_person_1.sort_by_price()
sales_person_1.display_sales()
