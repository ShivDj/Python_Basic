#Read a Number and Display the week day (Sunday, Monday,...)
read -p "enter week days between 1 to 7"choice

case  $choice in 

1) 
   echo "monday"
;;
2)
   echo "tuesday"
;;
3) 
   echo "wednesday"
;;
4)
   echo "thushday"
;;
5)
   echo "friday"
;;
6)
   echo "saturday"
;;
7) 
   echo "sunday"
;;
esac
