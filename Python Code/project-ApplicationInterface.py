import pandas as pd
import pymysql
from datetime import datetime
import time
import os
from art import *

# Establishing a connection to the database
conn = pymysql.connect(
    host='localhost',
    user='root',
    password='18blc1089*SENSE',
    database='eperfume',
    cursorclass=pymysql.cursors.DictCursor
)

#Function to run a given string sql qury
def run_query(query):
    with conn.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchall()
    conn.commit()
    return result

#Prints common header for application interface for the EPerfume site
def print_header():
    os.system('clear')
    print("-------------------------------------------------------------")
    HEADING = text2art("EPerfume",chr_ignore=True)
    SUBHEADING = "Your Destination for Your Perfume Needs"
    print(HEADING)
    print(f"\t\t{SUBHEADING}")
    print("-------------------------------------------------------------")
    print("-------------------------------------------------------------")

# Function for user login, checks the user password in the database and input to verify
def user_login(logged_in, current_customer_id):
    print("Log in...")
    username = str(input("Enter your username: "))
    #Accessing the customer table
    result = run_query(f"select password from Customer where email = '{username}'")
    result = result[0]['password']
    while (logged_in == False):
        password = input("Enter your password: ")
        if (password == str(result)):
            print("Success! Logging you in")
            logged_in = True
        else:
            print("Please enter the correct password")
            logged_in = False
    current_customer_id = run_query(f"select customer_id from Customer where email = '{username}'")[0]['customer_id']
    return logged_in, current_customer_id

# Function for user sign up, inserts content into the relevant tables
def user_sign_up():
    firstname = str(input("Enter your first name: "))
    lastname = str(input("Enter your last name: "))
    email = str(input("Enter your email: "))
    password = str(input("Enter a password: "))
    phone_num = str(input("Enter your phone number: "))
    address = str("Enter your address in a single line: ")
    #Inserting into customer table
    result = run_query(f"insert into Customer (first_name, last_name, email, password, phone_number, address) Values ('{firstname}', '{lastname}', '{email}', '{password}', '{phone_num}', '{address}')")
    print("Signed Up!")

# Function for user change password, given that they know their original password
def change_password():
    correct = False
    email_input = input("Provide your login email: ")
    result = run_query(f"select password from Customer where email = '{email_input}'")
    while (correct == False):
        confirm = input("Confirm your original password: ")
        if (confirm == str(result[0]['password'])):
            correct = True
            new_password = input("Provide the new password: ")
            #Updating into the customer table
            result = run_query(f"update Customer set password = '{new_password}' where password = '{confirm}' and email = '{email_input}'")
            print("Password Updated!")
        else:
            print("Enter the correct original password!")

#Function to update profile for profile details
def updateprofile(current_customer_id):
    choice_update = int(input("Would you like to update your...\n\t1. First Name\n\t2. Last Name\n\t3. Phone Number\n\t4. Address\n"))
    if choice_update  == 1:
        update_first_name = input("Enter the new First Name:")
        # Updating the first name
        result = run_query(f"Update Customer set first_name = '{update_first_name}'")
    elif choice_update  == 2:
        update_last_name = input("Enter the new Last Name:")
        # Updating the last name
        result = run_query(f"Update Customer set last_name = '{update_last_name}'")
    elif choice_update  == 3:
        update_phone_number = input("Enter the new Phone Number:")
        # Updating the phone number
        result = run_query(f"Update Customer set phone_number = '{update_phone_number}'")
    elif choice_update  == 4:
        update_address = input("Enter the new Address:")
        # Updating the address
        result = run_query(f"Update Customer set address = '{update_address}'")

# Function to view user's profile, and ask if the user needs to update it
def view_profile(current_customer_id):
    #Accesing the Customer table
    result = run_query(f"Select first_name, last_name, email, phone_number, address from Customer where customer_id = {current_customer_id}")
    print(f"Hello, {result[0]['first_name']} {result[0]['last_name']}")
    print("Your Profile:\n--------------------------------------------------")
    print(f"Email/Username: {result[0]['email']}")
    print(f"Phone Number: {result[0]['phone_number']}")
    print(f"Address: {result[0]['address']}")
    print("--------------------------------------------------")
    choice_profile = int(input("Would you like to update your profile? 1. Yes 2. No\n"))
    if choice_profile == 1:
        updateprofile(current_customer_id)
        print("Profile Updated!")

