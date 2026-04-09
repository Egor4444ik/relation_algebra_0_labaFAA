"""
Шаблон main.py для практических задач
=====================================

ИНСТРУКЦИЯ:
1. Переименуй this файл в main.py в корне своего репозитория
2. Реализуй функцию main(input_data) так, чтобы она:
   - Принимает input_data (словарь с входными данными)
   - Обрабатывает данные
   - Возвращает результат в формате словаря

НАЧАЛЬНЫЙ ПРИМЕР для addition:
"""


def main(input_data):
    """
    Основная функция для решения практической задачи.
    
    Args:
        input_data (dict): Входные данные в формате:
                          {"stdin": "1 2"}
                          или другом формате указанном в задаче
    
    Returns:
        dict: Результат в формате {"stdout": "3"}
              или другом формате указанном в задаче
    """
    
    # Пример: Сложение двух чисел
    # Извлекаем входные данные
    stdin = input_data.get('stdin', '')
    
    # Парсим два числа из строки "1 2"
    try:
        numbers = list(map(int, stdin.split()))
        result = sum(numbers)
        
        # Возвращаем результат в ожидаемом формате
        return {'stdout': str(result)}
    except (ValueError, AttributeError):
        # Обработка ошибок
        return {'stdout': 'Error: Invalid input'}


# Тестирование локально (необязательно)
if __name__ == '__main__':
    test_input = {'stdin': '1 2'}
    print(f"Input: {test_input}")
    print(f"Output: {main(test_input)}")
