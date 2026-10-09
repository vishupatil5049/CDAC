echo "Enter the name of Student:"
read name
echo "Enter the age of Student:"
read age
echo "Enter the marks of each subject"
echo "Enter marks of Maths:"
read maths
echo "Enter marks of English:"
read english
echo "Enter marks of History:"
read history
total=$((maths + english + history))
avg=$((total / 3))
echo "Name = $name"
echo "Age = $age"
echo "Maths = $maths, English = $english, History = $history"
echo "Total = $total"
echo "Average = $avg"
