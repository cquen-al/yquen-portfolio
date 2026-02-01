from database import db
from datetime import datetime

class Product(db.Model):
    __tablename__ = 'tbl_products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Numeric(6, 2), nullable=False)
    image = db.Column(db.String(255), nullable=False)
    category = db.Column(db.String(50))
    is_best_seller = db.Column(db.Boolean, default=False)
    display_order = db.Column(db.Integer, default=0)

class Order(db.Model):
    __tablename__ = 'tbl_orders'
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    address = db.Column(db.Text, nullable=False)
    order_date = db.Column(db.DateTime, default=db.func.current_timestamp())
    status = db.Column(db.String(20), default='Pending')

class OrderItem(db.Model):
    __tablename__ = 'tbl_order_items'
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('tbl_orders.id', ondelete='CASCADE'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('tbl_products.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Numeric(6,2), nullable=False)

class Message(db.Model):
    __tablename__ = 'tbl_messages'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    email = db.Column(db.String(100))
    phone = db.Column(db.String(20))
    message = db.Column(db.Text)
    sent_at = db.Column(db.DateTime, default=datetime.utcnow)
