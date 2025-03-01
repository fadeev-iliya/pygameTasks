left_1, top_1, width_1, height_1 = map(int, input().split())
right_1 = left_1 + width_1
bottom_1 = top_1 + height_1

left_2, top_2, width_2, height_2 = map(int, input().split())
right_2 = left_2 + width_2
bottom_2 = top_2 + height_2

s1 = (left_2 <= left_1 <= right_2) or (left_2 <= right_1 <= right_2)
s2 = (top_2 <= top_1 <= bottom_2) or (top_2 <= bottom_1 <= bottom_2)
s3 = (left_1 <= left_2 <= right_1) or (left_1 <= right_2 <= right_1)
s4 = (top_1 <= top_2 <= bottom_1) or (top_1 <= bottom_2 <= bottom_1)

print("YES" if ((s1 and s2) or (s3 and s4)) or ((s1 and s4) or (s3 and s2)) else "NO")
