max_chest_press = int(input('Введите ваш жим с груди'))
max_squats = int(input('Введите присед'))
standing_chest_press = int(input('Ведите жим с груди стоя'))
lifting_biceps = int(input('Ведите подъем на бицепс штанги'))
bent_over_row = int(input('Ведите тягу штанги в наклоне '))
close_grip_bench_press = int(input('Ведите жим лежа узким хватом '))
lat_pull_down_machine = int(input('Ведите вашу тягу в вертикальном блоке '))
max_romanian_lift = int(input('Ведите вашу румынскую тягу'))
shoulders = int(input('Ведите вес гантелей для упражения махи плечами'))
easy_max_romanian_lift = int(input('Ведите вашу румынскую тягу'))

easy_shoulders = shoulders//100*50
heavy_lat_pull_down_machine = lat_pull_down_machine//100*85

medium_close_grip_bench_press = close_grip_bench_press//100*70

heavy_bent_over_row = bent_over_row//100*85

easy_lifting_biceps = lifting_biceps//100*50

heavy_standing_chest_press = standing_chest_press//100*85

easy_day_squats = max_squats//100*50
medium_day_squats = max_squats//100*70
heavy_day_squats = max_squats//100*85

easy_day_chest_press = max_chest_press//100*50
medium_day_chest_press = max_chest_press//100*70
heavy_day_chest_press = max_chest_press//100*85

