#!/usr/bin/env python3
students = [{"name": "Steve", "score": 88}, {"name": "Becky", "score": 99}, {"name": "Chad", "score": 76}]

# And print out each of the students' names, scores, and grade they would receive (90-100 A, 80-90 B, etc)
# "Steve got a(n) 88, so this student received a(n) B"

for item in students:
    if item['score']>=90:
        print(f"{item['name']} got a(n) {item['score']}, so this student received a(n) A")
    elif 80 <= item['score'] <= 90:
        print(f"{item['name']} got a(n) {item['score']}, so this student received a(n) B")
    else:
        print(f"{item['name']} got a(n) {item['score']}, so this student received a(n) C")

