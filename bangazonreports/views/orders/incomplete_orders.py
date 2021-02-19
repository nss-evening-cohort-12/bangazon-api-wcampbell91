import sqlite3
from django.shortcuts import render
from bangazonapi.models import Product
from bangazonreports.views import Connection

def incomplete_orders_list(request):
    if request.method == "GET":
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

            cmd = """
            SELECT 
                o.id as 'order',
                u.first_name || ' ' || u.last_name as 'full name',
                SUM(price) as 'total price'
            FROM bangazonapi_order o
            JOIN bangazonapi_customer c ON o.customer_id = c.id
            JOIN auth_user u ON u.id = c.user_id
            JOIN bangazonapi_orderproduct op ON op.order_id = o.id
            JOIN bangazonapi_product p ON p.id = op.product_id
            WHERE payment_type_id IS NULL
            GROUP BY o.id
            """
            db_cursor.execute(cmd)

            dataset = db_cursor.fetchall()

            list_of_incomplete_orders = []

            for row in dataset:
                order = {
                    'order_id': row['order'],
                    'full_name': row['full name'],
                    'total_price': row['total price']
                }
                list_of_incomplete_orders.append(order)

            
            template = 'orders/incompleteorders.html'
            context = {
                'completed_orders': list_of_incomplete_orders
            }

            return render(request, template, context)
