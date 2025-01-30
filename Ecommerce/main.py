from model import Base, Customer, Vendor, Admin, Order, OrderItem, product_promotion, Product, Category
from model import Payment, Cart, CartItem, Shipping, CustomerAddress, Inventory, Review, Promotion
from database import engine, session

Base.metadata.create_all(engine)

# create customer
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

julietpratt = session.query(Customer).filter_by(username = "julietpratt").first()

# useraddress3 = CustomerAddress(
#     residence_number = 122,
#     customer = julietpratt,
#     street = "Ajah",
#     city = "Lagos",
#     postal_code = "1221-98",
#     country = "Nigeria",
#     description = "This is my own address"
# )

useraddress4 = CustomerAddress(
    residence_number = 188,
    customer = julietpratt,
    street = "Badore",
    city = "Lagos",
    postal_code = "1111-38",
    country = "Nigeria",
    description = "This is my own 2nd address"
)
session.add(useraddress4)
session.commit()








# Create user
# user1 = User(
#     first_name = "Opeyemi",
#     last_name= "Samuel",
#     country= "Nigeria",
#     city= "Ibadan",
#     phone_number= "978654323",
#     password= "mypass1"
# )

# user2 = User(
#     first_name = "Johnson",
#     last_name= "Williams",
#     country= "UAE",
#     city= "Dubai",
#     phone_number= "+90978654323",
#     password= "mypass2"
# )

# user3= User(
#     first_name = "Elizabeth",
#     last_name= "Keen",
#     country= "USA",
#     city= "New york",
#     phone_number= "+709978654323",
#     password= "mypass3"
# )

# session.add(user3)
# session.commit()

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


#Create expense
# expense = Expenses(
#     user_id = 1,
#     title= "Something new",
#     description= "New start of a great thing",
#     amount= 304.90
# )
# session.add(expense)
# session.commit()