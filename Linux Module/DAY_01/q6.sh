# Grade Calculation
echo "Enter the Marks"
read mark
if [ $mark -lt 0 ] || [ $mark -gt 100 ]
then
echo "Enter valid marks"
elif [ $mark -ge 90 ]
then
echo "Grade A"
elif [ $mark -ge 75 ]
then
echo "Grade B"
elif [ $mark -ge 60 ]
then
echo "Grade C"
elif [ $mark -ge 50 ]
then
echo "Grade D"
else
echo "Fail"
fi
