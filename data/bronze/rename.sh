#!/usr/bin

# Rename the file to the current date and time
for file in c9c0505d-de23-47a5-aa33-e62687113f7f2020329-1-12a9t69.a1eg.*; do
    mv "$file" "california.${file##*.}"
done