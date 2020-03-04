
mystring = "ISTC"      
mydict = {}       
for keys in mystring:       
        mydict[keys] = mydict.get(keys, 0) + 1        
print (mydict)