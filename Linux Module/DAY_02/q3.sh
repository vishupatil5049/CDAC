# Directory Functions
echo "Enter the directory name:"
read dir
if [ -d "$dir" ]
then
echo "Directory Already Exists"
ls -la "$dir"
else
echo "Directory Not Found. Creating One.."
mkdir "$dir"
fi
