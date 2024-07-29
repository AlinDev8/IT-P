import sys
import statistics

def read_numbers(file_path):
    with open(file_path, 'r') as file:
        numbers = [int(line.strip()) for line in file]
    return numbers

def min_moves_to_equalize(nums):
    # Найти медиану
    median = int(statistics.median(nums))
    
    # Рассчитать общее количество шагов до медианы
    total_moves = sum(abs(num - median) for num in nums)
    
    return total_moves

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <file_path>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    
    # Чтение чисел из файла
    nums = read_numbers(file_path)
    
    # Вычисление минимального количества ходов
    result = min_moves_to_equalize(nums)
    
    # Вывод результата
    print(result)

if __name__ == "__main__":
    main()
