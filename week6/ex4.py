score = [88,54,76,65,84,76,92,100,92,85]
print(score, end="\n\n")

score[2] = 35
print("score[2]=",score[2])
score[3:5] = [45,55,65]
print("score[3:5]=",score[3:5])
score[6:7] = [75,85,88]
print("score=",score,end="\n\n")

score=[]
n = int(input("학생 수: "))
for i in range(0,n):
    jumsu = int(input("[%d]시험 성적: " % i))
    score.append(jumsu)
print("score=", score, end="\n\n")
