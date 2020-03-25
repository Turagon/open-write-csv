food = []
with open("note.csv", "r", encoding = "utf-8") as f :
	for item in f :
		name, price, quantity = item.strip().split(",")
		food.append([name, price, quantity])

food1 = []
while True :
	n = input("Please input name of food :")
	if n == "quit" :
		break
	p = input("Please input price of food :")
	q = input("Please input quantity of food :")
	food1.append([n, p, q])

with open("note.csv", "a", encoding = "utf-8") as f :
	for item in food1 :
		f.write(item[0] + "," + item[1] + "," + item[2] + "\n")