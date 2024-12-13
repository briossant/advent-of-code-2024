#!/bin/sh

REG="mul\(([0-9]{1,3}),([0-9]{1,3})\)|(do\(\))|(don't\(\))"

grep -o -E $REG input.txt | sed -E "s/$REG/\3\4\1 \2/g" > input-treated.txt

python ./multiply.py
