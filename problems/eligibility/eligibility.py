n = int(input())
for i in range(n):
    name, studies_start, birthday, courses = input().split()

    courses = int(courses)
    studies_start = studies_start.split('/')
    birthday = birthday.split('/')

    if int(studies_start[0]) >= 2010:
        print(name, 'eligible')
    elif int(birthday[0]) >= 1991:
        print(name, 'eligible')
    elif courses >= 41:
        print(name, 'ineligible')
    else:
        print(name, 'coach petitions')
    