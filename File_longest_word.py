File=open("longest.txt","r")
for line in File:
	word=line.split(" ")
	longest=max(word)
	print("Longest word:", longest)
