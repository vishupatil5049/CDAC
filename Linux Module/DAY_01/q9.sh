#File Handling
echo "Enter the file name:"
read fname
if [ -f "$fname" ]
then
echo "File Exists"
echo "File Name = $fname"
size=$(wc -c < "$fname")
echo "File Size = $size"
lines=$(wc -l < "$fname")
echo "File Lines = $lines"
words=$(wc -w < "$fname")
echo "File Words = $words"
chars=$(wc -m < "$fname")
echo "File Characters = $chars"
else
echo "File not Found"
fi 
