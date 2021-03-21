str=input("enter a string to check for given string is palandrom or not=")
empty=""
for i in str:
	empty=i+empty
if empty == str:
	print("string is palandrom")
else:
	print("not palandrom")
