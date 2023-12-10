def reverse(st):
    st = st.split()[::-1]
    st = " ".join(st)
    return st

print(reverse("gjgj ghgh"))