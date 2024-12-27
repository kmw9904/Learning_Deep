import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

x = np.array([2, 4, 6, 8, 10, 12, 14])
y = np.array([0, 0, 0, 1, 1, 1, 1])

model = Sequential()
model.add(Dense(1, input_dim=1, activation='sigmoid'))

# 교차 엔트로피 오차 함수를 이용하기 위해 'binary_crossentropy'로 설정
model.compile(optimizer='sgd', loss='binary_crossentropy')
model.fit(x, y, epochs=10)

# 그래프로 확인
plt.scatter(x, y)
plt.plot(x, model.predict(x), 'r')
plt.show()

# 임의의 학습 시간을 집어넣어 합격 예상 확률을 예측
# 임의의 학습 시간 예측
hour = 7
input_data = np.array([[hour]], dtype=np.float32)  # 데이터 타입을 float32로 변환
prediction = model.predict(input_data)  # 올바른 입력 형식
print("%.f시간을 공부할 경우, 합격 예상 확률은 %0.1f%%입니다." % (hour, prediction[0][0] * 100))