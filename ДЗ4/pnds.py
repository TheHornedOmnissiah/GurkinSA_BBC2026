import pandas
import numpy


df = pandas.read_csv('tested.csv')
n = int(input("Введите количество строк для вывода: "))
print(df.head(n))
print()

print("Последние 5 строк")
print(df.tail(5))
print()

rows, cols = df.shape
print("Размер DataFrame")
print(f"Количество строк: {rows}")
print(f"Количество столбцов: {cols}")
print()

print("Названия столбцов")
print(df.columns.tolist())
print()

print("Типы данных каждого столбца")
print(df.dtypes)
print()

numeric_features = ['Age', 'SibSp', 'Parch', 'Fare']
categorical_features = ['Pclass', 'Sex', 'Embarked', 'Survived', 'Name', 'Cabine']
print("Разделение признаков")
print(f"Числовые признаки: {numeric_features}")
print(f"Категориальные признаки: {categorical_features}")
print()

print("Статистика числовых признаков")
stats = df[numeric_features].agg(['mean', 'median', 'min', 'max', 'std'])
print(stats)
print()

print("Количество пассажиров каждого класса (Pclass)")
print(df['Pclass'].value_counts().sort_index())
print()

print("Уникальные значения в Embarked")
print(f"Количество уникальных значений: {df['Embarked'].nunique()}")
print(f"Уникальные значения: {df['Embarked'].unique().tolist()}")
print(f"Количество каждого значения:\n{df['Embarked'].value_counts()}")
print()

print("Количество пропусков в каждом столбце")
missing_counts = df.isnull().sum()
print(missing_counts)
print()

print("Процент пропусков относительно общего числа строк")
missing_percent = (df.isnull().sum() / len(df) * 100).round(2)
print(missing_percent)
print()

print("Столбец с максимальным количеством пропусков")
max_missing_col = missing_counts.idxmax()
max_missing_val = missing_counts.max()
print(f"Столбец: {max_missing_col}, пропусков: {max_missing_val}")
print()

print("Характеристики Age ДО заполнения пропусков")
age_before = {
    'Среднее': df['Age'].mean(),
    'Медиана': df['Age'].median(),
    'Минимум': df['Age'].min(),
    'Максимум': df['Age'].max(),
    'Стандартное отклонение': df['Age'].std(),
    'Количество известных значений': df['Age'].count()
}
for key, val in age_before.items():
    print(f"  {key}: {val.round(4)}" if isinstance(val, float) else f"  {key}: {val}")
print()

age_median = df['Age'].median()
df['Age'] = df['Age'].fillna(age_median)
print(f"Пропуски в Age заполнены медианой = {age_median}")
print()

print("Характеристики Age ПОСЛЕ заполнения пропусков")
age_after = {
    'Среднее': df['Age'].mean(),
    'Медиана': df['Age'].median(),
    'Минимум': df['Age'].min(),
    'Максимум': df['Age'].max(),
    'Стандартное отклонение': df['Age'].std(),
    'Количество известных значений': df['Age'].count()
}
for key, val in age_after.items():
    print(f"  {key}: {val.round(4)}" if isinstance(val, float) else f"  {key}: {val}")
print()

print("Таблица сравнения До / После обработки Age")
comparison_df = pandas.DataFrame({
    'Показатель': age_before.keys(),
    'До обработки': age_before.values(),
    'После обработки': age_after.values()
})
print(comparison_df.to_string(index=False))
print()

print("Удаление строк с отсутствующим Embarked")
print(f"Пропусков в Embarked до удаления: {df['Embarked'].isnull().sum()}")
df = df.dropna(subset=['Embarked'])
print(f"Пропусков в Embarked после удаления: {df['Embarked'].isnull().sum()}")
print(f"Количество строк после удаления: {len(df)}")
print()

print("Обработка столбца Cabin")
cabin_missing_ratio = df['Cabin'].isnull().sum() / len(df)
print(f"Доля пропусков в Cabin: {cabin_missing_ratio.round(4)} ({(cabin_missing_ratio*100).round(2)}%)")

if cabin_missing_ratio > 0.5:
    df = df.drop(columns=['Cabin'])
    print("Столбец Cabin удалён (доля пропусков > 50%)")
else:
    print("Столбец Cabin оставлен")
print()

print("Оставшиеся пропуски после обработки")
remaining_missing = df.isnull().sum()
print(remaining_missing[remaining_missing > 0] if remaining_missing.sum() > 0 else "Пропусков не осталось")
print()

final_rows, final_cols = df.shape
print("Сравнение размеров DataFrame")
print(f"{''*25} {'До обработки':>15} {'После обработки':>18} {'Изменение':>12}")
print("-" * 75)
print(f"{'Количество строк':25} {rows:>15} {final_rows:>18} {final_rows - rows:>+12}")
print(f"{'Количество столбцов':25} {cols:>15} {final_cols:>18} {final_cols - cols:>+12}")
print()

