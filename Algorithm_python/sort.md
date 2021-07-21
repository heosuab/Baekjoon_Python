## 1. 선택 정렬 : Selection Sort

정렬되어 있지 않은 데이터 중 가장 작은 데이터를 선택하여 맨 앞부터 순서대로 정렬해 나가는 알고리즘

입력 배열이 이미 정렬되어 있거나 말거나 상관없이 동일한 연산량을 갖기 때문에 최적화의 여지가 적어 성능이 떨어지는 편

가장 구현이 쉬운 정렬 알고리즘

* 시간복잡도 :  ![figure1](./img/figure1.gif)

  루프문을 통해 모든 인덱스에 접근 : ![figure2](./img/figure2.gif), 최소값을 찾으면 현재 인덱스와 swap : ![figure2](./img/figure2.gif)

#### 구현

~~~python
def selection_sort(arr):
    for i in range(len(arr)-1):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
~~~



## 2. 거품 정렬 : Bubble Sort

뒤에서부터 앞으로 정렬을 진행하는 구조

배옆 내의 값들을 앞뒤로 서로 비교하며 자리를 바꾸는 작업 반복

작은 값을 앞으로 가져오겠다라는 개념을 반대로 이용하여 큰 값을 뒤로 보내며 원소들끼리 위치를 변경하는 모습이 물방울이 이동하는 것과 같이 보여서 Bubble Sort라는 이름 명명

큰 값들을 뒤에서부터 앞으로 하나씩 쌓아나가게 됨, 원소가 자리를 잡을때마다 정렬 범위가 하나씩 줄어들게 됨

제일 작은 값을 찾아 맨 앞에 위치시키는 선택정렬과는 정 반대의 정렬방향

타 정렬 알고리즘에 비하여 swap이 빈번히 일어남

* 시간복잡도 : ![figure1](./img/figure1.gif)

  루프문을 통해 모든 인덱스에 방문 : ![figure2](./img/figure2.gif), 인접한 원소와 대소비교 및 swap : ![figure2](./img/figure2.gif)

#### 예시

1. Initial : [5, 3, 4, 1, 2]
2. Pass 1 : [3, 4, 1, 2, 5]
3. Pass 2 : [3, 1, 2, 4, 5]
4. Pass 3 : [1, 2, 3, 4, 5]

#### 구현

~~~python
def bubble_sort(arr):
    for i in range(len(arr)-1, 0, -1):
        for j in range(len(i)):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
~~~



## 3. 삽입 정렬 : Insertion Sort

모든 요소를 앞에서부터 정렬 범위를 확장시켜나가며 정렬 진행

이미 정렬된 배열 부분과 확장된 범위 부분을 비교하며, 자신의 위치를 찾아 삽입함으로써 정렬 완성

선택, 거품 정렬과는 달리 정렬이 진행될수록 범위 넓어짐

outer루프는 순방향, inner루프는 역방향으로 반복 진행

* 시간복잡도 : ![figure1](./img/figure1.gif)

  루프문을 통해 정렬 범위를 2개로 시작하여 전체로 확장해 나아가기 때문에 기본적으로 ![figure2](./img/figure2.gif)시간을 소모하며, 각 회차마다 정렬 범위에 추가된 값과 기존 값들과의 대소 비교 및 swap을 위해 ![figure2](./img/figure2.gif) 의 시간이 추가적으로 소모된다.

#### 예시

1. Initial : [8, 5, 6, 2, 4]
2. Pass 1 : [5, 8, 6, 2, 4]
3. Pass 2 : [5, 6, 8, 2, 4]
4. Pass 3 : [2, 5, 6, 8, 4]
5. Pass 4 : [2, 4, 5, 6, 8]

#### 구현

~~~python
def insertion_sort(arr):
    for end in range(1, len(arr)): #index 1원소부터 정렬 시작
        for i in range(end, 0, -1):
            if arr[i-1] > arr[i]:
                arr[i], arr[i-1] = arr[i-1], arr[i]
    return arr
~~~



## 퀵 정렬 : Quick Sort

분할 정복(Divide & Conquer) 기법과 재귀 알고리즘을 이용한 정렬 알고리즘

정렬을 위해 pivot이라는 임의의 기준값 사용

pivot값을 기준으로 더 작은 값과 더 큰 값으로 반복적으로 분할하며 정렬해 나아가는 방식

* 시간복잡도(이상적 경우) : ![figure3](./img/figure3.gif)

  작은값과 큰 값이 동일한 개수로 분할되었을 경우

* 시간복잡도(최악의 경우) : ![figure1](./img/figure1.gif)

  pivot선택으로 값이 한쪽으로 치우치게 되었을 경우

  따라서 상용 코드에서는 중앙값(median)에 가까운 값을 pivot으로 설정할 수 있도록 하는 섬세한 전략이 요구되며, 배열의 첫 값과 중앙값 그리고 마지막 값 중 크기가 중간인 값을 사용하는 방법을 주로 사용한다.

#### 예시

1. Initial : [6, 5, 1, 4, 7, 2, 3], pivot=중간값
2. Pass 1 : [1, 2, 3] < 4 < [6, 5, 7]
3. Pass 2 : [1] < 2 < [3] < 4 < [5] < 6 < 7

#### 구현

~~~python
def quick_sort(arr):
    if len(arr)==1:
        return arr
    pivot = arr[len(arr)//2]
    lesser_list, equal_list, greater_list = [], [], []
    for i in arr:
        if i < pivot:
            lesser_list. append(i)
        elif i > pivot:
            greater_list.append(i)
        else:
            equal_list.append(i)
    return quick_sort(lesser_list) + equal_list + quick_sort(greater_list)
~~~



## 병합 정렬 : Merge Sort

병합 정렬은 퀵 정렬과 동일하게 분할 정복 기법과 재귀 알고리즘을 이용

주어진 배열의 크기가 1이 될 때까지 반씩 쪼갠 뒤 정렬을 진행하며 병합

크게 Split단계와 Merge 단계로 나눌 수 있으며, 중간 인덱스만 찾으면 되는 Split 비용보다 모든 값들을 비교해야 하는 Merge 비용이 더 크다.

* 시간복잡도 : ![figure3](./img/figure3.gif)

  Split단계는 반복수가 거듭할수록 반으로 줄어들기 때문에 ![figure4](./img/figure4.gif)의 시간이 필요하며, 병합시에는 모든 값들을 비교해야 하므로 ![figure2](./img/figure2.gif)의 시간이 소요

#### 예시

1. Initial : [6, 5, 3, 1, 8, 7, 2, 4]
2. Split 1 : [6, 5, 3, 1], [8, 7, 2, 4]
3. Split 2 : [6, 5], [3, 1], [8, 7], [2, 4]
4. Split 3 : [6], [5], [3], [1], [8], [7], [2], [4]

5. Merge 1: [5, 6], [1, 3], [7, 8], [2, 4]
6. Merge 2 : [1, 3, 5, 6], [2, 4, 7, 8]
7. Merge 3 : [1, 2, 3, 4, 5, 6, 7, 8]

#### 구현

~~~python
def merge_sort(arr):
    if len(arr) < 2:
        return arr
    
    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    merged_arr = []
    l = h = 0
    
    while l<len(left) and h<len(right):
        if left[l] < right[h]:
            merged_arr.append(left[l])
            l += 1
        else:
            merged_arr.append(right[h])
            h += 1
            
   	merged_arr += left[l:]
    merged_arr += right[h:]
    
    return merged_arr
~~~













#### References

* https://duwjdtn11.tistory.com/514