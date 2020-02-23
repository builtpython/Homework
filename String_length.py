# "1. Write a Python program to count the number of strings where the string length is 
# 2 or more and the first and last character are same from a given list of strings. Go to the editor
# Sample List : [‘abc’, ‘xyz’, ‘aba’, ‘1221’]
# Expected Result : 2"


# "Գրիր ծրագիր, որը տրված սթրինգների  ցանկից կհաշվի այն սթրինգերի քանակը, որոնց երկարությունը 
# 2 կամ ավելի է և որոնց առաջին և վերջին սիմվոլները նույնն են: Գնալ editor
# Օրինակ լիսթ՝ [‘abc’, ‘xyz’, ‘aba’, ‘1221’]
# Ակնկալվող արդյունք՝ 2 "




list=['abc', 'xyz', 'aba', '1221', '1991']

count=0
for i in list:
	if len(i)>2 and i[0]==i[-1]:
		count+=1
print("There are", count, "such strings")

