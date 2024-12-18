import numpy as np

x = np.array([2, 4, 6, 8])
y = np.array([81, 93, 91, 97]) 

# 임의로 정한 기울기 fake_a 임의로 정한 절편 fake_b
fake_a = 3
fake_b = 76

# 함수식 predict
def predict(x):
    return fake_a * x + fake_b

# 위 코드의 결과값이 들어갈 빈 리스트
predict_result = []

# 모든 x 값을 predict() 함수에 한 번씩 대입해 예측 값 리스트를 채우기
for i in range(len(x)):
    predict_result.append(predict(x[i]))
    print("공부시간=%.f, 실제점수=%.f, 예측점수=%.f" % (x[i], y[i], predict(x[i])))

# 평균 제곱 오차 공식을 그대로 각 y 값에 대입해 최종 값을 구하는 함수
n = len(x)
def mse(y, y_pred):
    return (1/n) * sum((y - y_pred) ** 2)

# 평균 제곱 오차 값을 출력
print("평균 제곱 오차: " + str(mse(y, predict_result)))