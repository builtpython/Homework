# 3. Write a Python class to reverse a string word by word.	
# Input string : ‘hello .py’
# Expected Output : ‘.py hello’




class reverse_string:
	def reverse_words(self, string):
		words=string.split(" ")
		output=' '.join(reversed(words))
		return output

print(reverse_string().reverse_words("hello .py")) 	