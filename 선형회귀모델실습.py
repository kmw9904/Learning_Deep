import numpy as np
import matplotlib.pyplot as plt

# 공부 시간 X와 성적 y의 넘파이 배열을 만들기
x = np.array([2, 4, 6, 8])
y = np.array([81, 93, 91, 97])

# 데이터의 분포를 그래프로 표현
plt.scatter(x, y)
plt.show()

# 기울기 a의 값과 절편 b의 값을 초기화
a = 0
b = 0

# 학습률을 정함 (학습률은 그때그때 찾아야함)
lr = 0.03

# 몇 번 반복될지 설정
epochs = 2001

# x 값이 총 몇 개인지 카운트
n = len(x)

# 경사 하강법을 시작
for i in range(epochs):     # 에포크 수만큼 반복
    y_pred = a * x + b      # 예측 값을 구하는 식
    error = y - y_pred      # 실제 값과 비교한 오차를 error 두기

    a_diff = (2/n) * sum(-x * (error))      # 오차 함수를 a로 편미분한 값
    b_diff = (2/n) * sum(-(error))          # 오차 함수를 b로 편미분한 값
    
    a = a - lr * a_diff     # 학습률을 곱해 기존의 a 값을 업데이트
    b = b - lr * b_diff     # 학습률을 곱해 기존의 b 값을 업데이트

    if i % 100 == 0:         # 100번 반복될 때마다 현재의 a 값, b 값을 출력
        print("epoch+%.f, 기울기=%0.4f, 절편=%0.4f" % (i, a, b))

# 앞서 구한 최종 a 값을 기울기, b 값을 y 절편에 대입해 그래프를 그림
y_pred = a * x + b

# 그래프 출력
plt.scatter(x, y)
plt.plot(x, y_pred,'r')
plt.show()