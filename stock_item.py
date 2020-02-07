user_items_number=int(input("Input the number of items you want to buy:"))
user_prefered_items=[]
market_stock=["Ice-Cream","Juice","Apple"]
user_avaliable_items=[]

for i in range(user_items_number):
	item=input("Enter item name you want to buy:")
	user_prefered_items.append(item)

for item in user_prefered_items:
	if item in market_stock:
		user_avaliable_items.append(item)
print(user_avaliable_items)