survived = df['Survived'].values
total_passengers = len(survived)
survived_count = numpy.sum(survived)
survival_rate_total = (survived_count / total_passengers) * 100

print("Общий процент выживших")
print(f"Всего пассажиров: {total_passengers}")
print(f"Выживших: {survived_count}")
print(f"Процент выживших: {survival_rate_total.round(2)}%")
print()

sex = df['Sex'].values
survived = df['Survived'].values

male_mask = sex == 'male'
female_mask = sex == 'female'

male_count = numpy.sum(male_mask)
female_count = numpy.sum(female_mask)

male_survived = numpy.sum(survived[male_mask])
female_survived = numpy.sum(survived[female_mask])

male_survival_rate = (male_survived / male_count) * 100
female_survival_rate = (female_survived / female_count) * 100

print("Процент выживших по полу")
print(f"Мужчины: {male_survived} из {male_count} выжили ({male_survival_rate:.2f}%)")
print(f"Женщины: {female_survived} из {female_count} выжили ({female_survival_rate:.2f}%)")
print()

age = df['Age'].values

age_male = age[male_mask]
age_female = age[female_mask]

mean_age_male = numpy.nanmean(age_male)
mean_age_female = numpy.nanmean(age_female)

print("Средний возраст по полу")
print(f"Средний возраст мужчин: {mean_age_male.round(2)} лет")
print(f"Средний возраст женщин: {mean_age_female.round(2)} лет")
print()

survived_mask = survived == 1
died_mask = survived == 0

survived_male_age = age[male_mask & survived_mask]
mean_age_survived_male = numpy.nanmean(survived_male_age)

died_male_age = age[male_mask & died_mask]
mean_age_died_male = numpy.nanmean(died_male_age)

survived_female_age = age[female_mask & survived_mask]
mean_age_survived_female = numpy.nanmean(survived_female_age)

died_female_age = age[female_mask & died_mask]
mean_age_died_female = numpy.nanmean(died_female_age)

print("=== 34. Средний возраст выживших и погибших по полу ===")
print(f"Мужчины выжившие: {mean_age_survived_male.round(2)} лет")
print(f"Мужчины погибшие: {mean_age_died_male.round(2)} лет")
print(f"Женщины выжившие: {mean_age_survived_female.round(2)} лет")
print(f"Женщины погибшие: {mean_age_died_female.round(2)} лет")
print()

fare = df['Fare'].values

min_fare = numpy.min(fare)
max_fare = numpy.max(fare)
mean_fare = numpy.mean(fare)

print("Статистика стоимости билета")
print(f"Минимальная стоимость: {min_fare.round(2)}")
print(f"Максимальная стоимость: {max_fare.round(2)}")
print(f"Средняя стоимость: {mean_fare.round(2)}")
print()

age_clean = age[~numpy.isnan(age)]
std_age = numpy.std(age_clean)

print("Стандартное отклонение возраста")
print(f"Стандартное отклонение возраста: {std_age.round(2)} лет")
print()

print("СВОДНАЯ ТАБЛИЦА РЕЗУЛЬТАТОВ АНАЛИЗА")

summary_data = {
    'Показатель': [
        'Общий процент выживших',
        'Процент выживших (мужчины)',
        'Процент выживших (женщины)',
        'Средний возраст мужчин',
        'Средний возраст женщин',
        'Средний возраст выживших мужчин',
        'Средний возраст погибших мужчин',
        'Средний возраст выживших женщин',
        'Средний возраст погибших женщин',
        'Минимальная стоимость билета',
        'Максимальная стоимость билета',
        'Средняя стоимость билета',
        'Стандартное отклонение возраста'
    ],
    'Значение': [
        f"{survival_rate_total.round(2)}%",
        f"{male_survival_rate.round(2)}%",
        f"{female_survival_rate.round(2)}%",
        f"{mean_age_male.round(2)} лет",
        f"{mean_age_female.round(2)} лет",
        f"{mean_age_survived_male.round(2)} лет",
        f"{mean_age_died_male.round(2)} лет",
        f"{mean_age_survived_female.round(2)} лет",
        f"{mean_age_died_female.round(2)} лет",
        f"{min_fare.round(2)}",
        f"{max_fare.round(2)}",
        f"{mean_fare.round(2)}",
        f"{std_age.round(2)} лет"
    ]
}

summary_df = pandas.DataFrame(summary_data)
print(summary_df.to_string(index=False))

age = df['Age'].values
sex = df['Sex'].values
pclass = df['Pclass'].values
survived = df['Survived'].values
name = df['Name'].values
fare = df['Fare'].values
embarked = df['Embarked'].values

mask1 = (sex == 'male') & (age > 30) & (pclass == 1)

count = numpy.sum(mask1)
print(f"Число пассажиров: {count}\n")

