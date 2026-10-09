DirName="Test1"
if [ -d "$DirName" ]
then
echo "Directory Exists"
else
mkdir "$DirName"
echo "Directory '$DirName' Created"
for ((i=0; i<5; i++))
do
touch "$DirName/file$i.txt"
done
echo "All the files from Directory"
total=$(ls "$DirName" | wc -l)
echo "Total Files = $total"
fi
#Run using bash q4.sh
