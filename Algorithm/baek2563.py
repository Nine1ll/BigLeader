import sys

N = int(sys.stdin.readline())
area = [[0 for _ in range(100)] for _ in range(100)]
coordinates = []

for _ in range(N):
    coordinates.append(list(map(int, sys.stdin.readline().split())))

for coordinate in coordinates:
    for idy in range(coordinate[0], coordinate[0] + 10):
        for idx in range(coordinate[1], coordinate[1] + 10):
            area[idx][idy] = 1

result = 0

for lst in area:
    result += lst.count(1)

print(result)

# print(result)
# for coordinate in coordinates:
#     x_coordinate = coordinate[0]
#     x_coordinates.append(x_coordinate)
#     y_coordinate = coordinate[1]
#     y_coordinates.append(y_coordinate)
#
# for idx, x in enumerate(x_coordinates):
#     for i in range(idx+1, len(x_coordinates)):
#         if x_coordinates[i] in range(x, x+10+1):
#             x_min = x_coordinates[i]
#             x_max = x+10
#             y_min = 0
#             y_max = 0
#             y1 = y_coordinates[idx]
#             y2 = y_coordinates[i]
#             if y1 < y2:
#                 y_min = y1
#                 y_max = y2
#             else:
#                 y_min = y2
#                 y_max = y1
#             if y_max in range(y_min, y_min+10+1):
#                 y_m = y_max
#                 y_ma = y_min+10
#                 area = area - (y_ma - y_m)*(x_max - x_min)
#
# print(area)



