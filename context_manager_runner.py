from different_classes.class1 import Student


def main():
    with Student(name='Javier', age=23, number_brothers=2) as stdnt:
        print('Name: %s\nAge: %i\nBrothers: %i' % (stdnt.name, stdnt.age, stdnt.number_brothers))


if __name__ == '__main__':
    main()
