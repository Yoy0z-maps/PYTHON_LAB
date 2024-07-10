# zip()은 iterable 객체를 인자로 받고, 각 객체가 담고 있는 원소를 터플 형태로 차례로 접근할 수 있는 iterator를 반환한다
numbers = [1, 2, 3]
letters = ['A', 'B', 'C']

for pair in zip(numbers, letters):
    print(pair)

# zip()은 나열된 리스트에서 원소를 하나씩 꺼내주는 역할을 한다.
iterable = [[n, l]for n, l in zip(numbers, letters)]
print(iterable)
