"""
https://www.hackerrank.com/challenges/nested-list/problem
Given the names and grades for each student in a Physics class of N students,
 store them in a nested list and print the name(s) of any student(s)
  having the second lowest grade.

Note: If there are multiple students with the same grade,
order their names alphabetically and print each name on a new line.

Input Format

The first line contains an integer,N , the number of students.
The 2N  subsequent lines describe each student over 2 lines;
 the first line contains a student's name,
  and the second line contains their grade.

Constraints

There will always be one or more students having the second lowest grade.

Output Format
Print the name(s) of any student(s) having the second
lowest grade in Physics; if there are multiple students,
order their names alphabetically and print each one on a new line.
"""
students = []
scores = []  # list only for scores
min_score = 100  # min score
second_score = 0  # second min score
i = 0  # counter
names = []  # list for final results
for _ in range(int(raw_input())):
    name = raw_input()
    score = float(raw_input())
    min_score = score if min_score > score else min_score
    student_score = [name, score]
    scores.append(score)
    students.append(student_score)

# sort scores from min to max
scores.sort()
while i in range(len(scores)):
    if min_score < scores[i]:
        second_score = scores[i]
        break
    else:
        i += 1

# find names
for i in range(len(students)):
    score = students[i][1]
    if second_score == score:
        names.append(students[i][0])

names = sorted(names)
for i in range(len(names)):
    print names[i]
