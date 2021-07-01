# max_chest_press = (int(input('Введите ваш жим с груди')))
# max_squats = int(input('Введите присед'))
# max_standing_chest_press = int(input('Ведите жим с груди стоя'))
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
        for week in range(1, 9):
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
        for week in range(1, 9):
            if week == 1:
                squat_list.append(self.easy)
                squat_list.append(self.med)
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


standing_chest_press_list = []


class StandingChestPress:
    def __init__(self, max_standing_chest_press):
        self.weight = max_standing_chest_press
        self.easy = int(self.weight / 100 * 50)
        self.med = int(self.weight / 100 * 70)
        self.heavy = int(self.weight / 100 * 85)
        easy = 0
        medium = 0
        hard = 0
        for week in range(1, 9):
            easy += .5
            medium += .5
            hard += .5
            self.easy += easy
            standing_chest_press_list.append(self.easy)
            self.med += medium
            standing_chest_press_list.append(self.med)
            self.heavy += hard
            standing_chest_press_list.append(self.heavy)
            standing_chest_press_list.append('-')

lifting_biceps_list = []

class LiftingBiceps:
    def __init__(self,max_lifting_biceps):
        self.weight = max_lifting_biceps
        self.easy = int(self.weight / 100 * 50)
        self.med = int(self.weight / 100 * 70)
        self.heavy = int(self.weight / 100 * 85)
        easy = 0
        medium = 0
        hard = 0
        for week in range(1, 9):
            easy += .5
            medium += .5
            hard += .5
            self.easy += easy
            lifting_biceps_list.append(self.easy)
            self.med += medium
            lifting_biceps_list.append(self.med)
            self.heavy += hard
            lifting_biceps_list.append(self.heavy)
            lifting_biceps_list.append('-')

incline_bench_press_list = []

class InclineBenchPress:
    def __init__(self, max_incline_bench_press):
        self.weight = max_incline_bench_press
        self.easy = int(self.weight / 100 * 50)
        self.med = int(self.weight / 100 * 70)
        self.heavy = int(self.weight / 100 * 85)
        easy = 0
        medium = 0
        hard = 0
        for week in range(1, 9):
            easy += .5
            medium += .5
            hard += .5
            self.easy += easy
            incline_bench_press_list.append(self.easy)
            self.med += medium
            incline_bench_press_list.append(self.med)
            self.heavy += hard
            incline_bench_press_list.append(self.heavy)
            incline_bench_press_list.append('-')


side_delts_list = []

class SideDelts:
    def __init__(self, max_side_delts_program):
        self.weight = max_side_delts_program
        self.easy = int(self.weight / 100 * 50)
        self.med = int(self.weight / 100 * 70)
        self.heavy = int(self.weight / 100 * 85)
        easy = 0
        medium = 0
        hard = 0
        for week in range(1, 9):
                easy += .5
                medium += .5
                hard += .5
                self.easy = int(self.weight / 100 * 50 + easy)
                side_delts_list.append(self.easy)
                self.med = int(self.weight / 100 * 70 + medium)
                side_delts_list.append(self.med)
                self.heavy = int(self.weight / 100 * 85 + hard)
                side_delts_list.append(self.heavy)
                side_delts_list.append('-')

romanian_lift_list = []

class RomanianLift:
    def __init__(self, max_romanian_lift):
        self.weight = max_romanian_lift
        self.easy = int(self.weight / 100 * 50)
        self.med = int(self.weight / 100 * 70)
        self.heavy = int(self.weight / 100 * 85)
        easy = 0
        medium = 0
        hard = 0
        for week in range(1, 9):
            if week == 1:
                romanian_lift_list.append(self.easy)
                romanian_lift_list.append(self.med)
                romanian_lift_list.append(self.heavy)
                romanian_lift_list.append('-')
            elif week == 2:
                easy += 5
                medium += 2
                hard += 7
                self.easy = int(self.weight / 100 * 50 + easy)
                romanian_lift_list.append(self.easy)
                self.med = int(self.weight / 100 * 70 + medium)
                romanian_lift_list.append(self.med)
                self.heavy = int(self.weight / 100 * 85 + hard)
                romanian_lift_list.append(self.heavy)
                romanian_lift_list.append('-')
            elif week == 3:
                easy += 5
                medium += 2
                hard += 8
                self.easy = int(self.weight / 100 * 50 + easy)
                romanian_lift_list.append(self.easy)
                self.med = int(self.weight / 100 * 70 + medium)
                romanian_lift_list.append(self.med)
                self.heavy = int(self.weight / 100 * 85 + hard)
                romanian_lift_list.append(self.heavy)
                romanian_lift_list.append('-')
            elif week >= 4:
                easy += 2
                medium += 2
                hard += 2
                self.easy = int(self.weight / 100 * 50 + easy)
                romanian_lift_list.append(self.easy)
                self.med = int(self.weight / 100 * 70 + medium)
                romanian_lift_list.append(self.med)
                self.heavy = int(self.weight / 100 * 85 + hard)
                romanian_lift_list.append(self.heavy)
                romanian_lift_list.append('-')


