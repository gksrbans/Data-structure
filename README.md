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

# Programmers in python 

See [Programmers](https://programmers.co.kr/)
