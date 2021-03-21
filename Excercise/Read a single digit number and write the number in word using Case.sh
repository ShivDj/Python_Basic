#Read a single digit number and write the number in word using Case

read -p "Enter your name : " choice

case $choice in  

1)
    echo "unit"  
;;
10)
    echo "ten"
;;
100)
    echo "hundred"
;;   
1000)
    echo "thousand"
;;
esac
