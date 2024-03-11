def ss(list,t): #6
    global n
    print("score=",list)
    print("총점 : %d" % (t))
    print("평균 : %d" % (t/n))
    
score =[] #1
n = int(input("학생 수 : ")) #2
total = 0 #3
for i in range(0,n): #4
    jumsu = int(input("[%d] 영어시험 성적 : " % (i+1)))
    total +=jumsu
    score.append(jumsu)
ss(score,total) #5