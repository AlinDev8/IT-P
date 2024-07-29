def circular_array_path(n, m):
    
    circular_array = list(range(1, n + 1))
    
    
    print("Круговой массив:", ''.join(map(str, circular_array)) + ".")
    
    
    path = []
    
    current_position = 0
    intervals = [] 
    visited = set()  

    while current_position not in visited:
        interval = []
        for i in range(m):
            interval.append(circular_array[(current_position + i) % n])
        intervals.append(''.join(map(str, interval)))  
        path.append(circular_array[current_position])
        visited.add(current_position)
        current_position = (current_position + m) % n
    
    print("При длине обхода", m, "получаем интервалы:", ', '.join(intervals) + ".")
    
    return path

if __name__ == "__main__":
    n = int(input("Введите значение n: "))
    m = int(input("Введите значение m: "))
    
    result = circular_array_path(n, m)
    
    print("Полученный путь:", ''.join(map(str, result)) + ".")

