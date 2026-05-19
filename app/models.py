from typing import List, Optional
from datetime import datetime, timezone
from sqlalchemy import String, Integer, Float, ForeignKey, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import db

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(64), index=True, unique=True)
    email: Mapped[str] = mapped_column(String(120), index=True, unique=True)
    password_hash: Mapped[Optional[str]] = mapped_column(String(256))
    created_at: Mapped[datetime] = mapped_column(DateTime, default=lambda: datetime.now(timezone.utc))

    # İlişkiler
    vehicles: Mapped[List["Vehicle"]] = relationship(back_populates="owner", cascade="all, delete-orphan")
    orders: Mapped[List["Order"]] = relationship(back_populates="user", cascade="all, delete-orphan")

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<User {self.username}>'

class Vehicle(db.Model):
    __tablename__ = 'vehicles'
    id: Mapped[int] = mapped_column(primary_key=True)
    brand: Mapped[str] = mapped_column(String(64))
    model_name: Mapped[str] = mapped_column(String(64))
    year: Mapped[int] = mapped_column(Integer)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))

    # İlişkiler
    owner: Mapped["User"] = relationship(back_populates="vehicles")

    def __repr__(self):
        return f'<Vehicle {self.brand} {self.model_name} {self.year}>'

class Product(db.Model):
    __tablename__ = 'products'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(128), index=True)
    category: Mapped[str] = mapped_column(String(64), index=True)
    specs: Mapped[Optional[str]] = mapped_column(String(256))
    price: Mapped[float] = mapped_column(Float)

    # İlişkiler
    orders: Mapped[List["Order"]] = relationship(back_populates="product")

    def __repr__(self):
        return f'<Product {self.name}>'

class Order(db.Model):
    __tablename__ = 'orders'
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    product_id: Mapped[int] = mapped_column(ForeignKey('products.id'))
    quantity: Mapped[int] = mapped_column(Integer, default=1)
    order_date: Mapped[datetime] = mapped_column(DateTime, default=lambda: datetime.now(timezone.utc))

    # İlişkiler
    user: Mapped["User"] = relationship(back_populates="orders")
    product: Mapped["Product"] = relationship(back_populates="orders")

    def __repr__(self):
        return f'<Order {self.id} by User {self.user_id}>'

from app import login_manager

@login_manager.user_loader
def load_user(id):
    return db.session.get(User, int(id))
