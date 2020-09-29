# Data-structure

- Study D.S. // 꾸준히 하면 다이긴다.
  
## 1. 선형 배열(Linear Array)

- 흔히 Python에서 리스트 내 원소(?)들에 대해서 append, pop등의 행위를 하는것을 말한다.
- 짚고 넘어가야 할 부분은 O(1)과 O(n)의 차이.
- O(1)는 리스트의 길이와 무관한 상수시간 동안의 시간이 소요, O(N)은 리스트 내부에 인덱스 요소를 써치하기 때문에 리스트의 길이에 비례해 시간이 소요됨.

> 시간복잡도 O(1)에 해당하는 리스트 원소의 추가,삭제(append, pop)은 리스트의 마지막에 요소를 넣었다가 뺐다가 한다.

> 하지만 시간복잡도 O(n)에 해당하는 리스트 내 원소의 삽입이나 제거(?) (insert, del) 은 리스트의 index 위치를 파라미터로 입력받는 차이점이 있다. ex) insert([index], element), del(list[index])



리스트의 조작은 밥먹듯이 하는 기본적인 것으로 리스트의 조작은 가볍게 pass 하도록 한다.  
ㄴ 리스트 조작하기 : https://dojang.io/mod/page/view.php?id=2281

그런데 문득 append()와 extend()의 차이가 무엇인지 궁금해서 구글링을 하였다.  
ㄴ 결론 : append는 x 그 자체를 원소로 넣고 extend는 iterable의 각 항목들을 넣습니다  
ㄴ https://m.blog.naver.com/PostView.nhn?blogId=wideeyed&logNo=221541104629&categoryNo=50&proxyReferer=

## 2. 정렬(Sorting)

#### 1) 선택정렬 (Selection Sort)
- 시간복잡도 : O(N^2)
- 선택정렬은 입력된 값 이외에 추가적인 메모리를 요구하지 않는 '제자리 정렬'의 일종이다.
- 내림차순의 배열을 오름차순으로 정렬할 때 가장 큰 효율을 자랑한다.
- 주어진 배열에서 최소값(min)을 찾은 후, 그 값을 배열의 가장 앞의 요소와 바꾼다.
- 이후 맨처음 위치를 빼고 상기 과정을 반복해서 정렬을 완성한다.

- 장점으로 자료의 이동 횟수가 미리 결정되지만, 같은 값의 요소인 경우 연산을 할 수도 있음.
```sh
# 랜덤한 리스트 생성 후 선택 정렬.
import random

def randomList(num):
    result = []
    for i in range(num):
            result.append(random.randint(0, num))
    return result

def selectionSort(x):
    length = len(x)
    for i in range(length - 1):
        indexMin = i;
        for j in range(i + 1, length):
            if x[indexMin] > x[j]:
                indexMin = j
        x[i], x[indexMin] = x[indexMin], x[i]
    return x

x = randomList(7777)

print(x)
print(selectionSort(x))
```

> Reference : https://gmlwjd9405.github.io/2018/05/06/algorithm-selection-sort.html


#### 2) 삽입정렬 (Insertion Sort)

- 시간복잡도 : O(N ~ N^2)
- 자료 배열의 모든 요소를 앞에서부터 차례대로 이미 정렬된 배열 부분과 비교하여, 자신의 위치를 찾아 삽입함.
- 삽입정렬은 이름 그대로 원하는 위치에 원소를 삽입하는 정렬임.
- 대상으로하는 리스트가 이미 정렬되어있는 상태에 가까울 때 최고의 효율을 자랑함.  ex) [1,2,3,4,5,7,6]
- 단점은 반대로 내림차순을 오름차순으로 바꿀경우 효율이 좋지 않음.

```sh
# 2번째 원소부터 써치
def insert_sort(x):
    for i in range(1, len(x)):
        for j in range(i, 0, -1):
            if x[j-1] > x[j]:
                x[j-1], x[j] = x[j], x[j-1]
```

> Reference : https://www.daleseo.com/sort-insertion/


#### 3) 버블정렬 (Bubble Sort)
- 시간복잡도 : O(N^2)
- 서로 인접한 두 레코드를 검사하여 정렬하는 알고리즘.
- 역시 시간복잡도 좋지 않아 잘 사용하지 않음.
- 장점으로 구현이 매우 간단하지만, 인접한 레코드를 바꾸는 것(SWAP) 보다 맞는 위치로 옮기는 거(MOVE)가 효율이 좋음.

```sh
def bubble_sort(x):
    for i in range(len(x)-1):
        temp = i
        for j in range(i+1, len(x)):
            if x[j] < x[i]:
                x[j], x[i] = x[i], x[j]
    return x
```


## 2. 스택/큐 (Stack/Queue) 

#### 1) 스택(Stack)
- 리스트의 한 쪽 끝에서만 자료를 넣고 뺄 수 있는 LIFO(후입선출) 자료구조.
- PUSH / POP을 이용해 레코드를 한쪽에서만 넣었다 뺐다함.
- Stack overflow는 스택이 꽉차서 레코드가 안들어갈 때, Stack underflow는 삭제해야할 자료가 남아있지 않을 때  
※ Stack에 기억되어 있는 자료를 삭제시킬 때는 제일 먼저 삭제할 자료가 있는지 없는지부터 확인해야 한다.


```sh
# Stack Class

class stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def isEmpty(self):
        return not self.items

stk = stack()
print(stk)
print(stk.isEmpty())
stk.push(1)
stk.push(2)

print(stk.pop())
print(stk.pop())
print(stk.isEmpty())

```

> Reference : https://korbillgates.tistory.com/79
# Programmers in python 

See [Programmers](https://programmers.co.kr/)