print("Первые 10 строк результата:")
print(f"{'№':<3} {'Имя':<40} {'Возраст':<8} {'Класс':<6} {'Билет':<8}")
print("-" * 70)

for i, idx in enumerate(numpy.where(mask1)[0][:10], 1):
    print(f"{i:<3} {name[idx]:<40} {age[idx]:<8.0f} {pclass[idx]:<6} {fare[idx]:<8.2f}")

# Задание 2
mask2_np = ((age < 18) | (sex == 'female')) & (survived == 1)
print(f"Задание 2 (NumPy): {numpy.sum(mask2_np)} пассажиров")

# Задание 3
mean_fare_3 = numpy.nanmean(fare[pclass == 3])
mask3_np = (pclass == 3) & (fare > mean_fare_3)
print(f"Задание 3 (NumPy): {numpy.sum(mask3_np)} пассажиров")

# Задание 4
mask4_np = (age >= 20) & (age <= 40) & (embarked == 'S')
print(f"Задание 4 (NumPy): {numpy.sum(mask4_np)} пассажиров")
print()

print("Задание 37. Группировка по Pclass и Sex\n")

grouped_37 = df.groupby(['Pclass', 'Sex']).agg(
    Количество=('Survived', 'count'),
    Средний_возраст=('Age', 'mean'),
    Доля_выживших=('Survived', 'mean'),
    Средняя_стоимость_билета=('Fare', 'mean')
)

grouped_37['Доля_выживших'] = grouped_37['Доля_выживших'] * 100

grouped_37['Средний_возраст'] = grouped_37['Средний_возраст'].round(2)
grouped_37['Доля_выживших'] = grouped_37['Доля_выживших'].round(2)
grouped_37['Средняя_стоимость_билета'] = grouped_37['Средняя_стоимость_билета'].round(2)

print(grouped_37)
print()

print("Задание 38. Группировка по Embarked\n")

grouped_38 = df.groupby('Embarked').agg(
    Количество=('Survived', 'count'),
    Процент_выживших=('Survived', 'mean')
)

grouped_38['Процент_выживших'] = (grouped_38['Процент_выживших'] * 100).round(2)

print(grouped_38)
print()

print("Задание 39. Класс с наибольшей долей выживших\n")

survival_by_class = df.groupby('Pclass')['Survived'].mean() * 100
survival_by_class = survival_by_class.round(2)

print("Доля выживших по классам:")
print(survival_by_class)
print()

best_class = survival_by_class.idxmax()
best_rate = survival_by_class.max()

print(f"Класс с наибольшей долей выживших: {best_class}-й класс ({best_rate}%)")
print()

grouped = df.groupby(['Pclass', 'Sex']).agg(
    Количество=('Survived', 'count'),
    Средний_возраст=('Age', 'mean'),
    Доля_выживших=('Survived', 'mean'),
    Средняя_стоимость_билета=('Fare', 'mean')
)
grouped['Доля_выживших'] = (grouped['Доля_выживших'] * 100).round(2)
grouped['Средний_возраст'] = grouped['Средний_возраст'].round(2)
grouped['Средняя_стоимость_билета'] = grouped['Средняя_стоимость_билета'].round(2)

df.to_csv('titanic_processed.csv', index=False, encoding='utf-8')
print("Обработанный DataFrame сохранён в 'titanic_processed.csv'")
print(f"Размер: {df.shape[0]} строк × {df.shape[1]} столбцов")
print()

grouped.to_csv('titanic_statistics.csv', encoding='utf-8')
print("Результаты группировки сохранены в 'titanic_statistics.csv'")
print(grouped)
print()

print("Проверка сохранённых данных\n")

# Загружаем обработанный DataFrame
df_loaded = pandas.read_csv('titanic_processed.csv')

print("--- Обработанный DataFrame ---")
print(f"Размер: {df_loaded.shape[0]} строк × {df_loaded.shape[1]} столбцов")
print(f"Столбцы: {df_loaded.columns.tolist()}")
print(f"Пропусков: {df_loaded.isnull().sum().sum()}")
print(f"Типы данных:\n{df_loaded.dtypes}")
print(f"\nПервые 5 строк:")
print(df_loaded.head())
print()

stats_loaded = pandas.read_csv('titanic_statistics.csv')

print("--- Статистика (группировка) ---")
print(f"Размер: {stats_loaded.shape[0]} строк × {stats_loaded.shape[1]} столбцов")
print(f"Столбцы: {stats_loaded.columns.tolist()}")
print(f"\nСодержимое:")
print(stats_loaded)
print()

print("=== Проверка целостности данных ===")
print(f"Совпадение размеров: {df.shape == df_loaded.shape}")
print(f"Совпадение столбцов: {list(df.columns) == list(df_loaded.columns)}")
print(f"Совпадение данных: {df.equals(df_loaded)}")
