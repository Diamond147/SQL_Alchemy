from model import Base, User, Expenses
from database import engine, session

Base.metadata.create_all(engine)

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
expense = Expenses(
    user_id = 1,
    title= "Something new",
    description= "New start of a great thing",
    amount= 304.90
)
session.add(expense)
session.commit()