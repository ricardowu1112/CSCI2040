def isint(n):
    return int(n) == n


def get_average_grades(filename='grades.csv'):
    average_grades_list = []
    with open(filename) as f:
        a = f.readlines()
        a = [x.rstrip('\n').split(',') for x in a]
        '''
        a is nested list with sublists in string type
        '''

        '''
        zip(*a) is all element with same position index in sublists of a
        e.g. [(a1,a2,a3,a4),(),()]
        '''
        for x in range(len(list(zip(*a)))):
            length = len(list(zip(*a))[x])
            average_grades_list.append('0')

            '''
            add str(0) before assign so that can evaluate string operation 
            '''
            for num in list(zip(*a))[x]:
                if float(num) != -1:
                    average_grades_listx = average_grades_list[x]
                    average_grades_list[x] = num + '+' + average_grades_listx
                else:
                    length -= 1
            '''
            now average_grades_list[x] contains operation in string e.g.['0+60+80','0+61+70',...]
            length is length without counting -1
            '''
            print(average_grades_list[x])
            average_grades_list[x] = eval(average_grades_list[x]) / length
        for index in range(len(average_grades_list)):
            if isint(average_grades_list[index]):
                average_grades_list[index] = int(average_grades_list[index])
                '''
                if float num can be expressed in int, then do it e.g. turn 75.0 to 75
                '''

    return average_grades_list
