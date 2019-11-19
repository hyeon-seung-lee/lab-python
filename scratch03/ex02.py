import matplotlib.pyplot as plt

# 선 그래프(line chart)
x = [i for i in range(10)]
print(x)

y1 = [2 ** x for x in range(10)]
y2 = [2** x for x in range(9, -1, -1)]
y3 = [x + y for x, y in zip(y1, y2)]
print(y3)

plt.plot(x, y1, 'go:', label='example1')
plt.plot(x, y2, 'r--', y1, 'go:')
plt.plot(x, y3, 'b:',  label='example3')
plt.title('Line Chart Example')
plt.legend()
plt.show()
