echo "Enter the unit"
read unit
if [ $unit -le 0 ]
then
echo "Enter the valid Unit"
elif [ $unit -le 100 ]
then
bill=$((unit * 2))
elif [ $unit -le 200 ]
then
bill=$(( (100 * 2) + ((unit - 100) * 3) ))
elif [ $unit -le 300 ]
then
bill=$(( (100 * 2) + (100 * 3) + ((unit - 200) * 5) ))
else
bill=$(( (100 * 2) + (100 * 3) + (100 * 5) + ((unit - 300) * 7) ))
fi
echo "Bill is $bill"
