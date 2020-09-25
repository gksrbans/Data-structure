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



# Programmers in python 

See [Programmers](https://programmers.co.kr/)
