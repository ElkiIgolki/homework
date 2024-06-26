grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
a = 0
sorted_students = sorted(students)
while a < len(grades):
    avg = sum(grades[a]) / len(grades[a])
    grades[a] = avg
    a += 1
avg_dict = dict(zip(sorted_students, grades))
print(avg_dict)