food = []
while True :
	n = input("Please input name of food :")
	if n == "quit" :
		break
	p = input("Please input price of food :")
	q = input("Please input quantity of food :")
	food.append([n, p, q])

with open("note.csv", "w", encoding = "utf-8") as f :
	f.write("Name,Price,Quantity\n")
	for item in food :
		f.write(item[0] + "," + item[1] + "," + item[2] + "\n")