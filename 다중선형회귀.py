import numpy as np
import matplotlib.pyplot as plt

# 공부 시간 x1과 과외 시간 x2, 성적 y의 넘파이 배열을 만듦듦
x1 = np.array([2,4,6,8])
x2 = np.array([0,4,2,3])
y = np.array([81, 93, 91, 97])

# 데이터의 분포를 그래프로 표현
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter3D(x1, x2 ,y)
plt.show()

# 기울기 a의 값과 절편 b의 값을 초기화
a1 = 0
a2 = 0
b = 0

# 학습률을 정함
lr = 0.01

# 몇 번 반복될지 설정
epochs = 2001

# x 값이 총 몇 개인지 카운트트
n = len(x1)                            

# 경사 하강법을 시작
for i in range(epochs):     # 에포크 수만큼 반복복
    y_pred = a1 * x1 + a2 * x2 + b      # 기울기와 절편 자리에 a1, a2, b를 각각 대입
    error = y - y_pred                  # 실제 값과 비교한 오차를 error로 놓음

    a1_diff = (2/n) * sum(-x1 * (error))    # 오차 함수를 a1로 편미분한 값
    a2_diff = (2/n) * sum(-x2 * (error))    # 오차 함수를 a2로 편미분한 값
    b_diff = (2/n) * sum(-(error))          # 오차 함수를 b로 편미분한 값

    a1 = a1 - lr * a1_diff  # 학습률을 곱해 기존의 a1 값을 업데이트
    a2 = a2 - lr * a2_diff  # 학습률을 곱해 기존의 a2 값을 업데이트
    b = b - lr * b_diff     # 학습률을 곱해 기존의 b 값을 업데이트

    if i % 100 == 0:        # 100번 반복될 때마다 현재의 a1, a2, b의 값을 출력
        print("epoch=%.f, 기울기1=%0.4f, 기울기2=%0.4f, 절편=%0.4f" % (i, a1, a2, b))

# 실제 점수와 예측된 점수를 출력
print('실제 점수 :', y)
print('예측 점수 :', y_pred)
