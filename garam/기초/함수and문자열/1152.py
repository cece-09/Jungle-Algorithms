n = input()
cnt = 0
m = n.count(" ")
cnt += m
if n[0] == " ":
    cnt -=1
if n[-1] == " ":
    cnt -=1
print(cnt+1)

# text = input().split()
# print(len(text))