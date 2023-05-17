try:
    dassfsdfsdf
except:
    print("에러발생")

try:
    dassfsdfsdf
except:
    pass
    print("에러를 무시")

try:
    dassfsdfsdf
except Exception as e:
    print("에러발생 원인:",e)