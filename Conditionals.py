def classify(grade):
    if grade >= 0 and grade < 70:
        print('Calificación reprobatoria')
    elif grade >= 70 and grade < 90:
        print('Tienes una calificación aprobatoria')
    elif grade >= 90 and grade <= 100:
        print('¡Muy buena calificación!')
    else:
        print('Calificación no válida')


if __name__ == '__main__':
    grade = float(input('Ingrese su calificación: '))

    classify(grade)