import math

def euclideanDistance(points):
    distances = []
    for i in range(len(points) - 1):
        x1, y1 = points[i]
        x2, y2 = points[i + 1]
        minus_x = (x2 - x1) ** 2
        minus_y = (y2 - y1) ** 2
        oklid = math.sqrt(minus_x + minus_y)
        distances.append(oklid)
    return min(distances)


n = int(input("Kaç nokta olacağını giriniz: "))

points = []
for _ in range(n):
    x = int(input("X değerini girin: "))
    y = int(input("Y değerini girin: "))
    points.append((x, y))


min_distance = euclideanDistance(points)
print("Minimum Öklid Mesafesi:", min_distance)