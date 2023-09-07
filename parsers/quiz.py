"""Calculate student grades by combining data from many sources.

Using Pandas, this script combines data from the:

* Roster список
* Homework & Exam grades
* Quiz grades

to calculate final grades for a class.
"""
from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats


# Створюємо дві константи, HERE і DATA_FOLDER, 
# щоб відстежувати розташування файлу, що виконується, 
# а також папку, де зберігаються дані. Використовуємо модуль pathlib.

HERE = Path(__file__).parent
DATA_FOLDER = HERE / "data"

# Файли, що містять інформацію для оцінок тестів. 
# В кожному файлі даних зберігається один тест:

# Потрібно обчислити буквену оцінку для кожного студента на основі 
# його первинних балів. 

# Зразок підсумкової таблиці:

# Identifier  Name    Homework        Quizzes Exams   Final Score Final Grade
# Student 1   Last, First #           #       #       #           A–F
# Student 2   Last, First #           #       #       #           A–F
# …   …   …   …   …   …   …

# У кожному рядку таблиці зберігаються всі дані для одного студента. 
# Перший стовпець містить унікальний ідентифікатор студента, 
# а другий стовпець містить ім’я студента. 
# Потім ряд стовпців зберігає домашнє завдання, тести, іспити та підсумкові бали. 
# Останній стовпець для підсумкової оцінки.

# Потрібно створити директорію під назвою data, 
# у якій зберігатимуться файли вхідних даних для сценарію журналу оцінок.


# Зразки даних містяться у файлах CSV. 
# Файл roster.csv містить інформацію про список студентів:

# Читаємо файл списку за допомогою pd.read_csv(). 
# Встановлюємо індекс за допомогою index_col та включаємо лише корисні стовпці 
# за допомогою usecols.

roster = pd.read_csv(
    DATA_FOLDER / "roster.csv",
    converters={"NetID": str.lower, "Email Address": str.lower},
    usecols=["Section", "Email Address", "NetID"],
    index_col="NetID",
)

# print(roster)
 
# NetID     Email Address             Section
# wxb12345  woody.barrera_jr@univ.edu        1
# mxl12345   malaika.lambert@univ.edu        2


# exit()

# Файл hw_exam_grades.csv, що містить домашні завдання та результати іспитів:
# Завантажити файл hw_exam_grades.csv з домашніми завданнями та оцінками іспитів:

hw_exam_grades = pd.read_csv(
    DATA_FOLDER / "hw_exam_grades.csv",
    
    # Використовуємо аргумент converters для перетворення даних у стовпцях SID 
    # і Email Address на нижній регістр. 

    converters={"SID": str.lower},
    
    # Якщо lambda-функція usecols повертає True, стовпець включено. 
    # В іншому випадку стовпець виключається. 

    usecols=lambda x: "Submission" not in x,
    
    # Вказужмо SID як стовпець індексу, щоб відповідати списку DataFrame.
    index_col="SID",
)



# print(hw_exam_grades)
# First Name   Last Name  ...  Exam 3  Exam 3 - Max Points
# SID                              ...                             
# axl60952      Aaron      Lester  ...      68                  100

# [150 rows x 28 columns]

# exit()


# Є п’ять тестів, які потрібно прочитати, та об’єднати в один DataFrame. Остаточний формат даних буде виглядати так:

# Email                   Quiz 5  Quiz 2  Quiz 4  Quiz 1  Quiz 3
# woody.barrera_jr@univ.edu   10      10      7       4       11
# john.g.2.flower@univ.edu        5       8       13      8       8
# traci.joyce@univ.edu            4       6       9       8       14
# malaika.lambert@univ.edu        6       10      13      8       10

# Цей DataFrame має стовпець електронної пошти як індекс, а кожен тест міститься в окремому стовпці. 

# Завантаження файлів тесту

