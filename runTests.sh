#!/bin/bash

for i in {01..33}
do
    input_file="test$i/test.a"
    expected_output_file="test$i/test.b"

    if [[ -f "$input_file" && -f "$expected_output_file" ]]; then
        python_output=$(python3 SimEnka.py < "$input_file")

        expected_output=$(cat "$expected_output_file")

        if [[ "$python_output" == "$expected_output" ]]; then
            echo "Test $i: PASSED"
        else
            echo "Test $i: FAILED"
        fi
    else
        echo "Test $i: Input or expected output file not found."
    fi
done
