#File Copy
echo "Enter the source file:"
read sname
echo "Enter the destination file:"
read dname
if [ -f "$sname" ]
then
echo "File Exists"
cp "$sname" "$dname"
echo "File copied Successfully"
echo "Copied Content"
cat "$dname"
else
echo "File not Found"
fi
