from model import Base, Customer, Vendor, Admin, Order, OrderItem, product_promotion, Product, Category
from model import Payment, Cart, CartItem, Shipping, CustomerAddress, Inventory, Review, Promotion
from database import engine, session

Base.metadata.create_all(engine)

# CREATE CUSTOMER

# user1 = Customer(
#     first_name = "Williams",
#     last_name = "Johnson",
#     username = "WilliamsJohnson",
#     email = "Williams@gmail",
#     phone_number = "+123456",
#     password_hash = "mypass"
# )
# user2 = Customer(
#     first_name = "Juliet",
#     last_name = "Pratt",
#     username = "julietpratt",
#     email = "juliet@gmail",
#     phone_number = "+123456789",
#     password_hash = "mypass2"
# )
# session.add_all([user1, user2])
# session.commit()


# CREATE CUSTOMERADDRESS

# WilliamsJohnson = session.query(Customer).filter_by(email = "Williams@gmail").first()
# useraddress1 = CustomerAddress(
#     residence_number = 109,
#     customer = WilliamsJohnson,
#     street = "Damico",
#     city = "Ile_ife",
#     postal_code = "1001-13",
#     country = "Nigeria",
#     description = "This is my 1st address"
# )
# useraddress2 = CustomerAddress(
#     residence_number = 122,
#     customer = WilliamsJohnson,
#     street = "Oduduwa_estate",
#     city = "Ile_ife",
#     postal_code = "1201-15",
#     country = "Nigeria",
#     description = "This is my 2nd address"
# )

# julietpratt = session.query(Customer).filter_by(username = "julietpratt").first()
# useraddress3 = CustomerAddress(
#     residence_number = 122,
#     customer = julietpratt,
#     street = "Ajah",
#     city = "Lagos",
#     postal_code = "1221-98",
#     country = "Nigeria",
#     description = "This is my own address"
# )
# useraddress4 = CustomerAddress(
#     residence_number = 188,
#     customer = julietpratt,
#     street = "Badore",
#     city = "Lagos",
#     postal_code = "1111-38",
#     country = "Nigeria",
#     description = "This is my own 2nd address"
# )
# session.add(useraddress4)
# session.commit()


# CREATE CATEGORY

# categ1 = Category(
#     name = "Home Appliances",
#     parentcategory = "Appliances"
# )
# categ2 = Category(
#     name = "Workshop Appliances",
#     parentcategory = "Appliances"
# )
# categ3 = Category(
#     name = "Big Appliances",
#     parentcategory = "Appliances"
# )
# session.add_all([categ1, categ2, categ3])
# session.commit()


# CREATE VENDOR
ven1 = Vendor(
    first_name = "Jumia",
    last_name = "Global Ltd",
    username = "Jumia Global Ltd",
    email = "jumia@gmail.com",
    phone_number = "+234098768",
    address = "234 fredick avenue, rd 2",
    password_hash = "password1"
)
ven2 = Vendor(
    first_name = "Goody",
    last_name = "Enterprise",
    username = "Goody Enterprise",
    email = "goody@gmail.com",
    phone_number = "+234672094",
    address = "546 badore area, villa estate",
    password_hash = "password2"
)
ven3 = Vendor(
    first_name = "Ebony",
    last_name = "Food Mart",
    username = "Ebony Food Mart",
    email = "Ebony@gmail.com",
    phone_number = "+2344455332",
    address = "987 Oduduwa estate",
    password_hash = "password3"
)
session.add_all([ven1, ven2, ven3])
session.commit()



 
# Read all users
# users = session.query(User).all()
# for user in users:
#     print(user)

#Read a single user
# user = session.query(User).filter_by(id=2).first()
# print(user)

#Update user
# user = session.query(User).filter_by(id=2).first()
# user.country = "UK"
# user.city = "london"

# session.commit()

#Delete user
# user = session.query(User).filter_by(id=3).first()

# session.delete(user)
# session.commit()
