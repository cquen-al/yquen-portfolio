from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from database import db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/db_bakery'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

from models import Product, Order, OrderItem, Message

#home page
@app.route("/")
def home():
    products = Product.query.filter_by(is_best_seller=True).order_by(Product.display_order).all()
    return render_template("home.html", products=products)

#products page
@app.route("/products")
def products():
    products = Product.query.all()
    return render_template("products.html", products=products)

#place order
@app.route("/order", methods=["GET", "POST"])
def order():
    products = Product.query.all()
    if request.method == "POST":
        name = request.form.get("customer_name")
        phone = request.form.get("phone")
        address = request.form.get("address")
        product_ids = request.form.getlist("product_id")
        quantities = request.form.getlist("quantity")

        
        if not product_ids:
            return "No products selected", 400

        
        new_order = Order(customer_name=name, phone=phone, address=address)
        db.session.add(new_order)
        db.session.commit()  

        
        order_items = []
        for pid, qty in zip(product_ids, quantities):
            product = Product.query.get(pid)
            item = OrderItem(
                order_id=new_order.id,
                product_id=product.id,
                quantity=int(qty),
                price=product.price
            )
            db.session.add(item)
            order_items.append({
                "name": product.name,
                "quantity": qty,
                "price": product.price
            })

        db.session.commit()

        return render_template(
            "order_success.html",
            order_id=new_order.id,
            customer=name,
            items=order_items
        )

    return render_template("order.html", products=products)

#contact form
@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        
        required_fields = ['first_name', 'last_name', 'email', 'phone', 'message']
        for field in required_fields:
            if field not in request.form:
                return f"Missing required field: {field}", 400
        
        message = Message(
            first_name=request.form["first_name"],
            last_name=request.form["last_name"],
            email=request.form["email"],
            phone=request.form["phone"],
            message=request.form["message"]
        )
        db.session.add(message)
        db.session.commit()
        return render_template("contact.html", success="Message sent successfully!")
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)
