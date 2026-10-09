cat << EOF > students.csv
Ravi, Java, 85
Priya, Python, 92
Kiran, Java, 76
Anita, Python, 88
Rahul, Java, 95
EOF

cat students.csv
echo "Students Scoring 80 and Above:"
grep -E ", (8[0-9]|9[0-9])$" students.csv
