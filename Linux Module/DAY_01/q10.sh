echo "Enter Directory:"
read dir
echo "Enter File Extenstion without '.'"
read ext
find "$dir" -type f -name "*.$ext"
total=$(find "$dir" -type f -name "*.$ext" | wc -l)
echo "Total .$ext Files = $total"
