
string="The lyrics is not that poor!"

word = string.find("not")
poor = string.find("poor")

if word<poor:
	new_string=string.replace(string[word:poor+4], "good")

print (new_string)