max_lifting_biceps = LiftingBiceps(max_lifting_biceps=25)
press_chest_program = TrainingCalculator(max_chest_press=80)
squat_program = Squat(max_squats=90)
standing_chest_press_program = StandingChestPress(max_standing_chest_press=35)
incline_bench_press_program = InclineBenchPress(max_incline_bench_press=45)
max_side_delts_program = SideDelts(max_side_delts_program=5)
max_romanian_lift_program = RomanianLift(max_romanian_lift=70)

print('chest press', chest_press_list)
print('squad', squat_list)
print('standing chest press', standing_chest_press_list)
print('lifting biceps', lifting_biceps_list)
print('incline_bench_press',incline_bench_press_list)
print('side delts',side_delts_list)
print('romanian lift',romanian_lift_list)

class TrainingProgramPrinter:
    def print_program(self, chest_press_list, squat_list, standing_chest_press_list, incline_bench_press_list,
                      side_delts_list,lifting_biceps_list,romanian_lift_list):
        i = 0
        for week in range(1, 9):
            print(week, 'неделя '
                    '\nДень 1 '
                    '\nЖим лежа. Вес:', chest_press_list[1 + i], 'кг. 4х12'
                    '\nПрисед со штангой. Вес:', squat_list[2 + i], 'кг. 3х8'
                    '\nЖим штанги на наклонной скамье. Вес:', incline_bench_press_list[1 + i], 'кг. 3х10'                                    
                    '\nРазведение плеч в стороны с гантелями. Вес:', side_delts_list[0 + i], 'кг. 4х20'
                    '\nГоризонтальная тяга блока в тренажере. Вес: 90ф 4х15',
                    '\nПодъем штанги на бицепс. Вес:', lifting_biceps_list[1+i],'кг. 3х10'
                    '\nПресс. Скручивния 2 подхода на максимум\n\n'
                    
                    'День 2'
                    '\nЖим лежа. Вес:', chest_press_list[0 + i], 'кг. 4х12'
                    '\nЖим стоя. Вес:', standing_chest_press_list[1 + i],'кг. 3х8'
                    '\nЖим лежа. Вес:', chest_press_list[1 + i], 'кг. 3х10'
                    '\nРумынская тяга. Вес:',romanian_lift_list[2 + i],'кг. 3х10' 
                    '\nРазведение плеч в стороны с гантелями. Вес:', side_delts_list[0 + i], 'кг. 4х20'
                    '\nПресс. Скручивния 2 подхода на максимум\n\n'

                    '\nПрисед со штангой. Вес:',squat_list[0 + i], 'кг. 4х12'
                    '\nЖим лежа. Вес:', chest_press_list[2 + i],'кг. 4х8'
                    '\nЖим лежа. Вес:', chest_press_list[0 + i], 'кг. 3х10'
                    '\nВертикальная тяга блока'
                    '\nРазгибание ног в тренажере'
                    '\nРазведение плеч в стороны с гантелями. Вес:', side_delts_list[0 + i], 'кг. 4х20'
                    '\nПресс. Скручивния 2 подхода на максимум\n\n'
                  )



            i += 4


week_1 = TrainingProgramPrinter()
week_1.print_program(chest_press_list, squat_list, standing_chest_press_list, incline_bench_press_list,
                      side_delts_list,lifting_biceps_list,romanian_lift_list)
