import sqlite3
from django.shortcuts import render
from bangazonapi.models import Customer
from bangazonreports.views import Connection

def customer_favorites_list(request):
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

            cmd = """
            SELECT DISTINCT
			    customer_user.first_name || ' ' || customer_user.last_name AS Customer_name,
			    seller_user.first_name || ' ' || seller_user.last_name AS Favorited_seller
            FROM bangazonapi_favorite f
            JOIN bangazonapi_customer  seller ON seller.id = f.seller_id
			JOIN auth_user seller_user ON seller.user_id = seller_user.id
			JOIN bangazonapi_customer customer ON customer.id = f.customer_id
            JOIN auth_user customer_user ON customer.user_id = customer_user.id
            """

            db_cursor.execute(cmd)

            dataset = db_cursor.fetchall()

            favorited_sellers = {}

            for row in dataset:
                # Get customer
                    # write SQL 
                    # use Django ORM i.e. customer.objects.get()
                # Get customer favorite_sellers
                    # write SQL
                    # use Django ORM i.e. favorite.objects.get()
                customer = row['Customer_name']
                
                if customer in favorited_sellers:
                    favorited_sellers[customer].append(row['Favorited_seller'])
                else:
                    favorited_sellers[customer] = [row['Favorited_seller']]


            template = 'favorites/favoritedsellers.html'
            context = {
                'customer_favorites_list': favorited_sellers
            }

            return render(request, template, context)