quiz_grades = pd.DataFrame()
# Path.glob() використовується, щоб знайти і завантажити всі CSV-файли тестів.
for file_path in DATA_FOLDER.glob("quiz_*_grades.csv"):
    quiz_name = " ".join(file_path.stem.title().split("_")[:2])
    quiz = pd.read_csv(
        file_path,
        # Встановлюємо index_col для кожного тесту на Email кожного студента.
        converters={"Email": str.lower},
        index_col=["Email"],
        usecols=["Email", "Grade"],
    ).rename(columns={"Grade": quiz_name})
    # .rename() змінює назву Grade на щось специфічне для кожного тесту. 
    
    # Передача axis=1 у pd.concat() змушує pandas об’єднувати стовпці, 
    # а не рядки, 
    # додаючи кожен новий тест у новий стовпець об’єднаного DataFrame.
    quiz_grades = pd.concat([quiz_grades, quiz], axis=1)


# Об’єднання фреймів даних

# Об’єднаємо roster і hw_exam_grades у новий DataFrame під назвою final_data.


final_data = pd.merge(
    roster,
    hw_exam_grades,
    left_index=True,
    right_index=True,
)

# print(final_data)
# exit()

#                     Email Address  Section  ... Exam 3 Exam 3 - Max Points
# wxb12345  woody.barrera_jr@univ.edu        1  ...     90                 100

# [150 rows x 30 columns]

# Об’єднаємо final_data та quiz_grades разом.

# Будемо використовувати різні стовпці в кожному DataFrame як ключ злиття, 
# саме так pandas визначає, які рядки зберігати разом. 
# Цей процес необхідний, оскільки кожне джерело даних використовує різні унікальні ідентифікатори для кожного студента.

# У roster і hw_exam_grades є стовпець NetID або SID як унікальний ідентифікатор для певного студента. 
# Під час злиття або приєднання DataFrames у pandas найкорисніше мати індекс. 

# Тепер можна об’єднати ці два DataFrames разом. Використовуємо pd.merge(), щоб поєднати список і hw_exam_grades:

# Щоб об’єднати quiz_grades у final_data, можна використати індекс 
# із quiz_grades і стовпець електронної адреси з final_data:

final_data = pd.merge(
    final_data, quiz_grades, left_on="Email Address", right_index=True
)

# У цьому коді використовується аргумент left_on для pd.merge(), 
# щоб сказати pandas використовувати стовпець Email Address 
# у final_data під час злиття. 
# Також використовується right_index, щоб сказати pandas використовувати 
# індекс із quiz_grades у злитті.

# Тепер усі дані об’єднано в один DataFrame. 

final_data = final_data.fillna(0)

# print(final_data)
# exit()

#   Email Address  Section First Name  ... Quiz 1  Quiz 5  Quiz 2
# wxb12345  woody.barrera_jr@univ.edu        1      Woody  ...      4      10      10
# [150 rows x 35 columns]

# Оскільки кожен іспит має унікальну вагу, можна розрахувати загальний бал 
# для кожного іспиту окремо. Найбільш доцільним є використання циклу for:

n_exams = 3

for n in range(1, n_exams + 1):
    final_data[f"Exam {n} Score"] = (
        final_data[f"Exam {n}"] / final_data[f"Exam {n} - Max Points"]
    )

# Максимальна кількість балів за кожне домашнє завдання варіюється від 50 до 100. 
# Це означає, що є два способи рахувати оцінку домашнього завдання:

# За загальним балом: підсумуйте необроблені бали та максимальну кількість балів 
# незалежно, а потім візьміть співвідношення.
# За середнім балом: розділіть кожну необроблену оцінку на відповідну 
# максимальну кількість балів, потім візьміть суму цих коефіцієнтів 
# і розділіть загальну суму на кількість завдань.

# Перший метод дає вищу оцінку студентам, які стабільно виконували завдання, 
# тоді як другий метод надає перевагу студентам, які добре справлялися 
# з завданнями, які коштували більше балів.

# Обчислення балів домашнього завдання займе кілька кроків:
# Збираються стовпчики з даними домашнього завдання.
# Підраховується загальний бал.
# Обчислюється середній бал.
# Визначається найбільша оцінка, що буде використана в остаточному розрахунку оцінки.

# Спочатку потрібно зібрати всі стовпці з даними про домашнє завдання. 
# Для цього можна використати DataFrame.filter():

homework_scores = final_data.filter(regex=r"^Homework \d\d?$", axis=1)
homework_max_points = final_data.filter(regex=r"^Homework \d\d? -", axis=1)

