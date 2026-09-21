marks = [78, 85, 62, 91, 45, 73]
count = 0
for mark in marks:
    count = count + 1
print(count)
print("Number of students are",count)
highest_marks = marks[0]
lowest_marks =marks[0]
total_sum = 0
for mark in marks:
    if mark > highest_marks:
        highest_marks = mark
    if mark < lowest_marks:
        lowest_marks = mark
    total_sum +=mark
average = total_sum/len(marks)
print(average)
print(highest_marks)
print(lowest_marks)