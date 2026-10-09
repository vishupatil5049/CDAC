DirName="Test1"
if [ -d "$DirName" ]
then
echo "Directory Exists"
else
mkdir "$DirName"
echo "Directory '$DirName' Created"
fi
for ((i=0; i<5; i++))
do
touch "$DirName/file$i.txt"
done
echo "All the files from Directory"
total=$(ls "$DirName" | wc -l)
echo "Total Files = $total"
#Run using bash q4.sh
