#Directory and extention
echo "Enter the name of Directory:"
read dir
echo "Enter the file extention without '.'"
read ext
find "$dir" -type d
find "$dir" -type f -name "*.$ext"
total=$(find "$dir" -type f -name "*.$ext" | wc -l)
echo "Total .$ext files = $total"
