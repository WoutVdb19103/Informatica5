def behoort_tot_taal(woord, letters):
    st = set(woord)
    st.discard(' ')

    return st.issubset(letters) and len(st) > 0

def is_onleesbaar(woord, letters):
    st = set(woord)
    st.discard(' ')
    return st.isdisjoint(letters)

def perfect_woord(woord, letters):
    st = set(woord)
    st.discard(' ')

    return st.issuperset(letters)