from sklearn.datasets import load_iris
import pandas as pd
import plotly.express as px  # 3D 시각화를 위한 라이브러리
from sklearn import svm

# 1. 데이터 불러오기
iris = load_iris()

# 2. 판다스(pd)를 사용하여 데이터프레임(표) 생성 💡 (px.DataFrame을 pd.DataFrame으로 수정)
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)

# 그래프 구분을 위해 정답(품종 이름) 데이터도 표에 추가해줍니다.
df['species'] = [iris.target_names[t] for t in iris.target]

# 3. 머신러닝 모델 학습 (기존 코드)
s = svm.SVC(gamma=0.1, C=10)
s.fit(iris.data, iris.target)

# 새로운 샘플 예측 (기존 코드)
new_d = [[6.4, 3.2, 6.0, 2.5], [7.1, 3.1, 4.7, 1.35]] 
res = s.predict(new_d)
print("새로운 2개 샘플의 부류는", res)

# 4. 플롯리(px)를 사용하여 3D 그래프 그리기 💡
fig = px.scatter_3d(
    df, 
    x='sepal length (cm)', 
    y='sepal width (cm)', 
    z='petal width (cm)', 
    color='species',
    title='Iris Dataset 3D Scatter Plot'
)
fig.show()
# print(iris.data)
# print(iris.target)
# print(iris.feature_names)
# print(iris.target_names)
# print(iris.DESCR)  # 데이터셋에 대한 설명 출력