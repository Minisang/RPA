score = int(input("점수:"))
grade = 'F'

if(score>=90):
    grade='A'
elif (score >=80):
    grade='B'
elif (score >=79):
    grade='C'
elif (score >=60):
    grade='D'
else:
    grade='F'
    
print("학점 : "+ grade)