# Function to check the list of available promotions
def view_promotions():
    # Accesing the Promotions table
    result = run_query(f"select promotion_name, start_date, end_date, discount_percent from Promotions")
    df = pd.DataFrame(result)
    pd.options.display.max_columns = 25
    df.style.set_table_styles([{'selector' : '', 
                            'props' : [('border', 
                                        '2px solid green')]}]) 
    if(df.empty):
        print("No Promotions")
    else:
        print(f"\t\t{df.to_string(index=False)}")
    ret = -1
    while ret != 0:
        ret = int(input("Enter 0 to return to the main screen"))
        

# Function to view available categories, and view its subsequent products
def view_categories(current_customer_id):
    # Implement view categories functionality using SQL queries
    print("Categories!")
        # Accesing the categories table
    result = run_query(f"select * from Category")
    df = pd.DataFrame(result)
    pd.options.display.max_columns = 25
    df.style.set_table_styles([{'selector' : '', 
                            'props' : [('border', 
                                        '2px solid green')]}]) 
    choice_category = -1
    while choice_category != 0:
        if(df.empty):
            print("No Products")
        else:
            print(f"\t\t{df.to_string(index=False)}")
            choice_category = int(input("Enter the category index number that you would like to see products for\nEnter 0 to go back to the main menu\n"))
            if choice_category != 0:
                view_inventory(current_customer_id, choice_category)

# Function to view inventory of products with options to move a preferred object to the Wishlist
def view_inventory(current_customer_id, choice_category = -1):
    # Choice category to describe the specific category id or not
    if choice_category == -1:
        #Accessing the product table for all categories
        query = "select * from Products"
    else:
        #Accesing the product table with specific category
        query = f"select * from Products where category_id = {choice_category}"
    result = run_query(query)
    df = pd.DataFrame(result)
    pd.options.display.max_columns = 25
    df.style.set_table_styles([{'selector' : '', 
                            'props' : [('border', 
                                        '2px solid green')]}]) 
    if(df.empty):
        print("No Products")
    else:
        print(f"\t\t{df.to_string(index=False)}")
        choice_product = 0
        choice_product = int(input("Enter 0 to return to the main menu. (OR)\nEnter the product id that would like to add to your wishlist: "))
        if choice_product != 0:
            #Inserting the relevant item into the wishlist
            result = run_query(f"insert into Wishlist (customer_id, product_id) VALUES ({current_customer_id}, {choice_product})")
        print("Succesfully Added to the Wishlist!")

# Function to view wishlist and choose to move preferred products to the Cart with a quantity
def view_wishlist(current_customer_id):
    # Accesing the Wishlist and Products table for display
    result = run_query(f"select Wishlist.wishlist_id, Products.product_id, Products.product_name, Products.price from Wishlist, Products where Wishlist.product_id = Products.product_id and Wishlist.customer_id = {current_customer_id}")
    df = pd.DataFrame(result)
    pd.options.display.max_columns = 25
    df.style.set_table_styles([{'selector' : '', 
                            'props' : [('border', 
                                        '2px solid green')]}]) 
    if(df.empty):
        print("No items in Wishlist")
    else:
        print(f"\t\t{df.to_string(index=False)}")
        choice_wishlist = 3
        choice_wishlist = int(input("Would you like to...\n\t1. Add an Item to the Cart?\n\t2. Remove An Item from Wishlist\n\t3. Return to main menu\n"))
        if choice_wishlist == 1:
            choice_wish = int(input("Enter the wishlist id you would like to add to your cart: "))
            #Getting the relevant values to add to the Cart table
            wishlist = run_query(f"select Wishlist.product_id, Products.price, Products.stock_quantity from Wishlist, Products where Wishlist.product_id = Products.product_id and Wishlist.wishlist_id = {choice_wish} and Wishlist.customer_id = {current_customer_id}")
            quantity_choice = int(input("Enter the quantity of this product that you'd like to add:"))
            remaining = wishlist[0]['stock_quantity']
            if quantity_choice <= remaining: 
                #Inserting into the Cart table
                result = run_query(f"insert into Cart (customer_id, product_id, quantity, price, total_price) VALUES ({current_customer_id}, {wishlist[0]['product_id']}, {quantity_choice}, {wishlist[0]['price']}, {float(wishlist[0]['price']) * float(quantity_choice)})")
                # SQL Trigger automatically deletes the entry for thhat particular product id from the Wishlist table.
                result = run_query(f"CALL ReduceStockQuantity({wishlist[0]['product_id']}, {quantity_choice});")
                print("Added to Cart!")
            else:
                print(f"There isnt enough stock of this item! Stock quantity remaining: {remaining}")
        elif choice_wishlist == 2:
            choice_remove_wishlist = int(input("Enter the product_id you want to delete?"))
            # Choice to remove from Wishlist
            result = run_query(f"DELETE FROM Wishlist WHERE product_id = {choice_remove_wishlist}")
            print("Removed from Wishlist!")
            view_wishlist(current_customer_id)        

