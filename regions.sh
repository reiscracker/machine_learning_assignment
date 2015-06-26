#!/bin/bash

echo -e "\nPossible Genders:"
cat users.csv | awk -F ',' '{print $2}' | sort | uniq        
echo -e "\nAge:"
cat users.csv | awk -F ',' '{print $3}' | sort | uniq        
echo -e "\nWorking Status:"
cat users.csv | awk -F ',' '{print $4}' | sort | uniq        
echo -e "\nRegions:"
cat users.csv | awk -F ',' '{print $5}' | sort | uniq        

