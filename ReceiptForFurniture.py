#This is based off the project Receipts For Lovely Loveseats from codecademy

#Descriptions and prices for the furniture

lovely_loveseat_description = "Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white."
lovely_loveseat_price = 254.00


stylish_settee_description = "Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black."
stylish_settee_price = 180.50

luxurious_lamp_description = "Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade."
luxurious_lamp_price = 51.15

#Sales tax
sales_tax = .088

#Customer one
customer_one_total = 254.00 + 51.15
customer_one_itemization = """
Lovely Loveseat: Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white.

Luxurious Lamp: Glass and iron. 36 inches tall. Brown with cream shade.
"""
customer_one_tax = customer_one_total + sales_tax

print("Customer One Items:", customer_one_itemization)
print("Custoner One Total:", customer_one_tax)