# Function to view cart and choose to order your items with specific payment method and updating statuses
def view_cart(current_customer_id):
    # Accesing the Cart, Products tables to display
    result = run_query(f"select Cart.cart_id, Products.product_id, Products.product_name, Cart.quantity, Cart.total_price from Cart, Products where Cart.product_id = Products.product_id and Cart.customer_id = {current_customer_id}")
    df = pd.DataFrame(result)
    pd.options.display.max_columns = 25
    df.style.set_table_styles([{'selector' : '', 
                            'props' : [('border', 
                                        '2px solid green')]}]) 
    if(df.empty):
        print("No Items in Cart")
    else:
        print(f"\t\t{df.to_string(index=False)}")
        cart_choice = 3
        cart_choice = int(input("Would you like to...\n\t1. Order your Cart\n\t2. Remove An Item from Cart\n\t3. Return to main menu\n"))
        if cart_choice == 1:
            #Getting payment info
            payment_type = 1
            payment_method = "Credit Card"
            payment_type = int(input("How would you like to pay?\n\t1. Credit Card\n\t2. Debit Card\n\t3. PayPal\n"))
            if payment_type == 1:
                payment_method = 'Credit Card'
            elif payment_type == 2:
                payment_method = 'Debit Card'
            elif payment_type == 3:
                payment_method = 'PayPal'
            #Obtaining relevant values to then add into the Orders table when placing an order
            #Getting the total amount on the Cart
            tot_amnt = int(run_query(f"select SUM(Cart.total_price) from Cart, Products where Cart.product_id = Products.product_id and Cart.customer_id = {current_customer_id}")[0]['SUM(Cart.total_price)'])
            temp = run_query(f"insert into Orders (customer_id, order_date, status, total_amount) VALUES ({current_customer_id}, CURDATE(), 'Processing', {tot_amnt})")
            orderID = int(run_query(f"select order_id from Orders where customer_id = {current_customer_id} and order_date = CURDATE() ORDER BY order_date DESC")[0]['order_id'])
            product_id_string = ''  
            quantity_string = ''
            price_string = ''
            for i in result:
                product_id_string = product_id_string + str(i['product_id'])
                quantity_string = quantity_string + str(i['quantity'])
                price_string = price_string + str(i['total_price'])
                if (i != result[-1]):
                    product_id_string = product_id_string + ','
                    quantity_string = quantity_string + ','
                    price_string = price_string + ','     
            #Calling stored procedure to process an Order given the arguments           
            result = run_query(f"CALL ProcessOrder({orderID}, {product_id_string}, {quantity_string}, {price_string}, '{payment_method}', {current_customer_id})")  
            print("Thank you for your order!")      
        elif cart_choice == 2:
            choice_remove_cart = int(input("Enter the product_id you want to delete?"))
            #Deleting choice item from Cart
            result = run_query(f"DELETE FROM Cart WHERE product_id = {choice_remove_cart}")
            print("Removed from Cart!")
            view_cart(current_customer_id)
        
