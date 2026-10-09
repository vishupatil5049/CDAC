cat << EOF > students.csv
Ravi, Java, 85
Priya, Python, 92
Kiran, Java, 76
Anita, Python, 88
Rahul, Java, 95
EOF

cat students.csv
echo "Courses And Counts:"
cut -d',' -f2 students.csv | sort | uniq -c
