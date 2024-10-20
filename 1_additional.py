
grades = [
    [5, 3, 3, 5, 4],
    [2, 2, 2, 3],
    [4, 5, 5, 2],
    [4, 4, 3],
    [5, 5, 5, 4, 5]
]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

# 1
print ( dict(
    zip(sorted(students),
    map(lambda stud_grades: sum(stud_grades)/len(stud_grades),grades)))
)

#2
stud_list = list(students)
#stud_list = list(students).sort()  -->None надо разобраться!
stud_list.sort()
averages = [sum(arr)/len(arr) for arr in grades ]
average_score_dict = dict(zip(stud_list,averages))

print(average_score_dict)

# 3
average_score_dict ={}
i=0
for stud in sorted(students):
    average_score_dict[stud] = sum(grades[i])/len(grades[i])
    i+=1
print(average_score_dict)

# как обойтись методами списков/словарей я пока не придумал









