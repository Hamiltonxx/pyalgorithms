def f(nums):
    st = set()
    for x in nums:
        if x in st:
            return x
        else:
            st.add(x)