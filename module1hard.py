#Базовые структуры данных
#coded by f1ibustier

grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = list(students)
students.sort()
sr_ball_0 = sum(grades[0])/len(grades[0])
sr_ball_1 = sum(grades[1])/len(grades[1])
sr_ball_2 = sum(grades[2])/len(grades[2])
sr_ball_3 = sum(grades[3])/len(grades[3])
sr_ball_4 = sum(grades[4])/len(grades[4])
yspevaemost = {students[0]: sr_ball_0, students[1]: sr_ball_1, students[2]: sr_ball_2, students[3]: sr_ball_3, students[4]: sr_ball_4}
print(yspevaemost)
