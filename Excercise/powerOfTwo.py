no = int(input("enter a number ="))
for i in range (1,11):
    print("table",(i*no)," power of 2 =" ,((i*no)*2))
    sum=+ ((i * no) * 2)
    if (sum<256):
        pass
    else:
        print("you have reached to more then 256", (sum))
        break
