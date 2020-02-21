
while True:	
	try:
		num=int(input("What is your phone number? Please write 9 digits using this format: 012345678:"))
		break
	except:
		print("Please don't put space between numbers:")

if str(num).startswith("91") or str(num).startswith("96") or str(num).startswith("99") or str(num).startswith("43"):
    print("Your operator is Beeline.")
elif str(num).startswith("55") or str(num).startswith("95") or str(num).startswith("45"):
    print("Your operator is Ucom.")
elif str(num).startswith("93") or str(num).startswith("94") or str(num).startswith("77") or str(num).startswith("98") or str(num).startswith("49"):
    print("Your operator is Vivacell.")
else: 
    print("Is there a new operator that I don't know?")           



