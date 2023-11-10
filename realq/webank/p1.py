# n = int(input())
# arr = list(map(int, input().split()))
arr = [1,2,3,3,4]
st = set()
for x in arr:
    if x in st:
        print(len(st))
        break
    else:
        st.add(x)

