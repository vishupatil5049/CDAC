# File Handling
echo "Enter the file name:"
read fname
if [ -f "$fname" ]
then
echo "File Exists"
echo "File Name = $fname"
size=$(wc -c < "$fname")
echo "File Size = $size"
lines=$(wc -l < "$fname")
echo "Number of lines = $lines"
words=$(wc -w < "$fname")
echo "Number of words = $words"
chars=$(wc -m < "$fname")
echo "Number of characters = $chars"
else
echo "File Does not Exist"
fi
