#!/bin/bash

RED='\033[0;31m'
GREEN='\033[0;32m' 
NC='\033[0m'
declare -i n=0

for i in {01..25}
do
    input_file="tests/test$i/primjer.in"
    expected_output_file="tests/test$i/primjer.out"

    if [[ -f "$input_file" && -f "$expected_output_file" ]]; then
        python_output=$(python3 SimPa.py < "$input_file")

        expected_output=$(cat "$expected_output_file")

        if [[ "$python_output" == "$expected_output" ]]; then
            echo -e "Test $i: ${GREEN}PASSED${NC}"
            n=$n+1
        else
            echo -e "Test $i: ${RED}FAILED${NC}"
            echo "Expected output:"
            echo "$expected_output"
            echo "Your output:"
            echo "$python_output"
        fi
    else
        echo "Test $i: Input or expected output file not found."
    fi
done
echo "Passed $n/25 tests!"
