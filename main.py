import telebot
from telebot import types
bot = telebot.TeleBot('5643632753:AAFotFUi-rmwqHra0b2MUc5V2E9mJ8kbsm4')

# Выберать машыну которий хотич узнать характеристики
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=False)
    item1 = types.KeyboardButton('Audi')
    item2 = types.KeyboardButton('Bmw')
    item3 = types.KeyboardButton('Mercedes')
    item5 = types.KeyboardButton('Интересний факт')
    markup.add(item1, item2, item3, item5)
    bot.send_message(message.chat.id, 'Привет. Тут я тебе раскажу про характерстики автомобили.Какую марку ты выберешь?', reply_markup=markup)


# Выбераем модель
@bot.message_handler(content_types=['text'])
def cars_choice(message):
    if message.chat.type == 'private':
        if message.text == 'Audi':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            types_cars1 = types.KeyboardButton('A1')
            types_cars2 = types.KeyboardButton('A3')
            types_cars3 = types.KeyboardButton('A4')
            types_cars4 = types.KeyboardButton('A5')
            types_cars5 = types.KeyboardButton('A7')
            types_cars6 = types.KeyboardButton('A8')
            item4 = types.KeyboardButton('Назад')
            item5 = types.KeyboardButton('Интересний факт')
            markup.add(types_cars1, types_cars2, types_cars3, types_cars4, types_cars5, types_cars6, item4, item5)

            bot.send_message(message.chat.id, 'Выберайте модель Audi', reply_markup=markup)

        elif message.text == 'Bmw':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            types_cars1 = types.KeyboardButton('M1')
            types_cars2 = types.KeyboardButton('M3')
            types_cars3 = types.KeyboardButton('M5')
            types_cars4 = types.KeyboardButton('M6')
            types_cars5 = types.KeyboardButton('X1')
            types_cars6 = types.KeyboardButton('X2')
            item4 = types.KeyboardButton('Назад')
            item5 = types.KeyboardButton('Интересний факт')
            markup.add(types_cars1, types_cars2, types_cars3, types_cars4, types_cars5, types_cars6, item4, item5)

            bot.send_message(message.chat.id, 'Выберайте модель Bmw', reply_markup=markup)

        elif message.text == 'Mercedes':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            types_cars1 = types.KeyboardButton('W163')
            types_cars2 = types.KeyboardButton('W164')
            types_cars3 = types.KeyboardButton('W220')
            types_cars4 = types.KeyboardButton('W221')
            types_cars5 = types.KeyboardButton('W222')
            types_cars6 = types.KeyboardButton('W223 ')
            item4 = types.KeyboardButton('Назад')
            item5 = types.KeyboardButton('Интересний факт')
            markup.add(types_cars1, types_cars2, types_cars3, types_cars4, types_cars5, types_cars6, item4, item5)

            bot.send_message(message.chat.id, 'Выберайте модель Mercedes', reply_markup=markup)

    # характеристики данной модели Audi

    if message.text == 'A1':
        bot.send_message(message.chat.id, 'Audi A1 производится на той же платформе PQ25, что Volkswagen Polo V и Seat Ibiza IV[9].'
                                          'Все модели серии A1 за исключением 1.4 TFSI 185 л. с. и 1.6 TDI S tronic 90 л. с. стандартно оснащаются системой Start-stop и системой рекуперации, позволяющими снизить расход топлива[10].')
    elif message.text == 'A2':
        bot.send_message(message.chat.id, 'Вместе со стандартной моделью была представлена версия с улучшенным коэффициентом аэродинамического сопротивления и низким расходом топлива — A2 3L. На такую модель устанавливался дизельный двигатель объёмом 1,2 литра и мощностью 45 кВт. Основной его особенностью является крайне низкий расход топлива, который составляет всего 2,99 л/100 км (отсюда и название данной модификации). Объём бака невелик — 20 литров. Запас хода модели составляет 669 км. Двигатель, как и кузов модели, сделан из алюминия,'
                                          ' его масса составляет всего 100 кг. Общая же масса A2 3L составляет 825 кг — на 70 кг меньше, чем у обычной модели.')
    elif message.text == 'A3':
        bot.send_message(message.chat.id, 'Audi A3 — хэтчбэк малого семейного класса, производимый концерном Audi с 1996 года[1][2]. В 1996—2003 годах выпускалось первое поколение, с 2003 по 2012 — второе, c 2013 по 2020 — третье, а в 2020 появилось 4 поколение (8Y) популярного в Европе компактного автомобиля[3], для российского рынка автомобиль 4-го поколения получил'
                                          ' 1.4-литровый турбомотр на 150 сил в паре с 8-диапазонной АКПП и передним приводом[4].')
    elif message.text == 'A4':
        bot.send_message(message.chat.id, 'Audi 80, с 1995 года Audi A4, представляет собой семейство моделей среднего класса, выпускаемых под маркой Audi. Внутреннее обозначение автомобилей этой серии — «тип В»[1].'
                                          'Audi 80 стал преемником серии Audi F103, модели которой — Audi 60, 75, 80 и Super 90— обозначались по числу лошадиных сил. Наименование Audi 80 стало использоваться для всего модельного ряда и в 1994 году было заменено на A4[2].')
    elif message.text == 'A5':
        bot.send_message(message.chat.id, 'Audi A5 — спортивный автомобиль (двухдверное купе на платформе Audi A4), производимый немецким aвтопроизводителем Audi с 2007 года на заводе в Ингольштадте. Audi A5 была одновременно представлена на Женевском автосалоне и Мельбурнском международном автосалоне 6 марта 2007 года[2]. Производитель позиционирует модель как автомобиль класса Гран туризмо, тем самым заявляя его как конкурента BMW E92 (купе BMW 3-серии) и Mercedes-Benz CLK-класс (ныне выпускается как Mercedes-Benz E-Class Coupe)[3].')
    elif message.text == 'A7':
        bot.send_message(message.chat.id, 'Audi A7 Sportback (код кузова — 4G) — пятидверный фастбэк класса Гран Туризмо, выпускаемый AUDI AG, на платформе А6, позиционируется в сегменте ниже Audi A8. Его основные конкуренты — Mercedes-Benz CLS и BMW 6 Gran Coupe. Федеральное автотранспортное ведомство ФРГ позиционирует A7 в верхнем сегменте среднего класса[1]. Спортивными версиями являются S7 и RS7.')
    elif message.text == 'A8':
        bot.send_message(message.chat.id, 'К началу продаж модели Audi A8 D3 в октябре 2002 года линейка двигателей включала три варианта 8-цилиндровых силовых агрегатов. На выбор предлагались 3,7 литровый двигатель 280 л .с., мощность которого по сравнению с предыдущей моделью увеличилась на 20 л.с., и 4,2-литровый агрегат мощностью 335 л. с., устанавливавшийся только в сочетании с полным приводом.')

    # характеристики данной модели Bmw
    elif message.text == 'M1':
        bot.send_message(message.chat.id, 'В конце 1970-х годов, итальянский производитель Lamborghini заключил соглашение с BMW на постройку и производство '
                                          'гоночных автомобилей в достаточном количестве для усовершенствования, но возник конфликт, что побудило BMW изготавливать \
                                          машины самой. BMW M1 был единственным средномоторным автомобилем BMW массового производства. Бензиновый двигатель с '
                                          'М88/1 — 3.5 л 6-цилиндровый с механическим впрыском топлива Kugelfischer. Версия этого мотора была позже использована в Южно-Африканской версии BMW 745i (209 экземпляров было построено в период между 1984 и 1986), а также Е24 BMW М6/M635CSi и БМВ М5 Е28.'
                                          ' Двигатель имел шесть отдельных дроссельных органов, четыре клапана на цилиндр и мощность 277 л. с. (204 кВт; 277 л. с.) в дорожном варианте, максимальная скорость 265 км/ч (165 миль/ч). Турбированные гоночные версии были способны производить около 850 л. с. (634 кВт).')
    elif message.text == 'M3':
        bot.send_message(message.chat.id, 'Первая версия для дорог общего пользования имела 195 л. с. (143 кВт). Модели Evolution имели 2,3 л двигатели, но изменённую выхлопную систему, увеличенное сжатие и небольшие доработки увеличили производительность до 215 л. с. (160 кВт). '
                                          'Позднее модель Sport Evolution получила 2,5 л двигатели, что увеличило мощность до 238 л. с. (175 кВт). Также было выпущено 786 кабриолетов.')
    elif message.text == 'M5':
        bot.send_message(message.chat.id, 'BMW M5 — доработанная подразделением BMW Motorsport версия автомобиля BMW пятой серии. Первое поколение было представлено в 1986 году. Последующие поколения M5 сменялись совместно с каждым поколением автомобилей пятой серии, включающей E34, E39, E60/61, F10. С началом производства модели'
                                          ' G30, после поступления первых заказов, с марта 2018 года началось также производство её M-версии.')
    elif message.text == 'M6':
        bot.send_message(message.chat.id, 'BMW M6 — высокотехнологичная версия BMW 6-ой серии, разработанная спортивным подразделением немецкого автопроизводителя BMW. Первое поколение было представлено в 1983 году. '
                                          'BMW M6 очень богата электроникой, имеет от 5 до 12 режимов передач.')
    elif message.text == 'X1':
        bot.send_message(message.chat.id, 'BMW X1 — компактный пятиместный кроссовер. Производство автомобиля началось на заводе в Лейпциге, Германия, в октябре 2009 года. Первое поколение было создано на платформе универсала BMW 3-й серии, отличалось шасси и электрогидравлическим усилителем руля. Второе поколение автомобилей стало переднеприводными, в дорогих комплектациях полноприводными.'
                                          ' Для китайского рынка выпущена удлиненная версия X1 L (с 4,454 метров до 4,56 метров). В 2012 году успешно прошел тест Euro NCAP.[1]')
    elif message.text == 'X2':
        bot.send_message(message.chat.id, 'BMW X2 (F39) — среднеразмерный кроссовер от немецкого автопроизводителя BMW. Автомобиль был представлен в 2016 году в Париже[1].'
                                          ' Серийно автомобиль производится с октября 2017 года[2]. На рынки автомобиль поставляется с марта 2018 года[3][4].')
    # характеристики данной модели mercedes
    elif message.text == 'W163':
        bot.send_message(message.chat.id, 'Mercedes-Benz W163 — первое поколение внедорожников M-класса от немецкой автомобильной марки Mercedes-Benz. Премьера автомобиля состоялась в феврале 1997 года с началом продаж в сентябре того же года. '
                                          'Производство первого поколения M-класса завершилось в 2005 году, а на смену ему в то же время пришли автомобили серии Mercedes-Benz W164.')
    elif message.text == 'W164':
        bot.send_message(message.chat.id, 'На рынке Германии на момент дебюта второго поколения M-класса автомобили были доступны как с бензиновыми, так и с дизельными силовыми агрегатами в конфигурациях V6 и V8. По время премьеры W164 состоялся дебют и нового дизельного двигателя V6 с системой Common Rail, пьезоэлектрическими форсунками и непосредственным впрыском топлива. Производительность модели ML 320 CDI составляла 165 кВт/224 л.с.[2] с максимальным крутящим моментом в 510 Н·м при 1600 оборотах в минуту. '
                                          'Новый бензиновый двигатель ML 350 генерировал 200 кВт/272 л.с. мощности и 350 Н·м крутящего момента.')
    elif message.text == 'W220':
        bot.send_message(message.chat.id, 'Среди моделей с бензиновыми двигателями базовой являлась S320 с двигателем М112 (3199 см3, V6, 224 л. с., 315 Н·м), хотя имелась также облегченная версия S280 для экспорта в Азию (тот же М112, но с рабочим объёмом 2799 см3, V6, 197 л. с., 270 Н·м).'
                                          ' По мощности М112 мотор немного уступал М104 на W140, но был более экономичным.')
    elif message.text == 'W221':
        bot.send_message(message.chat.id, 'Mercedes-Benz W221 — пятое поколение флагманской серии представительских автомобилей S-класса немецкой марки Mercedes-Benz, выпускавшихся с 2005 по 2013 года. Пришло на смену модели W220. В 2009 году автомобиль получил рестайлинг, в ходе которого были внесены внешние модификации и обновление модельного ряда двигателей. '
                                          'В 2013 производство автомобиля W221 было закончено, а на смену ему пришла модель Mercedes-Benz W222.')
    elif message.text == 'W222':
        bot.send_message(message.chat.id, 'На момент запуска автомобиля в производство было доступно 5 версий двигателей: 2 гибридных (S400 HYBRID и S300 BlueTEC HYBRID), 1 бензиновый (S500) и 1 дизельный (S350 BlueTEC)[2]. Все модели имели лучший класс эффективности в своём сегменте (S300 BlueTEC HYBRID — «A+», S400 HYBRID и S350 BlueTEC — «A») и обладали сниженным до 20 % расходом топлива по сравнению с предыдущей моделью серии. Все двигатели соответствуют требованиям стандарта Евро-6[2]. Также во время анонса нового S-класса 222 серии профессор Томас Вебер,'
                                          ' глава исследовательской группы и отдела развития Mercedes-Benz, заявил о ближайшем выпуске гибридной модели S500 plug-in Hybrid[2].')
    elif message.text == 'W223':
        bot.send_message(message.chat.id, 'Mercedes-Benz W223 — седьмое поколение флагманской серии представительских автомобилей S-класса немецкой марки Mercedes-Benz, выпускающееся с 2020 года. Пришло на смену модели W222 и базируется на втором поколении фирменной модульной платформы MRA. '
                                          'Презентация серии состоялась 2 сентября 2020 года. Продажи в России стартовали в декабре 2020 года[1].')

    # Кнопка и дествие назад
    if message.text == 'Назад':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=False)
        item1 = types.KeyboardButton('Audi')
        item2 = types.KeyboardButton('Bmw')
        item3 = types.KeyboardButton('Mercedes')
        markup.add(item1, item2, item3)
        bot.send_message(message.chat.id,'Вы вернулись назад. Выберите марку чтоб посмотреть характеристики', reply_markup=markup)

    # Кнопка и дествие интересний факт
    if message.text == 'Интересний факт':
        bot.send_message(message.chat.id, 'Донмез Бот')


bot.polling(none_stop=True)