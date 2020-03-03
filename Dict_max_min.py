# 5. Write a Python program to get the maximum and minimum value in a dictionary.



Family = {"John":90, "Jerry":70, "Anna": 55, "David": 25} 
Oldest = max(Family, key=Family.get)
Youngest = min(Family, key=Family.get)   
print("Oldest: ", Oldest, ", Youngest: ", Youngest) 