my_list = ["Waw, this a fantastic product ! I really like it ", "Hum this is not what I had in mind but it is kinda good"," it is bad"]
for i in range(len(my_list)):
    my_list[i] = my_list[i].lower()

my_list = list(my_list.strip())

# for i in range(len(my_list)):
# 	if " it " in (my_list[i]):
# 		my_list[i].remove(" it ")
# 		#print(my_list[i].index(" it "))
# 		print(my_list)
