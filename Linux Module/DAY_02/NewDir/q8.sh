#Backup Directory
echo "Enter source directory name:"
read src
echo "Enter backup directory name:"
read backup
if [ ! -d "$backup" ]
then
mkdir "$backup"
fi
cp -r "$src"/* "$backup"/
ls -l "$backup"/*
