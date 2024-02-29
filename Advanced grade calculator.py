a = int(input('>> Enter number of subjects: '))
grades = []
for i in range(1, a+1):
    grade = int(input(f'Enter the grade for subject {i}: '))
    if 0 <=grade<=100:
        grades.append(grade)
    else:
        print('Enter a valid grade(0 - 100)')
        break
print("Average grade: ", sum(grades)/a) 
print('Highest grade: ', max(grades))
print('Lowest grade :', min(grades))

    
b = input('>> Do you want to see the grade distribution (y/n): ')
if b == 'y':
    A = []
    B = []
    C = []
    D = []
    F = []

    for i in grades:
        if 90<=i<=100:
            print('A (90 - 100): ', len(A))
            A.append(i)
        elif 80<=i<89:
            print('B (80 - 89): ', len(B))
            B.append(i)
        elif 70<=i<79:
            print('C (70 - 79): ', len(C))
            C.append(i)
        elif 60<=i<69:
            print('D (60 - 69): ', len(D))
            D.append(i)
        else:
            print('F (0 - 59): ', len(F))
            F.append(i)
elif b == 'n':
    print('Exiting advanced grade calculator .Thank you!!')
else:
    print('Enter valid response!')
    
    