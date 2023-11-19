from flask import Blueprint, render_template, request, flash, redirect, url_for, session
from .models import User, Product
from werkzeug.security import generate_password_hash, check_password_hash
from . import db   ##means from __init__.py import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('auth.succsess_login'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')
    
    return  render_template("login.html", user=current_user)

@auth.route('/Succesfull-Login')
def succsess_login():
    return render_template("Succsesful_login.html")


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out successfully!', category='success')
    return redirect(url_for('auth.login'))

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        #checking for validation
        if len(email) < 4:
            flash('Email must be greater than 3 characters', category='error')
        elif len(first_name) <2:
            flash('First name must be greater than 1 character', category='error')
        elif password1 != password2:
            flash("Passwords don't match", category='error')
        elif len(password1) < 7:
            flash('Passwords must be at least 7 characters', category='error')
        else:
            #add user to database
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Acount created!', category='success')
            flash('Account created!', category='success')
            return redirect(url_for('auth.login'))
    
    return render_template("sign_up.html", user=current_user)

@auth.route('/shop')
def shop():
    product = Product.query.all()
    return render_template("product_caller.html", product=product)

@auth.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    product_id = request.form.get('product_id')
    if 'cart' not in session:
        session['cart'] = []
    # Add the product_id to the cart_items list
    # product = Product.query.get(product_id)
    session['cart'].append(product_id)
    session.modified = True
    return redirect('/Shopping-cart')

@auth.route('/Shopping-cart', methods=['POST', 'GET'])
def Shopping_Cart():
    # Pass the cart_items list to the auth.html template

    if request.method == 'POST':
        delete = request.form.get('delete')
        if 'cart' in session:
            session['cart'].remove(delete)
            session.modified = True

    cart_items = []
    total_price = 0

    cart = session.get('cart', [])  # Use get() method with a default value of an empty list

    for item in cart:
        product = Product.query.get(item)
        cart_items.append(product)
        total_price += product.price

    return render_template('Shopping_cart.html', cart_items=cart_items, total_price=total_price)


@auth.route('/add-product', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        product_name = request.form.get('product_name')
        price = request.form.get('price')
        image_path = request.form.get('image_path')
        carbon_footprint = request.form.get('carbon_footprint')

        #add product to database
        new_product = Product(product_name=product_name, price=price, image_path=image_path, carbon_footprint=carbon_footprint)
        db.session.add(new_product)
        db.session.commit()
        return redirect(url_for('auth.shop'))

    return render_template('add_products.html')

@auth.route('/Payment')
def Payment():
    cart_items = []
    total_price = 0

    cart = session.get('cart', [])  # Use get() method with a default value of an empty list

    for item in cart:
        product = Product.query.get(item)
        cart_items.append(product)
        total_price += product.price

    return render_template('Payment.html', cart_items=cart_items, total_price=total_price)

@auth.route('/Payment-Successfull')
def Purchase_Completed():
    return render_template('Thanks_Purchase.html')