# Function to view order history and an option to view detailed history with items, shipment and payment summaries
def view_orders(current_customer_id):
    #Accesing the orders table
    result = run_query(f"select order_id, order_date, total_amount, status from Orders where customer_id = {current_customer_id}")
    df = pd.DataFrame(result)
    pd.options.display.max_columns = 25
    df.style.set_table_styles([{'selector' : '', 
                            'props' : [('border', 
                                        '2px solid green')]}]) 
    if(df.empty):
        print("No Order History")
    else:
        print(f"\t\t{df.to_string(index=False)}")
        choice_order = 0
        choice_order = int(input("Which order id would you like to see?\nEnter 0 to return to the main menu\n"))
        if choice_order != 0:
            #Viewing Order Item History using the Order_Items table
            result_order_item = run_query(f"SELECT Orders.order_id, Products.product_name, Order_Item.quantity, Order_Item.price FROM Orders JOIN Order_Item ON Orders.order_id = Order_Item.order_id JOIN Products ON Order_Item.product_id = Products.product_id WHERE Orders.customer_id = {current_customer_id} and Orders.order_id={choice_order}")
            print("Order Summary for Order\n\tItem Summary:")
            df1 = pd.DataFrame(result_order_item)
            pd.options.display.max_columns = 25
            df1.style.set_table_styles([{'selector' : '', 
                                    'props' : [('border', 
                                                '2px solid green')]}]) 
            if(df1.empty):
                print("No Item History")
            else:
                print(f"\t\t{df1.to_string(index=False)}")
            print("\n\tPayment Summary:")
            #Viewing payment summary using the Payments table
            result_payment = run_query(f"SELECT Orders.order_id, Payments.payment_method, Payments.payment_date FROM Orders JOIN Payments ON Orders.order_id = Payments.order_id WHERE Orders.customer_id = {current_customer_id}")
            df2 = pd.DataFrame(result_payment)
            pd.options.display.max_columns = 25
            df2.style.set_table_styles([{'selector' : '', 
                                    'props' : [('border', 
                                                '2px solid green')]}]) 
            if(df2.empty):
                print("No Payment History")
            else:
                print(f"\t\t{df2.to_string(index=False)}")
            print("\n\tShipment Summary")
            #Viewing shipment summary from the SHipment table
            result_shipment = run_query(f"SELECT Orders.order_id, Shipment.shipment_date, Shipment.tracking_number, Shipment.status FROM Orders JOIN Shipment ON Orders.order_id = Shipment.order_id WHERE Orders.customer_id = {current_customer_id}")
            df3 = pd.DataFrame(result_shipment)
            pd.options.display.max_columns = 25
            df3.style.set_table_styles([{'selector' : '', 
                                    'props' : [('border', 
                                                '2px solid green')]}]) 
            if(df3.empty):
                print("No Shipment History")
            else:
                print(f"\t\t{df3.to_string(index=False)}")
            choice_review = int(input("Would you like to view/leave a review?\n\t1. Yes, view/leave a review\n\t2. Return to Main Menu\n"))
            if choice_review == 1:
                viewandleaveareview(result_order_item[0]['order_id'], current_customer_id)

# Function to initiate a return, given that the product meets certain requirements and that the Order was delivered in the first place
def startreturn(current_customer_id):
    result = run_query(f"select Orders.order_id, Orders.order_date, Orders.total_amount from Orders where Orders.customer_id = {current_customer_id} and Orders.status = 'Delivered'")
    df = pd.DataFrame(result)
    pd.options.display.max_columns = 25
    df.style.set_table_styles([{'selector' : '', 
                            'props' : [('border', 
                                        '2px solid green')]}]) 
    if(df.empty):
        print("No Return History")
    else:
        print(f"\t\t{df.to_string(index=False)}")
    flag = 1
    #Verifying whether the product is eligible for return
    if(int(input("Is the product in its original packaging?\n\t1. Yes\n\t2. No\n")) == 1):
        flag = 1
    elif(input(input("Is the product unopened?\n\t1. Yes\n\t2. No\n")) == 1):
        flag = 1
    else:
        flag = 2
    if (flag ==  1):
        choice_return = int(input("Enter the order id that you would like to Return"))
        #Calling stored procedure to process a refund
        result = run_query(f"CALL RefundOrder({choice_return});")
        print("Return Initiated!")
    else:
        print("You cannot return this order. Sorry!")

