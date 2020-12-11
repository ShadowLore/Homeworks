fruit_evaluation= [
    ['Яблоко', '5', '4', '5', '3', '4', '5'],
    ['Финоград', '4', '3', '4', '5', '5', '5'],
    ['Дыня', '5', '5', '4', '5', '3', '4'],
    ['Арбуз', '4', '4', '3', '5', '5', '4'],
    ['Киви', '4', '3', '5', '5', '4', '4'],
    ['Ананас', '4', '3', '4', '5', '4', '5']
]
def show_assessment(assessment_record):
    marks = assessment_record[1:]
    marks_as_int = []
    for mark in marks:
        mark = int(mark)
        marks_as_int.append(mark)


    marks_avg = sum(marks_as_int) / len(marks_as_int)
    marks_as_str = ', '.join(marks)
    print(f'{assessment_record[0]}: {marks_as_str}, средняя оценка {marks_avg}')


for record in fruit_evaluation:
    show_assessment(record)
