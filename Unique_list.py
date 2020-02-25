


def unique(list):
	newlist=[]

	for i in mylist:
		if i not in newlist:

			newlist.append(i)
			
	return newlist
			
mylist=[1,5,10,5,7,10,"hall","game","hall"]
print(unique(list))


