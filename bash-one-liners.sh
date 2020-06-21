#Rename list of files with sed + regex
for f in *.jpg; do mv $f $(echo "$f" | sed 's/b-//'); done
