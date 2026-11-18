from flask import Blueprint, render_template, request, redirect, url_for

orders = Blueprint('orders', __name__,  template_folder='templates')

@orders.route('/orders')
def orders_page():
    # Logic to fetch and display orders
    return render_template('orders/orders.html')