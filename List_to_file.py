# 3. Write a Python program to write a list to a file.


a=["weather", "hot", "cold", "mountain"]

File=open("List.txt","w+")
for word in a:
	File.write(word)
	File.write("\n")
File.close()	







# my_file = open("List.txt", "a")
# new_list = []
# num = int(input("How many items do you want to enter: "))
# for i in range(num):
# 	a = input("Write an item: ")
# 	new_list.append(a)
# my_file.writelines(new_list)
# my_file.close()