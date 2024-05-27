import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
from tabulate import tabulate

# Загрузка данных из файла с использованием openpyxl
file_path = r'C:\Users\PC1\Prog\KTP\lab2\lab2data.xlsx'
try:
    df = pd.read_excel(file_path, engine='openpyxl')
    print("Файл успешно загружен.")
except Exception as e:
    print("Ошибка загрузки файла:")
    print(e)
    exit()

# Вывод первых нескольких строк для проверки
print("Первые несколько строк загруженного DataFrame:")
print(tabulate(df.head(), headers='keys', tablefmt='pretty', showindex=False, numalign="center"))

# Вывод имен столбцов для проверки
print("Имена столбцов в загруженном файле:")
print(tabulate([df.columns], headers='keys', tablefmt='pretty', showindex=False))

# Попробуем вывести данные выбранных столбцов для просмотра
try:
    selected_columns = ['5-бальна', '10-бальна', '100-бальна', '20-бальна', '3-бальна']
    print("Данные выбранных столбцов:")
    print(tabulate(df[selected_columns], headers='keys', tablefmt='pretty', showindex=False, numalign="center"))
except KeyError as e:
    print("Ошибка: Имена столбцов не найдены в DataFrame. Проверьте правильность имен столбцов.")
    print(e)
    print("Доступные столбцы:", df.columns)
    exit()

# Нормализация данных
scaler = MinMaxScaler()
normalized_data = scaler.fit_transform(df[selected_columns])

# Создание нового DataFrame с нормализованными данными
normalized_df = pd.DataFrame(normalized_data, columns=selected_columns)
normalized_df['№'] = df['№']

print("\nНормализованные данные:")
print(tabulate(normalized_df, headers='keys', tablefmt='pretty', showindex=False, numalign="center"))

# Построение диаграмм рассеяния для каждого столбца
plt.figure(figsize=(15, 10))

# Индексы строк
indices = range(1, len(df) + 1)

# Диаграмма для 5-бальна
plt.subplot(2, 3, 1)
plt.scatter(indices, normalized_df['5-бальна'], c='blue')
plt.xlabel('Индекс строки')
plt.ylabel('Нормализованные значения')
plt.title('5-бальна')

# Диаграмма для 10-бальна
plt.subplot(2, 3, 2)
plt.scatter(indices, normalized_df['10-бальна'], c='green')
plt.xlabel('Индекс строки')
plt.ylabel('Нормализованные значения')
plt.title('10-бальна')

# Диаграмма для 100-бальна
plt.subplot(2, 3, 3)
plt.scatter(indices, normalized_df['100-бальна'], c='red')
plt.xlabel('Индекс строки')
plt.ylabel('Нормализованные значения')
plt.title('100-бальна')

# Диаграмма для 20-бальна
plt.subplot(2, 3, 4)
plt.scatter(indices, normalized_df['20-бальна'], c='purple')
plt.xlabel('Индекс строки')
plt.ylabel('Нормализованные значения')
plt.title('20-бальна')

# Диаграмма для 3-бальна
plt.subplot(2, 3, 5)
plt.scatter(indices, normalized_df['3-бальна'], c='orange')
plt.xlabel('Индекс строки')
plt.ylabel('Нормализованные значения')
plt.title('3-бальна')

plt.tight_layout()
plt.show()
