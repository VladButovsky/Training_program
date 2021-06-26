# my_exercises = []
# max_chest_press = my_exercises.append(int(input('Введите ваш жим с груди')))
# max_squats = int(input('Введите присед'))
# standing_chest_press = int(input('Ведите жим с груди стоя'))
# lifting_biceps = int(input('Ведите подъем на бицепс штанги'))
# bent_over_row = int(input('Ведите тягу штанги в наклоне '))
# close_grip_bench_press = int(input('Ведите жим лежа узким хватом '))
# lat_pull_down_machine = int(input('Ведите вашу тягу в вертикальном блоке '))
# max_romanian_lift = int(input('Ведите вашу румынскую тягу'))
# shoulders = int(input('Ведите вес гантелей для упражения махи плечами'))
# easy_max_romanian_lift = int(input('Ведите вашу румынскую тягу'))

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


# print(my_exercises)
# easy_load = []
# for week, weight in enumerate(my_exercises):
#     week = 1
#
#     ('неделя',week, 'вес жима',int(weight / 100 * 50))

class ChestPress:
    def __init__(self,max_chest_press):
        self.weight = max_chest_press
        self.easy = int(max_chest_press / 100 * 50)
        self.med = int(max_chest_press / 100 * 70)
        self.heavy = int(max_chest_press / 100 * 85)
        i = 0
        for weight in range(1,8):
            self.easy = int(max_chest_press / 100 * 50+i)
            self.med = int(max_chest_press / 100 * 70+i)
            self.heavy = int(max_chest_press / 100 * 85+i)
            result = print('Жим лежа', 'легкая тренировка',self.easy,'средняя тренировка',self.med,'тяжелая тренировка',self.heavy)
            i += 10

        return result

press_chest_program = ChestPress(120)