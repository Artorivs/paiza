N = int(input()) # 1 <= N <= 50
x_R, x_G, x_B = map(int, input().split()) # -100 ≦ x_R, x_G, x_B ≦ 100

print(x_R, x_G, x_B)
count = 0
cube = 0

for i in range(N):
    # if R on the R side, x_R -1, x_G and x_B remains
    side, light = input().split()
    if side == "R":
        if light == "R":
            x_R += 1
        elif light == "G":
            x_G += 1
        elif light == "B":
            x_B += 1
        elif light == "Y":
            x_R += 1
            x_G += 1
        elif light == "M":
            x_R += 1
            x_B += 1
        elif light == "C":
            x_G += 1
            x_B += 1
        elif light == "W":
            x_R += 1
            x_G += 1
            x_B += 1
    else:
        if light == "R":
            x_R -= 1
        elif light == "G":
            x_G -= 1
        elif light == "B":
            x_B -= 1
        elif light == "Y":
            x_R -= 1
            x_G -= 1
        elif light == "M":
            x_R -= 1
            x_B -= 1
        elif light == "C":
            x_G -= 1
            x_B -= 1
        elif light == "W":
            x_R -= 1
            x_G -= 1
            x_B -= 1
    if x_R == x_G == x_B:
        count += 1
        cube = x_R
        break

# if x_R == x_G == x_B, print "yes"; else print "no"
if count > 0:
    print(f'{cube}')
else:
    print("no")
