# ptreegraph
дз1_2 (менеджер пакетов)

## Использование:
1. Запустить скрипт ptreegraph.py
2. Ввести наименование пакета.
3. Получить список зависимотей на языке graphviz

## Принцип работы
1. Парсим json файл заданного пакета.
2. Находим список зависимотей.
3. Вызываем рекурсивную функцию, которая проходит по каждой из зависимотей до тех пор пока не вернется null (requires_dist : null). Данная функция вернет словарь с иерархией зависимостей.
4. Затем используем полученный словарь для создания иерархии на языке graphviz.
