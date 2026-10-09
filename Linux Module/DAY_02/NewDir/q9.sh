echo "Enter directory path:"
read dir
mkdir -p report
files=$(find "$dir" -maxdepth 1 -type f | wc -l)
dirs=$(find "$dir" -maxdepth 1 -type d ! -path "$dir" | wc -l)
lines=$(find "$dir" -maxdepth 1 -type f -exec cat {} + | wc -l)
echo "Files = $files" > report/summary.txt
echo "Directories = $dirs" >> report/summary.txt
echo "Lines = $lines" >> report/summary.txt

