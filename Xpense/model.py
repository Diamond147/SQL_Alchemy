from typing import List
from sqlalchemy import String,ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column,relationship


class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String(30))
    last_name: Mapped[str] = mapped_column(String(30))
    country: Mapped[str] = mapped_column(String(50))
    city: Mapped[str] = mapped_column(String(50))
    phone_number: Mapped[str] = mapped_column(String(50))
    password: Mapped[str] = mapped_column(String(50))
    expenses:Mapped[List["Expenses"]] = relationship(back_populates="user")

    def __repr__(self) -> str: #Danda repra
       return f"User(id={self.id!r}, first_name={self.first_name!r}, last_name={self.last_name!r},\
       country={self.country!r}, city={self.city!r}, phone_number={self.phone_number!r}, password={self.password!r})"
    

class Expenses(Base):
    __tablename__ = "expenses" 

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id = mapped_column(ForeignKey("users.id"))
    title: Mapped[str] = mapped_column(String(50))
    description: Mapped[str] = mapped_column(String(100))
    amount: Mapped[float]
    user: Mapped[List[User]] = relationship(back_populates="expenses")

    def __repr__(self) -> str:
       return f"Expenses(id={self.id!r}, user_id={self.user_id!r}, title={self.title!r},\
       description={self.description!r}, amount={self.amount!r})"
    
