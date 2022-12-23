print("""В совокупности 16 студентов определены два признака:
X — оценка по математике и Y — оценка по иностранному языку.
Совместное частотное распределение оценок задано таблицей:""")
data = [[0]*4 for _ in range(3)]
n = 16
row_x = (2, 3, 4, 5)
row_y = (3, 4, 5)
data_x = [0]*4
data_y = [0]*3
for i in range(len(data)):
    for j in range(len(data[i])):
        print(f"Введите значение для X = {2+j} Y = {3+i}")
        data[i][j] = int(input())
        data_y[i] += data[i][j]
        data_x[j] += data[i][j]
x_sum = (1/sum(data_x))
x_mean = x_sum * (sum([row_x[i] * data_x[i] for i in range(len(data_x))]))
x_disp = x_sum * sum([data_x[i] * (row_x[i]-x_mean)**2 for i in range(len(data_x))])
y_sum = (1/sum(data_y))
y_mean = y_sum * (sum([row_y[i]*data_y[i] for i in range(len(data_y))]))
y_disp = y_sum * sum([data_y[i] * (row_y[i]-y_mean)**2 for i in range(len(data_y))])
xy_sum = 0
for i in range(len(data)):
    for j in range(len(data[i])):
        xy_sum += (row_x[j]-x_mean)*(row_y[i]-y_mean)*data[i][j]
cov_xy = (1/n) * (xy_sum)
p_xy = cov_xy/((x_disp*y_disp)**0.5)
print(x_mean, x_disp, y_mean, y_disp, cov_xy, p_xy, sep="\n")