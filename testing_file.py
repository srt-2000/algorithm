n = int(input())
temp = []
temp.append(int(n))
response = 0
for line in range(n):
    temp.append(int(input()))
qnt_ab_one = sum(temp[1::])
qnt_ab_double = 0
for i in temp[1::]:
    if i // 2 != 0:
        qnt_ab_double += i // 2
print(qnt_ab_double // qnt_ab_one)