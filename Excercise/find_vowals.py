str=input("enter a string to check for vowals in it=")
vowals="aeiouAEIOU"
count=0
for i in vowals:
	for j in str:
		if i==j:
			count+=1

print("number of vowals in string=",count)
