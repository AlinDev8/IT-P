import math

def determine_position(x_center, y_center, radius, points):
    radius_squared = radius ** 2
    results = []
    for x, y in points:
        distance_squared = (x - x_center) ** 2 + (y - y_center) ** 2
        if math.isclose(distance_squared, radius_squared):
            results.append(0)
        elif distance_squared < radius_squared:
            results.append(1)
        else:
            results.append(2)
    return results

def main():
    # Ввод данных для окружности
    x_center, y_center = map(float, input("Введите координаты центра окружности (x y): ").strip().split())
    radius = float(input("Введите радиус окружности: "))
    
    # Ввод данных для точек
    points = []
    print("Введите координаты точек (в формате 'x y'). Введите 'end' для завершения ввода:")
    while True:
        line = input()
        if line.lower() == 'end':
            break
        x, y = map(float, line.strip().split())
        points.append((x, y))
    
    # Определяем положение точек относительно окружности
    results = determine_position(x_center, y_center, radius, points)
    
    # Вывод результатов
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
