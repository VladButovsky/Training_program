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

class TrainingCalculator:
    def __init__(self, Exercises):
        self.weight = Exercises
        self.easy = int(Exercises / 100 * 50)
        self.med = int(Exercises / 100 * 70)
        self.heavy = int(Exercises / 100 * 85)
        easy = 0
        medium = 0
        hard = 0
        for week in range(1, 8):
            if week == 1:
                easy += 0
                medium += 0
                hard += 0
                self.easy = int(Exercises / 100 * 50 + easy)
                self.med = int(Exercises / 100 * 70 + medium)
                self.heavy = int(Exercises / 100 * 85 + hard)
                print('легкая тренировка', self.easy, 'средняя тренировка', self.med,
                      'тяжелая тренировка', self.heavy)

            elif week == 2:
                easy += 5
                medium += 2
                hard += 7
                self.easy = int(Exercises / 100 * 50 + easy)
                self.med = int(Exercises / 100 * 70 + medium)
                self.heavy = int(Exercises / 100 * 85 + hard)
                print('легкая тренировка', self.easy, 'средняя тренировка', self.med,
                      'тяжелая тренировка', self.heavy)

            elif week == 3:
                easy += 5
                medium =+ 2
                hard += 8
                self.easy = int(Exercises / 100 * 50 + easy)
                self.med = int(Exercises / 100 * 70 + medium)
                self.heavy = int(Exercises / 100 * 85 + hard)
                print('легкая тренировка', self.easy, 'средняя тренировка', self.med,
                      'тяжелая тренировка', self.heavy)

            elif week == 4:
                easy += 2
                medium += 2
                hard += 2
                self.easy = int(Exercises / 100 * 50 + easy)
                self.med = int(Exercises / 100 * 70 + medium)
                self.heavy = int(Exercises / 100 * 85 + hard)
                print('легкая тренировка', self.easy, 'средняя тренировка', self.med,
                      'тяжелая тренировка', self.heavy)

            elif week >= 5:
                easy += 2
                medium += 2
                hard += 2
                self.easy = int(Exercises / 100 * 50 + easy)
                self.med = int(Exercises / 100 * 70 + medium)
                self.heavy = int(Exercises / 100 * 85 + hard)
                print('легкая тренировка', self.easy, 'средняя тренировка', self.med,
                           'тяжелая тренировка', self.heavy)


class Exercises:
    def __init__(self,max_press):
        self.weight = max_press
        self.easy = 0
        self.med = 0
        self.heavy = 0

        TrainingCalculator(self.weight)




press_chest_program = Exercises(max_press=80)


class Week:
    def __init__(self):




# max_chest_press = ChestPress(80)
# max_squats = TrainingCalculator(80)
# standing_chest_press = TrainingCalculator(80)
# lifting_biceps = TrainingCalculator(80)
# bent_over_row = TrainingCalculator(80)
# close_grip_bench_press = TrainingCalculator(80)
# lat_pull_down_machine = TrainingCalculator(80)
# max_romanian_lift = TrainingCalculator(80)
# shoulders = TrainingCalculator(80)

