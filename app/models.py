from typing import List, Optional
from datetime import datetime, timezone, date
from sqlalchemy import String, Integer, Float, ForeignKey, DateTime, Date, Boolean
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
    is_admin: Mapped[bool] = mapped_column(Boolean, default=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=lambda: datetime.now(timezone.utc))

    # İlişkiler
    vehicles: Mapped[List["Vehicle"]] = relationship(back_populates="owner", cascade="all, delete-orphan")
    orders: Mapped[List["Order"]] = relationship(back_populates="user", cascade="all, delete-orphan")
    order_groups: Mapped[List["OrderGroup"]] = relationship(back_populates="user", cascade="all, delete-orphan")
    cart_items: Mapped[List["CartItem"]] = relationship(back_populates="user", cascade="all, delete-orphan")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<User {self.username}>'

# Araçlar ile Ürünler arasındaki çoka-çok ilişki (Uyumlu ürünler)
product_compatibility = db.Table('product_compatibility',
    db.Column('product_id', db.Integer, db.ForeignKey('products.id', ondelete='CASCADE'), primary_key=True),
    db.Column('vehicle_id', db.Integer, db.ForeignKey('vehicles.id', ondelete='CASCADE'), primary_key=True)
)

class Vehicle(db.Model):
    __tablename__ = 'vehicles'
    id: Mapped[int] = mapped_column(primary_key=True)
    brand: Mapped[str] = mapped_column(String(64))
    model_name: Mapped[str] = mapped_column(String(64))
    year: Mapped[int] = mapped_column(Integer)
    plate: Mapped[Optional[str]] = mapped_column(String(20))
    fuel_type: Mapped[Optional[str]] = mapped_column(String(32))
    transmission: Mapped[Optional[str]] = mapped_column(String(32))
    engine_power: Mapped[Optional[str]] = mapped_column(String(32))
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    
    # Yeni eklenen tarih alanları
    inspection_date: Mapped[Optional[date]] = mapped_column(Date)
    maintenance_date: Mapped[Optional[date]] = mapped_column(Date)

    # İlişkiler
    owner: Mapped["User"] = relationship(back_populates="vehicles")
    notifications: Mapped[List["VehicleNotification"]] = relationship(back_populates="vehicle", cascade="all, delete-orphan")
    compatible_products: Mapped[List["Product"]] = relationship(
        secondary=product_compatibility,
        back_populates="compatible_vehicles"
    )

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __repr__(self):
        return f'<Vehicle {self.brand} {self.model_name} {self.year}>'

class VehicleNotification(db.Model):
    __tablename__ = 'vehicle_notifications'
    id: Mapped[int] = mapped_column(primary_key=True)
    vehicle_id: Mapped[int] = mapped_column(ForeignKey('vehicles.id'))
    title: Mapped[str] = mapped_column(String(128))
    due_date: Mapped[date] = mapped_column(Date)
    is_completed: Mapped[bool] = mapped_column(Boolean, default=False)
    
    # İlişkiler
    vehicle: Mapped["Vehicle"] = relationship(back_populates="notifications")
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __repr__(self):
        return f'<Notification {self.title} for Vehicle {self.vehicle_id}>'

class Product(db.Model):
    __tablename__ = 'products'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(128), index=True)
    category: Mapped[str] = mapped_column(String(64), index=True)
    specs: Mapped[Optional[str]] = mapped_column(String(256))
    price: Mapped[float] = mapped_column(Float)
    stock: Mapped[int] = mapped_column(Integer, default=10, server_default='10')
    image_url: Mapped[Optional[str]] = mapped_column(String(256))

    # İlişkiler
    orders: Mapped[List["Order"]] = relationship(back_populates="product")
    cart_items: Mapped[List["CartItem"]] = relationship(back_populates="product", cascade="all, delete-orphan")
    compatible_vehicles: Mapped[List["Vehicle"]] = relationship(
        secondary=product_compatibility,
        back_populates="compatible_products"
    )

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __repr__(self):
        return f'<Product {self.name}>'

class OrderGroup(db.Model):
    __tablename__ = 'order_groups'
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    order_date: Mapped[datetime] = mapped_column(DateTime, default=lambda: datetime.now(timezone.utc))
    status: Mapped[str] = mapped_column(String(32), default="Beklemede")
    address: Mapped[str] = mapped_column(String(256))
    city: Mapped[str] = mapped_column(String(64))
    phone: Mapped[str] = mapped_column(String(32))
    total_price: Mapped[float] = mapped_column(Float)

    user: Mapped["User"] = relationship(back_populates="order_groups")
    orders: Mapped[List["Order"]] = relationship(back_populates="order_group", cascade="all, delete-orphan")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class Order(db.Model):
    __tablename__ = 'orders'
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    product_id: Mapped[int] = mapped_column(ForeignKey('products.id'))
    order_group_id: Mapped[Optional[int]] = mapped_column(ForeignKey('order_groups.id'))
    quantity: Mapped[int] = mapped_column(Integer, default=1)
    price_at_purchase: Mapped[Optional[float]] = mapped_column(Float)
    order_date: Mapped[datetime] = mapped_column(DateTime, default=lambda: datetime.now(timezone.utc))

    # İlişkiler
    user: Mapped["User"] = relationship(back_populates="orders")
    product: Mapped["Product"] = relationship(back_populates="orders")
    order_group: Mapped[Optional["OrderGroup"]] = relationship(back_populates="orders")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __repr__(self):
        return f'<Order {self.id} by User {self.user_id}>'

class CartItem(db.Model):
    __tablename__ = 'cart_items'
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    product_id: Mapped[int] = mapped_column(ForeignKey('products.id'))
    quantity: Mapped[int] = mapped_column(Integer, default=1)
    added_at: Mapped[datetime] = mapped_column(DateTime, default=lambda: datetime.now(timezone.utc))

    user: Mapped["User"] = relationship(back_populates="cart_items")
    product: Mapped["Product"] = relationship(back_populates="cart_items")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __repr__(self):
        return f'<CartItem {self.id} for User {self.user_id}>'

from app import login_manager

@login_manager.user_loader
def load_user(id):
    return db.session.get(User, int(id))
