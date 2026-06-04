def remove_duplicates(seq: list) -> list:
    return list(dict.fromkeys(seq))  # sıralamayı bozmadan tekrarları kaldırır

def list_counts(seq: list) -> dict:
    L = {}
    for i in seq:
        L[i] = L.get(i, 0) + 1  # daha kısa ve temiz
    return L

def reverse_dict(d: dict) -> dict:
    rd = {}
    for i, h in d.items():
        if h not in rd:   # çakışma varsa ezmemesi için
            rd[h] = i
    return rd
