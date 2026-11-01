#Delivery charges question
#1. Delivery charge. A customer, "Karachi Crafts", orders 3 lamps at Rs 2,400 each.
#Delivery costs Rs 350. Store each value in a variable, then print the order total including delivery. 
#Finally, print the type of your total.

Customer = "Karachi crafts"
Lamp_ordered = 3
Lamp_ord_price = 2400
delivery_cost = 350
total_charges = Lamp_ord_price + delivery_cost
print(total_charges)
print(type(total_charges))

#2. Sales tax. An order's subtotal is Rs 7,200 and sales tax is 18%. 
#Print the tax amount and the total with tax (expected: 1296.0 and 8496.0). 
#rint the type of the tax amount. Why is it a float when the subtotal was an int?

total_order = 7200
sales_tax = "18%"
tex_amount = 18/100*7200
print(tex_amount)
total_with_tax = tex_amount + total_order
print(total_with_tax)
print(type(total_with_tax))


#3. Splitting a bill. Four friends split a Rs 4,750 dinner. 
#Print each person's share using /. Then look up the // and % operators and use them to 
#print how many whole rupees each person pays and how many rupees are left over.

total_bill = 4750




#4. Discount and tax. A phone costs Rs 15,000. Apply a 10% discount, then add 18% tax to the discounted price, 
#and print the final price. Now do it the other way round: tax first, then the discount. Do you get the same answer? 
#Write a comment in your code explaining why or why not.

phone_cost = 15000
applied_discount = 10/100*15000
added_tax = (18/100*applied_discount)
final_price = (phone_cost - applied_discount) + added_tax

phone_cost = 15000
added_tax = (18/100*applied_discount)
applied_discount = 10/100*15000
final_price = (phone_cost - applied_discount) + added_tax


#5. Packing boxes. A shop is shipping 23 items, and each box holds 6. Using only arithmetic (no if), 
#print the number of full boxes, the number of items left over, and the total number of boxes needed, 
#including a partly full one (expected: 3, 5 and 4). Each box costs Rs 120 to ship: print the shipping cost. 
#Test your code with 24 items. Does the box count still come out right?

shipping_items = 23
each_box_hold = 6



