#!/bin/bash

echo "Possible Genders:"
cat users.csv | awk -F ',' '{print $2}' | sort | uniq        
echo "Working status:"
cat users.csv | awk -F ',' '{print $3}' | sort | uniq        
echo "Regions:"
cat users.csv | awk -F ',' '{print $4}' | sort | uniq        

