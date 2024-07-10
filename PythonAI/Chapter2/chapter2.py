import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
# numpy는 고차원의 배열을 위한 라이브러리이다.
import numpy as np

# 이 데이터 자체는 35개의 빙어와 14개의 도미의 데이터가 차례대로 들어가있다
# 그래서 35개의 훈련데이터와 14개의 평가 데이터를 나눴을 때 샘플링 편향이 일어난다
# 따라서 line38의 평가 점수가 0.0인 것이며, 훈련/평가 데이터에는 빙어와 도미가 골고루 섞여 있어야한다.
fish_length = [25.4, 26.3, 26.5, 29.0, 29.0, 29.7, 29.7, 30.0, 30.0, 30.7, 31.0, 31.0,
               31.5, 32.0, 32.0, 32.0, 33.0, 33.0, 33.5, 33.5, 34.0, 34.0, 34.5, 35.0,
               35.0, 35.0, 35.0, 36.0, 36.0, 37.0, 38.5, 38.5, 39.5, 41.0, 41.0, 9.8,
               10.5, 10.6, 11.0, 11.2, 11.3, 11.8, 11.8, 12.0, 12.2, 12.4, 13.0, 14.3, 15.0]

fish_weight = [242.0, 290.0, 340.0, 363.0, 430.0, 450.0, 500.0, 390.0, 450.0, 500.0, 475.0, 500.0,
               500.0, 340.0, 600.0, 600.0, 700.0, 700.0, 610.0, 650.0, 575.0, 685.0, 620.0, 680.0,
               700.0, 725.0, 720.0, 714.0, 850.0, 1000.0, 920.0, 955.0, 925.0, 975.0, 950.0, 6.7,
               7.5, 7.0, 9.7, 9.8, 8.7, 10.0, 9.9, 9.8, 12.2, 13.4, 12.2, 19.7, 19.9]

# 여기서 2차원 배열 속에 있는 하나 하나의 1차원 배열을 샘플이라고 부른다. 이 2차원 배열에는 49개의 샘플이 있다
fish_data = [[l, w] for l, w in zip(fish_length, fish_weight)]    # 물고기의 정보
fish_target = [1]*35 + [0]*14    # 정답 = 물고기의 정체 (인공지능은 0과 1로 구분함)

kn = KNeighborsClassifier()

# slicing : => 0 생략 가능
train_input = fish_data[:35]  # 0~34 index
train_target = fish_target[:35]
test_input = fish_data[35:]    # 35~last index
test_target = fish_target[35:]

kn = kn.fit(train_input, train_target)
score = kn.score(test_input, test_target)
print(score)

# 파이선 리스트를 넘파이 배열로 바꾸는 법. array()메소드에 리스트를 인수로 전달하기
input_arr = np.array(fish_data)
target_arr = np.array(fish_target)

print(input_arr)    # 2개의 열 => 특성, 49개의 행 => 샘플
# shape는 넘파이 배열의 크기를 알 수 있다.  위의 코드(line 38)를 결과물을 개수로 확인하는 것
print(input_arr.shape)


# 데이터를 무작위로 섞어서 학습을 시작해야하는데 중요한 점이 있다. 앞의 35개의 데이터는 1이고, 14개는 0이다.
# 이 데이터들을 무작위로 섞을 때 반드시 인덱스 번호를 기억해야한다

# numpy arrange(n)메소드는 0부터 1씩 증가하는 n개의 인덱스를 만들 수 있다
# numpy의 무작위 결과를 만드는 함수들은 실행할 때마다 다른 결과를 만들기 때문에 일정한 결과를 얻기 위해서 초기에 랜덤시드를 정하였다
np.random.seed(42)  # 시드 값으로는 0 이상의 정수를 넣어주면 되는데 42이로 하는게 국룰이간하다
# 컴퓨터 프로그램에서 발생한 랜덤값은 무작위가 아니라 특정 시작 숫자값을 정해주면 정해진 알고리즘에 따라 난수처럼 보이는 수열을 생성하는건데, 이때 설정해주는 특정 시작 숫자가 바로 시드이다
# 따라서 시드 값을 고정해주면  같은 값을 알 수 있다
index = np.arange(49)
np.random.shuffle(index)

print(index)


# 넘파이는 배열 인덱싱 기능을 제공한다. 1개의 인덱스가 아닌 여러 개의 인덱스로 한 번에 여러 개의 원소를 선택할 수 있다
print(input_arr[[1, 3]])  # 두 번째와 네 번째 샘플 선택

# 위에서 만든 index 배열의 처음 35개를 input_arr과 target_arr에 전달하여 랜덤하게 35개의 훈련 샘플 세트를 만듬
train_input = input_arr[index[:35]]
train_target = target_arr[index[:35]]

# 만들어진 index의 첫번째 값은 13이다. 따라서 train_input의 첫번째 원소는 input_arr의 14번째 원소가 들어있다
print(input_arr[13], train_input[0])


# 나머지 14개의 테스트 샘플 세트 만들기
test_input = input_arr[index[35:]]
test_target = target_arr[index[35:]]


# 데이터가 잘 섞였는지 확인
# 2차원 배열은 행과 열 인덱스를 ,로 나누어 지정한다
plt.scatter(train_input[:, 0], train_input[:, 1])
# 슬라이싱 연산자로 처음부터 마지막 원소까지 모두 선택하는 경우 시작과 종료 인덱스를 모두 생략할 수 있다
plt.scatter(test_input[:, 0], test_input[:, 1])
plt.xlabel('length')
plt.ylabel('weight')
plt.show()


kn = kn.fit(train_input, train_target)
print(kn.score(test_input, test_target))


print(kn.predict(test_input))
print(test_target)
