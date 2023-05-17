a=1
b=1
if a==b:
    print("두개의 값은 같습니다.")
if a!=b:
    print("두개의 값은 같지 않습니다.")

c=2
if a==c:
    print("두개의 값은 같습니다.")
else:
    print("두개의 값은 같지 않습니다.")

if a>c:
    print("a 값이 더 큽니다.")
elif a<c:
    print("c 값이 더 큽니다.")
else:
    print("두개의 값은 같습니다.")

if a>=b:
    print("a값이 더 크거나 작습니다.")
if a<=b:
    print("a값이 더 작거나 같습니다.")

d=2
if a==b and c==d:
    print("두 조건 모두 만족")
if a==b or c==d:
    print("두 조건 중 하나라도 만족하면")

a_str="hello python"
if a_str=="hello python":
    print("hello python 문자열이 같습니다.")
if a_str=="hi python":
    print("hi python 문자열이 같습니다.")
if "hello" in a_str:
    print("hello 가 포함되어 있습니다.")
if "hello" not in a_str:
    print("hello 가 포함되어 있지 않습니다.")
if "hi" not in a_str:
    print("hi 가 포함되어 있지 않습니다.")

a_list=["안녕",1,2,"파이썬"]
if "안녕" in a_list:
    print("a_list에 안녕이 포함되어 있습니다.")
if 2 in a_list:
    print("a_list에 숫자 2가 포함되어 있습니다.")

if "안녕" not in a_list:
    print("a_list에 안녕이 포함되어 있지 않습니다.")
if 5 not in a_list:
    print("a_list에 숫자 5는 없습니다.")