# Створюємо серію pandas для quiz_max_points, використовуючи словник 
# як вхідні дані. Ключі словника стають мітками індексу, 
# а значення словника стають значеннями серії.
# Оскільки мітки індексів у quiz_max_points мають ті самі назви, 
# що й quiz_scores, не потрібно використовувати DataFrame.set_axis() для тестів. 

sum_of_hw_scores = homework_scores.sum(axis=1)
sum_of_hw_max = homework_max_points.sum(axis=1)
final_data["Total Homework"] = sum_of_hw_scores / sum_of_hw_max

hw_max_renamed = homework_max_points.set_axis(homework_scores.columns, axis=1)
average_hw_scores = (homework_scores / hw_max_renamed).sum(axis=1)
final_data["Average Homework"] = average_hw_scores / homework_scores.shape[1]

final_data["Homework Score"] = final_data[
    ["Total Homework", "Average Homework"]
].max(axis=1)

# print(final_data)
# exit()


# Email Address  Section  ... Average Homework Homework Score
# wxb12345  woody.barrera_jr@univ.edu        1  ...         0.799405       0.808108

# [150 rows x 41 columns]

# Підраховуємо оцінку тестів. 
# Тести мають різну максимальну кількість балів, 
# тому потрібно виконати ту саму процедуру, що й для домашнього завдання. 
# Максимальна оцінка для кожного тесту не вказана в таблицях даних тесту, 
# тому потрібно створити  pandas.Series, щоб зберегти цю інформацію:

quiz_scores = final_data.filter(regex=r"^Quiz \d$", axis=1)
quiz_max_points = pd.Series(
    {"Quiz 1": 11, "Quiz 2": 15, "Quiz 3": 17, "Quiz 4": 14, "Quiz 5": 12}
)

# Іншим аргументом, який передаєтться DataFrame.filter(), є axis. 
# Багато методів DataFrame можуть працювати як по рядках, так і по стовпцях, 
# і можна перемикатися між двома підходами за допомогою аргументу осі. 
# З аргументом за замовчуванням axis=0, pandas шукатиме рядки в індексі, 
# які відповідають переданому регулярному виразу. 
# Якщо потрібно знайти всі стовпці, які відповідають регулярному виразу, 
# потрібно передать axis=1.

# Підсумуємо два значення незалежно, а потім обчислимо загальний бал 
# за домашнє завдання:

sum_of_quiz_scores = quiz_scores.sum(axis=1)
sum_of_quiz_max = quiz_max_points.sum()
final_data["Total Quizzes"] = sum_of_quiz_scores / sum_of_quiz_max

# За замовчуванням .sum() додасть значення для всіх рядків у кожному стовпці. 
# Сума всіх стовпців для кожного рядка, буде обчислена з аргументом axis=1.

# print(final_data)
# exit()

# Email Address  Section  ... Homework Score Total Quizzes
# wxb12345  woody.barrera_jr@univ.edu        1  ...       0.808108      0.608696
# [150 rows x 42 columns]

# Вибираємо два стовпці, щойно створені,["Total Homework", "Average Homework"], 
# і призначаємо максимальне значення новому стовпцю під назвою "Homework Score". 
# Беремо максимум для кожного студента з віссю=1.

# Максимальне значення, яке буде використано для остаточного розрахунку оцінки:

average_quiz_scores = (quiz_scores / quiz_max_points).sum(axis=1)
final_data["Average Quizzes"] = average_quiz_scores / quiz_scores.shape[1]

final_data["Quiz Score"] = final_data[
    ["Total Quizzes", "Average Quizzes"]
].max(axis=1)

# print(final_data)
# exit()


# Email Address  Section  ... Average Quizzes Quiz Score
# wxb12345  woody.barrera_jr@univ.edu        1  ...        0.602139   0.608696
# [150 rows x 44 columns]

# Розрахунок літерної оцінки
# Щоб визначити остаточну оцінку потрібно помножити кожен бал на його вагу
# Використовуємо pandas.Series для зберігання вагових коефіцієнтів. 
# Надаємо вагу кожному компоненту класу. 
# Іспит 1 оцінюється в 5 відсотків, 
# іспит 2 - 10 відсотків, 
# іспит 3 - 15 відсотків, 
# тести - 30 відсотків, а домашнє завдання - 40 відсотків загальної оцінки.

