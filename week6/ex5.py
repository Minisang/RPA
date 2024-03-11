hobby = {'바둑':10, '독서':8,'영화감상':7}

print(hobby)
hobby['영화감상'] = "100명"
print(hobby)
hobby['등산']  =20
hobby['여행'] = 30
print(hobby)

print("hobby.keys()의 출력결과 : ", hobby.keys())
print("딕셔너리 hobby 키 리스트 : ", list(hobby.keys()))
print("hobby.values()의 출력결과 :", list(hobby.values()))
print("hobby.items()의 출력결과 : ", list(hobby.items()))