

File=open("List.txt","r")
File1=open("list5.txt","w+")
for line in File:
	File1.write(line)
File.close()
File1.close()