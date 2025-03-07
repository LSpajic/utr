#!/bin/bash

read -p "Enter the starting test number: " start
read -p "Enter the ending test number: " end

for ((i=start; i<=end; i++)); do
    in_file="test${i}.in"
    out_file="test${i}.out"

    tmp_output=$(mktemp)
    
    python3 UTRlab1.py < "$in_file" > "$tmp_output"
    
    echo "----------------------------------------"
    echo "Test $i:"
    if diff -wBq "$tmp_output" "$out_file" > /dev/null; then
        echo "Result: PASSED"
    else
        echo "Result: FAILED"
        echo "Differences:"
        diff -wB "$tmp_output" "$out_file"
    fi
    
    rm "$tmp_output"
done

echo "----------------------------------------"
echo "Test sequence completed ($start-$end)"