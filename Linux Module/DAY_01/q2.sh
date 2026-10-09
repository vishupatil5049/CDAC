echo "Enter the principal amount:"
read p
echo "Enter rate of interest:"
read r
echo "Enter the time:"
read t
si=$((($p * $r * $t) / 100))
ta=$(($p + $si))
echo "Simple Interest = $si"
echo "Total Amount = $ta"
