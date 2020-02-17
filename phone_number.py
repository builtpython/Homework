# 2. Write a python program to ask user to input his phone number 
# ( using try except block ) and than say him which mobile operator he is using ( beeline, vivacell, ucom )


# while True:
#     try:
# 	    number = int(input("enter your phone number: "))
# 	    break
#     except:
# 	    print("Phone number should be written with numbers!")
# if str(number).startswith("93") or str(number).startswith("94") or str(number).startswith("77"):
# 	print(" You use VivaCell operatore!")
# elif str(number).startswith("55"):
# 	print("You use Ucom!")
# elif str(number).startswith("99"):
# 	print("You are Beeline user!")




while True:	
	try:
		num=int(input("What is your phone number? Please write 9 digits using this format: 012345678:"))
		break
	except:
		print("Please don't put space between numbers:")
# if len(str(num!=9)):
# 	print("number must be 8 digits")


if str(num).startswith("91") or str(num).startswith("96") or str(num).startswith("99") or str(num).startswith("43"):
    print("Your operator is Beeline.")
elif str(num).startswith("55") or str(num).startswith("95") or str(num).startswith("45"):
    print("Your operator is Ucom.")
elif str(num).startswith("93") or str(num).startswith("94") or str(num).startswith("77") or str(num).startswith("98") or str(num).startswith("49"):
    print("Your operator is Vivacell.")
else: 
    print("Is there a new operator that I don't know?")           




#   "

# try:
#     num=int(input(""What is your phone number, please don't put space between numbers:""))
#         if len(str(num)!=9)             
#             break
#         except:
#                 print(""Please use this format: 055133111"")

# if str(num).startswith(""091"") or str(num).startswith(""096"") or str(num).startswith(""099"") or  str(num).startswith(""043""):
#         print(""Your operator is Beeline."")
# elif str(num).startswith(""55"") or str(num).startswith(""095"") or str(num).startswith(""045""):
#         print(""Your operator is Ucom."")
# elif str(num).startswith(""093"") or str(num).startswith(""094"") or str(num).startswith(""077"") or str(num).startswith(""098"") or str(num).startswith(""049""):
#         print(""Your operator is Vivacell."")
# else: 
#     print (Is there a new operator that I don't know? :)




# "

# try:
#     num=int(input(""What is your phone number? Please write 9 digits using this format: 055133111:""))
#         if len(str(num)!=9):             
#             break
#         except:
#                 print(""Please don't put space between numbers"")

# if str(num).startswith(""091"") or str(num).startswith(""096"") or str(num).startswith(""099"") or  str(num).startswith(""043""):
#         print(""Your operator is Beeline."")
# elif str(num).startswith(""55"") or str(num).startswith(""095"") or str(num).startswith(""045""):
#         print(""Your operator is Ucom."")
# elif str(num).startswith(""093"") or str(num).startswith(""094"") or str(num).startswith(""077"") or str(num).startswith(""098"") or str(num).startswith(""049""):
#         print(""Your operator is Vivacell."")
# else: 
#     print (""Is there a new operator that I don't know?"")"