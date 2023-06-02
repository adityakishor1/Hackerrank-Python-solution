from collections import Counter

S = input()
S = sorted(S)

FREQUENCY = Counter(list(S))

for k, v in FREQUENCY.most_common(3):
    print(k, v)
