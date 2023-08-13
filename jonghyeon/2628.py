width, height = map(int, input().split())
n_cut = int(input())

w_num = [0, width]
h_num = [0, height]

for i in range(n_cut):
    direction, num = map(int, input().split())
    if direction == 0:
        h_num.append(num)
    else:
        w_num.append(num)
        
w_num.sort()
h_num.sort()

w = []
h = []
for i in range(1, len(w_num)):
      w.append(w_num[i] - w_num[i-1])
for i in range(1, len(h_num)):
      h.append(h_num[i] - h_num[i-1])
        
w.sort()
h.sort()

print(w[-1]*h[-1])
    