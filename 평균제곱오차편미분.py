y_pred = a * x + b  # 예측 값을 구하는 식
error = y - y_pred  # 실제 값과 비교한 오챠를 error로 놓습니다.
a_diff = (2/n) * sum(-x * (error))  # 오차 함수를 a로 편미분한 값
b_diff = (2/n) * sum(-(error))  # 오차 함수를 b로 편미분한 값

# 여기에 학습률을 곱해 기존의 a 값과 b 값을 업데이트 합니다.

lr = 0.03
a = a - lr * a_diff
b = b - lr * b_diff