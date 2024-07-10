# matplotlib 패키지의 pyplot함수를 plt라는 이름으로 사용
import matplotlib.pyplot as plt
# k-최근접 이웃 알고르짐 구현을 위해 클래스 임포트
from sklearn.neighbors import KNeighborsClassifier

# 여기서 인공지능이 구분하기 위해 사용한 길이와 무게 정보를 특성이라고 한다.
# bream data
bream_length = [25.4, 26.3, 26.5, 29.0, 29.0, 29.7, 29.7, 30.0, 30.0, 30.7, 31.0, 31.0,
                31.5, 32.0, 32.0, 32.0, 33.0, 33.0, 33.5, 33.5, 34.0, 34.0, 34.5, 35.0,
                35.0, 35.0, 35.0, 36.0, 36.0, 37.0, 38.5, 38.5, 39.5, 41.0, 41.0]
bream_weight = [242.0, 290.0, 340.0, 363.0, 430.0, 450.0, 500.0, 390.0, 450.0, 500.0, 475.0, 500.0,
                500.0, 340.0, 600.0, 600.0, 700.0, 700.0, 610.0, 650.0, 575.0, 685.0, 620.0, 680.0,
                700.0, 725.0, 720.0, 714.0, 850.0, 1000.0, 920.0, 955.0, 925.0, 975.0, 950.0]

# smelt data
smelt_length = [9.8, 10.5, 10.6, 11.0, 11.2, 11.3,
                11.8, 11.8, 12.0, 12.2, 12.4, 13.0, 14.3, 15.0]
smelt_weight = [6.7, 7.5, 7.0, 9.7, 9.8, 8.7,
                10.0, 9.9, 9.8, 12.2, 13.4, 12.2, 19.7, 19.9]


# 산점도는 x, y축으로 이뤄진 자표계에 두 변수(x, y)의 관계를 표현하는 방법이다
# scatter()는 산점도를 그리는 함수이다. 인수로 x축, y축의 값을 받는다
plt.scatter(bream_length, bream_weight)
plt.scatter(smelt_length, smelt_weight)
plt.xlabel('length')    # x축 이름
plt.ylabel('weight')    # y축 이름
plt.show()    # 그래프를 화면에 출력 => 이 결과의 그래프는 일직선에 가까운 형태로 나타나는데 이것을 "선형"적이다라고 말한다.


# k-Nearest Neighbors 알고리즘을 사용하기 위해서 2개의 데이터를 하나로 합친다
length = bream_length + smelt_length
weight = bream_weight + smelt_weight

# scilit-learn 머신러닝 패키지를 사용하려면 2차원 리스트를 만들어야한다. => [[],[],...]
fish_data = [[l, w] for l, w in zip(length, weight)]  # reference: help/zip.py
# 두개의 데이터를 1과 0으로 표현한다
# 머신러닝에서 2개를 구분하는 경우 찾으려는 대상을 1로 놓고 그 외에는 0으로 놓는다.
# 여기서는 fish_data 안의 데이터를 순서대로 나열했기 때문에 아래와 같이 코드를 작성할 수 있다
fish_target = [1] * 35 + [0] * 14

# KNeighborsClassfier 클래스의 객체를 생성
kn = KNeighborsClassifier()
kn.fit(fish_data, fish_target)    # fit() 메서드는 주어진 데이터로 알고리즘 훈련을 진행한다.
# score() 메서드는 모델을 평가한다. 0과 1을 반환하는데 숫자가 1에 가까울 수록 데이터 학습의 정확도가 높다는 것이다.
# 모델: 머신러닝 알고리즘을 구현한 프로그램
accuracy = kn.score(fish_data, fish_target)
print(accuracy)


# predict() 메소드는 새로운 데이터를 2차원 리스트 인수로 받고, 새로운 데이터의 정답을 예측한다
print(kn.predict([[30, 600]]))

'''
사실상 KneighborsClassfier은 새로운 데이터가 등장하면 가장 가까운 데이터를 참고해서 결과를 도출하는 것이다.
따라서 KNeighborsClassfier객체를 생성할 때 n_neighbors인수를 통해참고할 데이터의 개수를 정할 수 있다. (기본 값 = 5)

Ex) kn = KNeighborsClassfier(n_neighbors=integer)


아래 코드는 데이터 개수에 따라 정확성이 1.0에서 작아질 때의 데이터의 개수를 찾아내는 코드이다. 
'''
for i in range(5, 50):
    kn.n_neighbors = i

    accuracyScore = kn.score(fish_data, fish_target)

    if accuracyScore < 1:
        print(i, accuracyScore)
        break

# Question) 왜 n_neighbors = 18부터 score()의 반환 값이 1보다 작아지기 시작하는 것인가?
