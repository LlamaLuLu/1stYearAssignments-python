# Takes in list of marks & outputs histogram representation of marks according to mark categories at UCT
# Lulama Lingela
# 14 April 2023

marks = input("Enter a space-separated list of marks:\n").split(" ")

category_f = []
category_3 = []
category_2m = []
category_2p = []
category_1 = []

for score in marks:
    score = int(score)
    # sorts & stores mark into score category
    if score < 50:   # fail
        category_f.append(score)
    elif 50 <= score < 60:   # 3rd
        category_3.append(score)
    elif 60 <= score < 70:   # lower 2nd
        category_2m.append(score)
    elif 70 <= score < 75:   # upper 2nd
        category_2p.append(score)
    else:   # 1st
        category_1.append(score)

# histogram of scores per category
print(f"""1 |{"X" * len(category_1)}
2+|{"X" * len(category_2p)}
2-|{"X" * len(category_2m)}
3 |{"X" * len(category_3)}
F |{"X" * len(category_f)}""")
