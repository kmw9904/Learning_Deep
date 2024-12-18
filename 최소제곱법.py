import numpy as np

x = np.array([2, 4, 6, 8])
y = np.array([81, 93, 91, 97])

# 최소 제곱근 공식으로 기울기a의 값과 y 절편 b의 값을 구현
mx = np.mean(x)
my = np.mean(y)
print("x의 평균 값 :", mx) # x의 평균 값 : 5.0
print("y의 평균 값 :", my) # y의 평균 값 : 90.5

# 분모 값 = x의 각 원소와 x의 평군 값의 차를 제곱
divisor = sum([(i - mx) ** 2 for i in x])
print("분모 값 : ",divisor) # 분모 값 :  20.0

# 분자 값 = x와 y의 편차를 곱해서 합한 값
dividend = 0
for i in range(len(x)):
    dividend += (x[i] - mx) * (y[i] - my)
print("분자 값 :", dividend) # 분자 값 : 46.0

# 기울기 a의 값
a = dividend / divisor
print("기울기 a의 값 :", a) # 기울기 a의 값 : 2.3

# y절편 b의 값
b = my - (mx * a)
print("y절편 값 b :", b) # y절편 값 b : 79.0