weightings = pd.Series(
    {
        "Exam 1 Score": 0.05,
        "Exam 2 Score": 0.1,
        "Exam 3 Score": 0.15,
        "Quiz Score": 0.30,
        "Homework Score": 0.4,
    }
)

# Розрахунок літерної оцінки

# Поєднуємо відсотки з балами, які розраховані раніше, 
# щоб визначити остаточний бал. 
# Вибираємо стовпці final_data, які мають ті самі назви, що й індекс 
# у вагових коефіцієнтахю 
# Обчислюємо суму стовпців для кожного студента за допомогою 
# DataFrame.sum(axis=1) і призначаємо результат новому стовпцю 
# під назвою «Final Score»:

final_data["Final Score"] = (final_data[weightings.index] * weightings).sum(
    axis=1
)

# print(final_data)
# exit()
#                      Email Address  Section  ... Quiz Score Final Score
# wxb12345  woody.barrera_jr@univ.edu        1  ...   0.608696    0.745852

# [150 rows x 45 columns]

# Значення в цьому стовпці для кожного студента є числом із плаваючою комою 
# від 0 до 1. Множимо підсумковий бал кожного студента на 100, 
# щоб оцінити його за шкалою від 0 до 100, а потім використовуєте numpy.ceil(), 
# щоб округлити кожен бал до наступного найвищого цілого числа.

final_data["Ceiling Score"] = np.ceil(final_data["Final Score"] * 100)

# print(final_data)
# exit()

# Email Address  Section  ... Final Score Ceiling Score
# wxb12345  woody.barrera_jr@univ.edu        1  ...    0.745852          75.0

# [150 rows x 46 columns]

# Останнє, що потрібно зробити, це зіставити максимальний бал кожного студента 
# з літерною оцінкою:

# A: Оцінка 90 або вище
# B: Оцінка від 80 до 90
# C: Оцінка між 70 і 80
# D: Оцінка від 60 до 70
# F: Оцінка нижче 60

# Оскільки кожна буквена оцінка має відображатися в діапазоні балів, 
# ви не можете легко використовувати лише словник для відображення. 
# У pandas є метод Series.map(), який дозволяє застосовувати довільну 
# функцію до значень у Series. 

# Розрахунок літерної оцінки
# Створюємо словник, який зберігає відображення між нижньою межею 
# оцінки кожної літери та літерою. 
# Визначаємо grade_mapping(), який приймає як аргумент значення рядка 
# з серії максимальних балів. При перегляді елементів в оцінках, 
# порівнюються значення з ключем зі словника. 
# Якщо значення більше за ключ, повертається відповідна буквена оцінка.

# Можна написати відповідну функцію таким чином:

grades = {
    90: "A",
    80: "B",
    70: "C",
    60: "D",
    0: "F",
}


def grade_mapping(value):
    """Map numerical grade to letter grade."""
    for key, letter in grades.items():
        if value >= key:
            return letter

# Визначивши grade_mapping(), можна використовувати Series.map(), 
# щоб знайти літерні оцінки:

letter_grades = final_data["Ceiling Score"].map(grade_mapping)

# У цьому коді створюється нова серія letter_grades, 
# шо відображає grade_mapping() у стовпці Ceiling Score із final_data. 
# Оскільки є п’ять варіантів літерної оцінки, має сенс, 
# щоб це був категорійний тип даних. 

# Можна також створити категорійний стовпець за допомогою класу pandas 
# Categorical,  передаючи літерні оцінки, а також два ключових аргументи: 
# letter_grades та categories=grades.values(). 
# ordered = True говорить що категорії впорядковані. 

final_data["Final Grade"] = pd.Categorical(
    letter_grades, categories=grades.values(), ordered=True
)

# print(final_data)
# exit()

# Email Address  Section  ... Ceiling Score Final Grade
# wxb12345  woody.barrera_jr@univ.edu        1  ...          75.0           C

# [150 rows x 47 columns]

