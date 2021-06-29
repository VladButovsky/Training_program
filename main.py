# my_exercises = []
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

# easy_shoulders = shoulders//100*50
# heavy_lat_pull_down_machine = lat_pull_down_machine//100*85
#
# medium_close_grip_bench_press = close_grip_bench_press//100*70
#
# heavy_bent_over_row = bent_over_row//100*85
#
# easy_lifting_biceps = lifting_biceps//100*50
#
# heavy_standing_chest_press = standing_chest_press//100*85
#
# easy_day_squats = max_squats//100*50
# medium_day_squats = max_squats//100*70
# heavy_day_squats = max_squats//100*85
#
# easy_day_chest_press = max_chest_press//100*50
# medium_day_chest_press = max_chest_press//100*70
# heavy_day_chest_press = max_chest_press//100*85




class ChestPress:
    def __init__(self, max_chest_press):
        self.weight = max_chest_press
        self.easy = int(max_chest_press / 100 * 50)
        self.med = int(max_chest_press / 100 * 70)
        self.heavy = int(max_chest_press / 100 * 85)
        easy = 0
        medium = 0
        hard = 0
        for week in range(1, 8):
            if week == 1:
                easy += 0
                medium += 0
                hard += 0
                self.easy = int(max_chest_press / 100 * 50 + easy)
                self.med = int(max_chest_press / 100 * 70 + medium)
                self.heavy = int(max_chest_press / 100 * 85 + hard)
                print('Жим лежа', 'легкая тренировка', self.easy, 'средняя тренировка', self.med,
                      'тяжелая тренировка', self.heavy)

            elif week == 2:
                easy += 5
                medium += 2
                hard += 7
                self.easy = int(max_chest_press / 100 * 50 + easy)
                self.med = int(max_chest_press / 100 * 70 + medium)
                self.heavy = int(max_chest_press / 100 * 85 + hard)
                print('Жим лежа', 'легкая тренировка', self.easy, 'средняя тренировка', self.med,
                      'тяжелая тренировка', self.heavy)

            elif week == 3:
                easy += 5
                medium =+ 2
                hard += 8
                self.easy = int(max_chest_press / 100 * 50 + easy)
                self.med = int(max_chest_press / 100 * 70 + medium)
                self.heavy = int(max_chest_press / 100 * 85 + hard)
                print('Жим лежа', 'легкая тренировка', self.easy, 'средняя тренировка', self.med,
                      'тяжелая тренировка', self.heavy)

            elif week == 4:
                easy += 2
                medium += 2
                hard += 2
                self.easy = int(max_chest_press / 100 * 50 + easy)
                self.med = int(max_chest_press / 100 * 70 + medium)
                self.heavy = int(max_chest_press / 100 * 85 + hard)
                print('Жим лежа', 'легкая тренировка', self.easy, 'средняя тренировка', self.med,
                      'тяжелая тренировка', self.heavy)

            elif week >= 5:
                easy += 2
                medium += 2
                hard += 2
                self.easy = int(max_chest_press / 100 * 50 + easy)
                self.med = int(max_chest_press / 100 * 70 + medium)
                self.heavy = int(max_chest_press / 100 * 85 + hard)
                print('Жим лежа', 'легкая тренировка', self.easy, 'средняя тренировка', self.med,
                           'тяжелая тренировка', self.heavy)





press_chest_program = ChestPress(80)
