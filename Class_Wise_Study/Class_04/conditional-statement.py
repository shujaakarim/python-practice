#conditional statement class 29/10/2026

#2. Grades. Given marks, print A for 80 and above, B for 65–79, C 
#for 50–64 and Fail below 50. Test with exactly 80, 79, 50 and 49. 
#Boundary values are where bugs hide.
""""
marks = 39
if marks >= 80:
    print("A")
elif marks >=65 and marks >=79:
    print("B")
elif marks >=50 and marks >=64:
    print("B")
else:
    print("Fail")
"""

""""
3. Stock check. Given stock = 12 and quantity, print:
Invalid quantity if the quantity is 0 or less
Only 12 left in stock if the quantity is more than the stock
Confirmed. 7 left after this order otherwise (here, for a quantity of 5)
Work out every number in the message from the variables.
"""

""""
given_stock = 12
quantity = 5
if quantity <=0:
    print("Invalid quality")
elif quantity > given_stock:
    print("Only ",given_stock," left in the stock")
else:
    remaining_stock = given_stock - quantity
    print(remaining_stock,":","left in the stock")
"""
"""
4. Shipping rules. Given weight_kg, order_total and city, work out the shipping charge:
Orders over Rs 10,000 ship free anywhere.
Karachi, Lahore and Islamabad: Rs 200 up to 5 kg, Rs 400 above that.
Every other city: Rs 350 up to 5 kg, Rs 700 above that.
Customers type the city themselves, so clean city first: " karachi " must count as Karachi. 
Print Shipping to Karachi: Rs 200. Test at least five combinations, including exactly 5 kg.
"""
order_limit = 10000
city_1 = "Karachi"
city_2 = "Lahore"
city_3 = "Islamabad"
wait_lim = "5kg"
wait_lim = int(wait_lim)
higher_wait = 400
other_city_5kg = 350
higher_wiat = 700

user_city = input("please enter your city for the shipping!")
user_shipping_waight = int(input("Please enter the shipping waight"))
if user_shipping_waight > order_limit and user_city == city_1 or city_2 or city_3:
     print("your shipping is free you exceeds the given limit", "make sure your are shipping to ", user_city)




