echo "Enter a number"
read num
if [ $num -eq 0 ]
then
echo "Number is Zero"
elif (( $num % 2 == 0))
then
echo "Number is Even"
else
echo "$num is Odd Number"
fi
#Use bash q5.sh to run
