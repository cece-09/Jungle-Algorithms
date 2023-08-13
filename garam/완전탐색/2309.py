import sys

input = sys.stdin.readline
members = []
for i in range(9):
    members.append(int(input().strip()))
members.sort()
sum = sum(members)

for i in range(len(members)):
    for j in range(i + 1, len(members)):
        if sum - members[i] - members[j] == 100:
            temp1 = members[i]
            temp2 = members[j]
print(temp1, temp2)
members.remove(temp1)
members.remove(temp2)


print("\n".join(map(str, members)))  # = for i in members: \n print(i)


# import sys
# input = sys.stdin.readline
# members = []
# for i in range(9):
#     members.append(int(input().strip()))
# members.sort()
# sum = sum(members)
# for i in range(len(members)):
#     for j in range(i + 1, len(members)):
#         if sum - members[i] - members[j] == 100:
#             for k in range(len(members)):
#                 if k == i or k == j:
#                     pass
#                 else:
#                     print(members[k])
#             exit()

# 여기서 exit의 정확한 기능과 역할은?
