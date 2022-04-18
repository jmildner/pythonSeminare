from tools import mytools as mt


def main():
    mt.h1("Übung 7.7 - Tupel")

    mt.h1("erstellen")

    student = ("max", "meier", 22, "informatik", 1234711)
    print(student)

    mt.h1("entpacken")
    first_name, last_name, age, subject, mat_nr = student
    print(first_name, last_name, age, subject, mat_nr)

    mt.h1("erweitern (konvertieren und rückkonvertieren")

    student_list = list(student)
    print(student_list)
    student_list.append("wien")
    student = tuple(student_list)
    print(student)
    first_name, last_name, age, subject, mat_nr, ort = student
    print(first_name, last_name, age, subject, mat_nr, ort)

    student2 = (first_name, last_name, age, subject, mat_nr, ort)
    student3 = [first_name, last_name, age, subject, mat_nr, ort]
    print(student2)
    print(student3)

    mt.end(__name__)


if __name__ == "__main__":
    main()
