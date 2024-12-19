
# 조건문 (if문 사용)
# if : 만약에 ~라면

# 조건에 따라 다른 명령을 내릴때 사용

# 조건이 참(True)이면 실행, 거짓(False)이면 실행하지마

# 비교연산자
a = 10
b = 3

# a와 b가 서로 같습니까?
print(a == b)

# 실행순서
# print(a == b)
# print(10 == b)
# print(10 == 3)
# print(False)

# a와 b가 서로 다릅니까?
print(a != b)

# a가 b보다 큽니까?
a = 20
b = 10
print(a > b)

# a가 b 이상입니까? (같거나 큽니까?)
print(a >= b)

# b가 a보다 큽니까?
print(b > a)
# a가 b보다 작습니까?
print(a < b)

# a가 b 이하입니까?  (<=, >=, !=) 등호는 항상 오른쪽
print(a <= b)


# 주민번호 뒷자리의 첫번째 숫자가
# 짝수면 여자, 홀수면 남자
# 1, 2, 3, 4, 5, 6, 7, 8, 9, 0
# 1900 년도에 태어난 남자 1, 여자 2
# 2000 년도에 태어난 남자 3, 여자 4
# 1900 년도에 태어난 외국인 남자 5, 여자 6
# 2000 년도에 태어난 외국인 남자 7, 여자 8

idNum = "1234567"

# idNum 의 첫번째 숫자가 홀수면 남성 출력, 짝수면 여성 출력
print(idNum[0])

fst = idNum[0]
# fst의 타입? 문자열
print(type(fst))  # "1"

# 파이썬은 배열에 곱하기를 하면 내용이 그 수만큼 늘어남
print(fst * 3)

# 홀수, 짝수 계산을 위해 fst를 int 로 변환해야함
fst = int(fst)

# 홀수, 짝수 계산하기
# 어떤 수든 2로 나누었을때 나머지가 0이면 짝수, 1이면 홀수
print(fst % 2 == 0)

# 실행순서
# print(fst % 2 == 0)
# print(1 % 2 == 0)
# print(1 == 0)
# print(False)

print(fst % 2 == 1)


# 짝수일때는 여성, 홀수일때는 남성 출력
fst = 4
# if문의 조건이 True일 때만 if문 내부 코드가 실행 됨
if fst % 2 == 0:
    print("여성")  # 탭이 있기에 if 내부 코드가 됨
print("성별체크")  # 탭이 없기에 if문과 무관한 코드

# fst가 홀수일 때는 남성이 출력되도록 if문 작성
if fst % 2 == 1:
    print("남성")


# 두 개의 if문을 하나로 묶기
if fst % 2 == 0:
    print("여성")
elif fst % 2 == 1:  # 위 if문이 False면 추가적인 조건 체크
    print("남성")


# 짝수 체크를 해서 True면 짝수이고, False면 fst가 홀수라는 뜻
fst = 3
if fst % 2 == 0:
    print("여성")
else:  # 위 if문이 False면 조건 체크없이 실행
    print("남성")


# fst가 1~4면 한국인
# fst가 5~8이면 외국인
# 1 <= fst <= 4
fst = 3
print(1 <= fst <= 4)
print(5 <= fst <= 8)  # boolean 값 (조건)

# fst 에 대해 1~4면 한국인, 5~8이면 외국인 출력하기
if 1 <= fst <= 4:
    print("한국인")
else:
    print("외국인")


# 성적이 90점 이상이면 A등급 출력
# 성적이 80점대면 B등급 출력
# 성적이 70점대면 C등급 출력
# 그 외 나머지는 D등급 출력

score = 85

# score가 90점 이상 인지 확인
print(score >= 90)
# score가 80점대인지 확인
print(80 <= score < 90)

if score >= 90:
    print("A등급")
elif 80 <= score < 90:
    print("B등급")
elif 70 <= score < 80:
    print("C등급")
else:
    print("D등급")

# if문의 실행 순서를 잘 고려한다면
score = 85
if score >= 90:
    print("A등급")
elif 80 <= score:   # 이 타이밍에 score < 90 인 상황
    print("B등급")
elif 70 <= score:   # 이 타이밍에 score < 80 인 상황
    print("C등급")
else:
    print("D등급")

score = 95
if score >= 70:
    print("C등급")
elif score >= 80:
    print("B등급")
elif score >= 90:
    print("A등급")
else:
    print("D등급")









