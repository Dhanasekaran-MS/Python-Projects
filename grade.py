students_mark={
  "Dhana":90,
  "Yogesh":92,
  "kutty":95,
  "Thuppan":45,
  "komali":30,
  "kirukku":25,
}
print(students_mark)
students_grade={}

for student in students_mark:
  score=students_mark[student]
  if score>=90:
    students_grade[student]="OUTSTANDING"
    
  elif score>80:
    students_grade[student]="GOOD"
    
  elif score>70:
    students_grade[student]="ACCEPTABLE"
    
  else:
    students_grade[student]="FAIL"

print(students_grade)
