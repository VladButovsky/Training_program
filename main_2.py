# max_chest_press = (int(input('Введите ваш жим с груди')))
# max_squats = int(input('Введите присед'))
# standing_chest_press = int(input('Ведите жим с груди стоя'))
# lifting_biceps = int(input('Ведите подъем на бицепс штанги'))
# bent_over_row = int(input('Ведите тягу штанги в наклоне '))
# close_grip_bench_press = int(input('Ведите жим лежа узким хватом '))
# lat_pull_down_machine = int(input('Ведите вашу тягу в вертикальном блоке '))
# max_romanian_lift = int(input('Ведите вашу румынскую тягу'))
# shoulders = int(input('Ведите вес гантелей для упражения махи плечами'))
# max_romanian_lift = int(input('Ведите вашу румынскую тягу'))


chest_press_list = []


class TrainingCalculator:
    def __init__(self, max_chest_press):
        self.weight = max_chest_press
        self.easy = int(self.weight / 100 * 50)
        self.med = int(self.weight / 100 * 70)
        self.heavy = int(self.weight / 100 * 85)
        easy = 0
        medium = 0
        hard = 0
        for week in range(0, 9):
            if week == 1:
                easy += 0
                medium += 0
                hard += 0
                self.easy += easy
                chest_press_list.append(self.easy)
                self.med += medium
                chest_press_list.append(self.med)
                self.heavy += hard
                chest_press_list.append(self.heavy)
                chest_press_list.append('-')
            elif week == 2:
                easy += 5
                medium += 2
                hard += 7
                self.easy = int(self.weight / 100 * 50 + easy)
                chest_press_list.append(self.easy)
                self.med = int(self.weight / 100 * 70 + medium)
                chest_press_list.append(self.med)
                self.heavy = int(self.weight / 100 * 85 + hard)
                chest_press_list.append(self.heavy)
                chest_press_list.append('-')
            elif week == 3:
                easy += 5
                medium += 2
                hard += 8
                self.easy = int(self.weight / 100 * 50 + easy)
                chest_press_list.append(self.easy)
                self.med = int(self.weight / 100 * 70 + medium)
                chest_press_list.append(self.med)
                self.heavy = int(self.weight / 100 * 85 + hard)
                chest_press_list.append(self.heavy)
                chest_press_list.append('-')
            elif week >= 4:
                easy += 2
                medium += 2
                hard += 2
                self.easy = int(self.weight / 100 * 50 + easy)
                chest_press_list.append(self.easy)
                self.med = int(self.weight / 100 * 70 + medium)
                chest_press_list.append(self.med)
                self.heavy = int(self.weight / 100 * 85 + hard)
                chest_press_list.append(self.heavy)
                chest_press_list.append('-')
            # print('Неделя {} Легкая тренировка {}. Средняя тренировка {}.Тяжелая тренировка {}'.format(week,self.easy, self.med,
            #                                                                                  self.heavy))


squat_list = []


class Squat:
    def __init__(self, max_squats):
        self.weight = max_squats
        self.easy = int(self.weight / 100 * 50)
        self.med = int(self.weight / 100 * 70)
        self.heavy = int(self.weight / 100 * 85)
        easy = 0
        medium = 0
        hard = 0
        for week in range(0, 9):
            if week == 1:
                easy += 0
                medium += 0
                hard += 0
                self.easy += easy
                squat_list.append(self.easy)
                self.med += medium
                squat_list.append(self.med)
                self.heavy += hard
                squat_list.append(self.heavy)
                squat_list.append('-')
            elif week == 2:
                easy += 5
                medium += 2
                hard += 7
                self.easy = int(self.weight / 100 * 50 + easy)
                squat_list.append(self.easy)
                self.med = int(self.weight / 100 * 70 + medium)
                squat_list.append(self.med)
                self.heavy = int(self.weight / 100 * 85 + hard)
                squat_list.append(self.heavy)
                squat_list.append('-')
            elif week == 3:
                easy += 5
                medium += 2
                hard += 8
                self.easy = int(self.weight / 100 * 50 + easy)
                squat_list.append(self.easy)
                self.med = int(self.weight / 100 * 70 + medium)
                squat_list.append(self.med)
                self.heavy = int(self.weight / 100 * 85 + hard)
                squat_list.append(self.heavy)
                squat_list.append('-')
            elif week >= 4:
                easy += 2
                medium += 2
                hard += 2
                self.easy = int(self.weight / 100 * 50 + easy)
                squat_list.append(self.easy)
                self.med = int(self.weight / 100 * 70 + medium)
                squat_list.append(self.med)
                self.heavy = int(self.weight / 100 * 85 + hard)
                squat_list.append(self.heavy)
                squat_list.append('-')
            # print('Неделя {} Легкая тренировка {}. Средняя тренировка {}.Тяжелая тренировка {}'.format(week, self.easy,
            #                                                                                            self.med,
            #                                                                                            self.heavy))


press_chest_program = TrainingCalculator(max_chest_press=80)
squat_program = Squat(max_squats=90)
print('chest press', chest_press_list)
print('squad', squat_list)


class TrainingProgramPrinter:
    def print_program(self, chest_press_list,squat_list):
        print('1 неделя \nДень 1 \nЖим лежа. Вес:', chest_press_list[0], 'кг. 4х12\nПрисед. Вес:',squat_list[2],'кг. 3х8')


# print('1 тернировка, 1 неделя, \n 1 - жим, 4х12', chest_press_list[0])
week_1 = TrainingProgramPrinter()
week_1.print_program(chest_press_list,squat_list)