# Групування даних
# pandas має потужні можливості для групування та сортування даних у DataFrames. 
# Згрупувати дані за номером секції студентів і відсортувати 
# згрупований результат за їхніми іменами можна за допомогою коду:

for section, table in final_data.groupby("Section"):
    section_file = DATA_FOLDER / f"Section {section} Grades.csv"
    num_students = table.shape[0]
    print(
        f"In Section {section} there are {num_students} students saved to "
        f"file {section_file}."
    )
    # Нарешті, зберігаємо відсортовані дані у файлі CSV.
    table.sort_values(by=["Last Name", "First Name"]).to_csv(section_file)

# DataFrame final_data.groupby() використовується для групування 
# за стовпцем Section і DataFrame.sort_values() для сортування 
# згрупованих результатів. 


# Використовуючи pandas і Matplotlib, можна побудувати підсумкову статистику, 
# наприклад розподіл літерних оцінок у класі:

grade_counts = final_data["Final Grade"].value_counts().sort_index()

# print(grade_counts)
# exit()

# In Section 1 there are 56 students saved to file /home/janus/projects/python3-fundamental/unit_18/src/quiz/data/Section 1 Grades.csv.
# In Section 2 there are 51 students saved to file /home/janus/projects/python3-fundamental/unit_18/src/quiz/data/Section 2 Grades.csv.
# In Section 3 there are 43 students saved to file /home/janus/projects/python3-fundamental/unit_18/src/quiz/data/Section 3 Grades.csv.
# Final Grade
# A      0
# B     42
# C    102
# D      6
# F      0
# Name: count, dtype: int64

# Тут використовується Series final_data.value_counts() у стовпці «Final Grade», 
# щоб обчислити, скільки з’являється кожна літера. 
# За замовчуванням кількість значень відсортовано від найбільшої до найменшої. 
# Series.sort_index() використовується для сортування оцінок у порядку, 
# вказаному під час визначення стовпця Categorical.
# Потім використовується Matplotlib для створення діаграми оцінок 
# за допомогою DataFrame.plot.bar(). 

grade_counts.plot.bar()

# Matplotlib показкє графік за допомогою plt.show().

plt.show()

# Гістограма - це один із способів оцінити розподіл даних.

# Висота стовпчиків відображає кількість студентів, 
# які отримали кожну буквену оцінку, яка показана на горизонтальній осі. 

# pandas може використовувати Matplotlib з DataFrame.plot.hist(), 
# щоб переглянути гістограму числових балів студентів автоматично:

# Тут використовується DataFrame.plot.hist() для побудови гістограми остаточних 
# результатів. Будь-які аргументи ключових слів передаються до Matplotlib 
# після завершення побудови.
final_data["Final Score"].plot.hist(bins=20, label="Histogram")


# Pandas може використовувати бібліотеку SciPy для розрахунку 
# оцінки щільності ядра за допомогою DataFrame.plot.density(). 
# Можна припустити, що дані матимуть нормальний розподіл, 
# і обчислити нормальний розподіл із середнім значенням 
# і стандартним відхиленням від даних. 
# Використовуємо DataFrame.plot.density(), щоб побудувати графік 
# оцінки щільності ядра для даних:

final_data["Final Score"].plot.density(
    linewidth=4, label="Kernel Density Estimate"
)

# Обчислюємо середнє значення та стандартне відхилення даних остаточної оцінки 
# за допомогою DataFrame.mean() і DataFrame.std(). 

final_mean = final_data["Final Score"].mean()
final_std = final_data["Final Score"].std()

# Використовуємо np.linspace(), щоб створити набір значень x від -5 до +5 
# стандартних відхилень від середнього. 

x = np.linspace(final_mean - 5 * final_std, final_mean + 5 * final_std, 200)

# Обчислюємо нормальний розподіл у normal_dist, підключаючись до формули 
# для стандартного нормального розподілу.

normal_dist = scipy.stats.norm.pdf(x, loc=final_mean, scale=final_std)

# Будуємо графік x проти normal_dist, регулюючи ширину лінії та додаємо мітку. 
plt.plot(x, normal_dist, label="Normal Distribution", linewidth=4)
plt.legend()
plt.show()
