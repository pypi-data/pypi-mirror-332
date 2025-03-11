import json
import os  # Импортируем модуль os для работы с путями


def example_json():
    data = {
        'Example_code': True,
        'Example': False,
        'data': 1,
        'Local': 0
    }

    with open("data.json", 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def create_json(data, name, directory):
    # Проверяем, существует ли директория, если нет, создаем ее
    if directory and not os.path.exists(directory):
        os.makedirs(directory)

    # Создаем JSON-файл
    with open(os.path.join(directory, name + ".json"), 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def json_config(config, name, directory):
    # Проверяем, существует ли файл конфигурации
    file_path = os.path.join(directory, name + ".json")

    if os.path.exists(file_path):
        # Если файл существует, загружаем текущие настройки
        with open(file_path, 'r', encoding='utf-8') as file:
            existing_config = json.load(file)

        # Обновляем существующие настройки новыми значениями
        existing_config.update(config)
        config = existing_config  # Обновляем конфигурацию для сохранения

    # Сохраняем (или обновляем) конфигурацию в JSON-файл
    create_json(config, name, directory)