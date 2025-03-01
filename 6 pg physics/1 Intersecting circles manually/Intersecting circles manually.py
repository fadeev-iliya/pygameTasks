x_a, y_a, r_a = map(int, input().split())
x_b, y_b, r_b = map(int, input().split())

s = ((x_b - x_a) ** 2 + (y_b - y_a) ** 2) ** 0.5
print('YES' if (r_a + r_b) >= s else 'NO')
