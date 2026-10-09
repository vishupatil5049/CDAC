#Directory Files
echo "Enter the directory name:"
read dname
mkdir "$dname"
echo "Enter first file name:"
read file1
echo "Enter second file name:"
read file2
echo "Enter third file name:"
read file3
touch "$dname/$file1" "$dname/$file2" "$dname/$file3"
ls -la "$dname"
