# function 함수
# method 메소드

# 코드 기능을 하나로 묶어서 사용
# 중복 코드를 하나로 묶어서 사용하는데 주로 이용

# 사용자의 나이에 대해 연령대로 변환하기
ageA = 38

# 중복코드는 나중에 수정할때 전부 고쳐야 되므로 귀찮음
# 28 -> 28 / 10 -> 2.8 -> int(2.8) -> 2 -> 2 * 10 -> 20
# 25 -> 25 / 10 -> 2.5 -> int(2.5) -> 2 -> 2 * 10 -> 20
a = ageA / 10
b = int(a)
c = b * 10
d = str(c) + "대"
print(d)

ageB = 23
a = ageB / 10
b = int(a)
c = b * 10
d = str(c) + "대"
print(d)

ageC = 14
a = ageC / 10
b = int(a)
c = b * 10
print(c)

ageD = 34
a = ageD / 10
b = int(a)
c = b * 10
d = str(c) + "gen"
print(d)

ageE = 45
a = ageE / 10
b = int(a)
c = b * 10
d = str(c) + "대"
print(d)



# 함수 정의하기
# 함수 실행시 값을 넘겨받을때, 값을 저장할 변수(파라미터)를 소괄호 안에 기입
def calGen(age):
    a = age / 10
    b = int(a)
    c = b * 10
    d = str(c) + "대"
    print(d)
    # 함수 실행 결과를 리턴(return)하고 있지 않음
    # 계산한 결과 d를 리턴
    return d

# 정의한 함수 실행
# 함수에 값을 넘겨주기
calGen(35)  # age에 35가 담김. age = 35

calGen(24)
calGen(16)

# 나이를 연령대로 변환한 값을 저장
gen = calGen(16)
print(gen) # None


# 1부터 10까지 다 더한값 출력
sum = 0
for i in range(1, 11):
    sum += i
print(sum)

# 20부터 40까지 다 더한값 출력
sum = 0
for i in range(20, 41):
    sum += i
print(sum)

# 35부터 45까지 다 더한값 출력
sum = 0
for i in range(35, 46):
    sum += i
print(sum)

# 46부터 51까지 다 더한값 출력
sum = 0
for i in range(46, 52):
    sum += i
print(sum)

# a부터 b까지 다 더한값 출력하는 함수 정의
def calSum(a, b):
    sum = 0
    for i in range(a, b+1):
        sum += i
    print(sum)
    return sum

# 1부터 10까지
calSum(1, 10)

# 5부터 15까지
sum = calSum(5, 15)
print(sum)


numArray = [3, 6, 9, 12, 15, 18]

# numArray의 평균값을 계산 후 출력
# 배열 안에 있는 값들을 모두 더하고 5로 나눠야징

# 배열 안에 있는 값들을 모두 더하기
sum = 0
for i in numArray:
    sum += i
mean = sum / len(numArray)
print(mean)


intArray = [5, 10, 15, 20, 25]

# intArray 의 평균값 계산 출력
sum = 0
for i in intArray:
    sum += i
mean = sum / len(intArray)
print(mean)


# 어떤 숫자 배열에 대해 평균값을 계산해서 리턴해주는 함수 정의
def calMean(arr):
    sum = 0
    for i in arr:
        sum += i
    mean = sum / len(arr)
    print(mean)
    return mean


numbers = [1, 3, 5, 7, 9]
calMean(numbers)

calMean(numArray)

calMean(intArray)