# Function to view or leave a review for a specific product within a specific Order
def viewandleaveareview(order_ID, current_customer_id):
    result_order_item = run_query(f"SELECT Orders.order_id, Products.product_name, Order_Item.quantity, Order_Item.price FROM Orders JOIN Order_Item ON Orders.order_id = Order_Item.order_id JOIN Products ON Order_Item.product_id = Products.product_id WHERE Orders.customer_id = {current_customer_id}")
    print("Order Summary for Order\n\tItem Summary:")
    df1 = pd.DataFrame(result_order_item)
    pd.options.display.max_columns = 25
    df1.style.set_table_styles([{'selector' : '', 
                            'props' : [('border', 
                                        '2px solid green')]}]) 
    if(df1.empty):
        print("No Order History")
    else:
        print(f"\t\t{df1.to_string(index=False)}")
        choice_product_review = int(input("Which product_id would you like to view/leave a review?"))
        choice_leave_view = int(input("Would you like to...\n\t1. View reviews\n\t2. Leave a review?\n"))
        if choice_leave_view == 2:
            rating = input("Enter your rating from 1 - 5:")
            review_text = input("Enter your review text:")
            # Inserting into the Reviews table
            result_order = run_query(f"INSERT into Reviews (product_id, customer_id, rating, review_text) VALUES ({choice_product_review}, {current_customer_id}, {rating}, '{review_text}')")
            print("Thank you for your review!")
        else:
            # Just checking the review for that particuar products
            result_review = run_query(f"SELECT Reviews.review_id, Products.product_name, Reviews.rating, Reviews.review_text, Reviews.review_date FROM Reviews JOIN Products ON Reviews.product_id = Products.product_id WHERE Reviews.product_id = {choice_product_review} and Reviews.customer_id = {current_customer_id}")
            print("Reviews:")
            df1 = pd.DataFrame(result_review)
            pd.options.display.max_columns = 25
            df1.style.set_table_styles([{'selector' : '', 
                                    'props' : [('border', 
                                                '2px solid green')]}]) 
            if(df1.empty):
                print("No Reviews")
            else:
                print(f"\t\t{df1.to_string(index=False)}")
    ret = -1
    while ret != 0:
        ret = int(input("Enter 0 to return to the main screen"))

# Close connection to the database
def close_connection():
    conn.close()

def main():
    try:
        # print the header continously
        print_header()
        global logged_in
        global current_customer_id
        logged_in = False
        current_customer_id = -1
        action = int(input("Welcome to EPerfume. Would you like to login or signup\nEnter your choice #:\n\t1. Login\n\t2. Signup\n"))

        #Initial login/signup menu
        if action == 1:
            logged_in, current_customer_id = user_login(logged_in, current_customer_id)
        elif action == 2:
            user_sign_up()
            logged_in, current_customer_id = user_login(logged_in, current_customer_id)
        else:
            print("Enter a valid option")

        if logged_in == False:
            print("User Not Logged In")

        #Loop to display the main menu continously as the user returns back after performing actions.
        #Displayed as a new page every time
        while logged_in == True and current_customer_id != -1:
            time.sleep(1.75)
            print_header()
            print("-----------------------------------------------")
            print("\nWhat would you like to do?\n")
            print("Enter your choice:\n")
            print("\t1. Change Password")
            print("\t2. View Profile")
            print("\t3. View latest promotions")
            print("\t4. View full list of perfume categories")
            print("\t5. View full list of product inventory")
            print("\t6. View your wishlist")
            print("\t7. View your cart")
            print("\t8. View order history")
            print("\t9. Start a return")
            print("\t0. Log Out")
            print("-----------------------------------------------")

            action = int(input())

            #Calling the relevant functions
            if action == 1:
                print_header()
                change_password()
                time.sleep(1.25)
            elif action == 2:
                print_header()
                view_profile(current_customer_id)
                time.sleep(1.25)
            elif action == 3:
                print_header()
                view_promotions()
                time.sleep(1.25)
            elif action == 4:
                print_header()
                view_categories(current_customer_id)
                time.sleep(1.25)
            elif action == 5:
                print_header()
                view_inventory(current_customer_id, -1)
                time.sleep(1.25)
            elif action == 6:
                print_header()
                view_wishlist(current_customer_id)
                time.sleep(1.25)
            elif action == 7:
                print_header()
                view_cart(current_customer_id)
                time.sleep(1.25)
            elif action == 8:
                print_header()
                view_orders(current_customer_id)
                time.sleep(1.25)
            elif action == 9:
                print_header()
                startreturn(current_customer_id)
                time.sleep(1.25)
            elif action == 0:
                print_header()
                print("Thank you for visiting EPerfume. Come again soon!")
                logged_in = False
                current_customer_id =  -1
                time.sleep(1.25)
            else:
                print("Invalid action specified. Please choose from available actions.")

        close_connection()
    
    except Exception as e:
        # Handling the exception
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    main()
