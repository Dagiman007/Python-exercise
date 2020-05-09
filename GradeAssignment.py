def main():
    scores = input('Enter scores: ').split()
    scores = [eval(x) for x in scores]

    grades = grade(scores)

    for i in range(len(scores)):
        print('Student {0} score is {1} and grade is {2}'.format(i, scores[i], grades[i]))


def grade(scores):
    best = scores[0]
    bestIndex = 0
    for i in range(1, len(scores)):
        if best < scores[i]:
            best = scores[i]
            bestIndex = i

    grades = []
    for i in range(len(scores)):
        if i == bestIndex:
            pass
        if scores[i] >= best - 10:
            grades.append('A')
        elif scores[i] >= best - 20:
            grades.append('B')
        elif scores[i] >= best - 30:
            grades.append('C')
        elif scores[i] >= best - 40:
            grades.append('D')
        else:
            grades.append('F')

    return grades

main()
                  
    
              
