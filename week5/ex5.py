name = input("이름 : ")
a = int(input("영어 성적 : "))
b = int(input("수학 성적 : "))
c=a+b
print("총점은 : ",c)
c= c/2
print("평균은 : ",c)
score=c
grade='F'
if(score>=90):
    grade='A'
elif(score>=80):
    grade='B'
elif(score>=70):
    grade='C'
elif(score>=60):
    grade='D'
else:
    grade='F'
print("학점 : "+ grade)