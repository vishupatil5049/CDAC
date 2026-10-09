#Reverse Number and Add
echo "Enter the number:"
read num
sum=0
re=""
while [ $num -gt 0 ]
do
digit=$((num % 10))
sum=$((sum + digit))
num=$((num / 10))
re=${re}${digit}
done
echo "$re"
echo "Sum = $sum"
