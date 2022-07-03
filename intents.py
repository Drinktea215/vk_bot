INTENTS = [
    {
        'city': 'Москва',
        'tokens': ('москв',),
        'where': ['Санкт-Питербург', 'Казань', 'Владивосток', 'Мурманск', 'Новосибирск', 'Сочи', 'Иркутск'],
        'scenario': None,
        'when': [['пн. 09:00', 'чт. 21:00'], ['вт. 11:00', 'пт. 23:00'], ['ср. 15:00', 'сб. 03:00'],
                 ['чт. 18:00', 'вс. 06:00'], ['пт. 21:00', 'пн. 09:00'], ['сб. 23:00', 'вт. 11:00'],
                 ['вс. 02:00', 'ср. 14:00']]
    },
    {
        'city': 'Санкт-Питербург',
        'tokens': ('питер',),
        'where': ['Москва', 'Казань', 'Владивосток', 'Мурманск', 'Новосибирск', 'Сочи', 'Хабаровск'],
        'scenario': None,
        'when': [['пн. 09:00', 'чт. 21:00'], ['вт. 11:00', 'пт. 23:00'], ['ср. 15:00', 'сб. 03:00'],
                 ['чт. 18:00', 'вс. 06:00'], ['пт. 21:00', 'пн. 09:00'], ['сб. 23:00', 'вт. 11:00'],
                 ['вс. 02:00', 'ср. 14:00']]
    },
    {
        'city': 'Казань',
        'tokens': ('казан',),
        'where': ['Санкт-Питербург', 'Москва', 'Владивосток', 'Мурманск', 'Новосибирск', 'Иркутск', 'Хабаровск'],
        'scenario': None,
        'when': [['пн. 09:00', 'чт. 21:00'], ['вт. 11:00', 'пт. 23:00'], ['ср. 15:00', 'сб. 03:00'],
                 ['чт. 18:00', 'вс. 06:00'], ['пт. 21:00', 'пн. 09:00'], ['сб. 23:00', 'вт. 11:00'],
                 ['вс. 02:00', 'ср. 14:00']]
    },
    {
        'city': 'Владивосток',
        'tokens': ('владивосток',),
        'where': ['Санкт-Питербург', 'Казань', 'Москва', 'Мурманск', 'Сочи', 'Иркутск', 'Хабаровск'],
        'scenario': None,
        'when': [['пн. 09:00', 'чт. 21:00'], ['вт. 11:00', 'пт. 23:00'], ['ср. 15:00', 'сб. 03:00'],
                 ['чт. 18:00', 'вс. 06:00'], ['пт. 21:00', 'пн. 09:00'], ['сб. 23:00', 'вт. 11:00'],
                 ['вс. 02:00', 'ср. 14:00']]
    },
    {
        'city': 'Мурманск',
        'tokens': ('мурманск',),
        'where': ['Санкт-Питербург', 'Казань', 'Владивосток', 'Новосибирск', 'Сочи', 'Иркутск', 'Хабаровск'],
        'scenario': None,
        'when': [['пн. 09:00', 'чт. 21:00'], ['вт. 11:00', 'пт. 23:00'], ['ср. 15:00', 'сб. 03:00'],
                 ['чт. 18:00', 'вс. 06:00'], ['пт. 21:00', 'пн. 09:00'], ['сб. 23:00', 'вт. 11:00'],
                 ['вс. 02:00', 'ср. 14:00']]
    },
    {
        'city': 'Новосибирск',
        'tokens': ('новосиб',),
        'where': ['Санкт-Питербург', 'Казань', 'Мурманск', 'Москва', 'Сочи', 'Иркутск', 'Хабаровск'],
        'scenario': None,
        'when': [['пн. 09:00', 'чт. 21:00'], ['вт. 11:00', 'пт. 23:00'], ['ср. 15:00', 'сб. 03:00'],
                 ['чт. 18:00', 'вс. 06:00'], ['пт. 21:00', 'пн. 09:00'], ['сб. 23:00', 'вт. 11:00'],
                 ['вс. 02:00', 'ср. 14:00']]
    },
    {
        'city': 'Сочи',
        'tokens': ('соч',),
        'where': ['Санкт-Питербург', 'Владивосток', 'Мурманск', 'Новосибирск', 'Москва', 'Иркутск', 'Хабаровск'],
        'scenario': None,
        'when': [['пн. 09:00', 'чт. 21:00'], ['вт. 11:00', 'пт. 23:00'], ['ср. 15:00', 'сб. 03:00'],
                 ['чт. 18:00', 'вс. 06:00'], ['пт. 21:00', 'пн. 09:00'], ['сб. 23:00', 'вт. 11:00'],
                 ['вс. 02:00', 'ср. 14:00']]
    },
    {
        'city': 'Иркутск',
        'tokens': ('иркут',),
        'where': ['Казань', 'Владивосток', 'Мурманск', 'Новосибирск', 'Сочи', 'Москва', 'Хабаровск'],
        'scenario': None,
        'when': [['пн. 09:00', 'чт. 21:00'], ['вт. 11:00', 'пт. 23:00'], ['ср. 15:00', 'сб. 03:00'],
                 ['чт. 18:00', 'вс. 06:00'], ['пт. 21:00', 'пн. 09:00'], ['сб. 23:00', 'вт. 11:00'],
                 ['вс. 02:00', 'ср. 14:00']]
    },
    {
        'city': 'Хабаровск',
        'tokens': ('хабар',),
        'where': ['Санкт-Питербург', 'Казань', 'Мурманск', 'Новосибирск', 'Сочи', 'Иркутск', 'Москва'],
        'scenario': None,
        'when': [['пн. 09:00', 'чт. 21:00'], ['вт. 11:00', 'пт. 23:00'], ['ср. 15:00', 'сб. 03:00'],
                 ['чт. 18:00', 'вс. 06:00'], ['пт. 21:00', 'пн. 09:00'], ['сб. 23:00', 'вт. 11:00'],
                 ['вс. 02:00', 'ср. 14:00']]
    },
    {
        'city': None,
        'tokens': ('билет', 'ticket'),
        'scenario': 'registration',
        'where': None
    },
    {
        'city': None,
        'tokens': ('help', 'помощ', 'помог', 'справк'),
        'where': 'Help',
        'scenario': None,
        'when': None
    }
]

DEFAULT_ANSWER = 'Вас приветствует бот авиакомпании "Куда подальше". ' \
                 'Я могу ознакомить вас со списком городов, участвующих в авиасообщении нашей компании, ' \
                 'а также я могу зарегистрировать вас на рейс. ' \
                 'Просто спросите или попросите помощь, напечатав слово "Help".'

CITIES = [city['city'] for city in INTENTS if city['city']]

HELP = 'В авиасообщении компании "Куда Подальше" учавствуют следующие города:\n{CITIES}.'.format(
    CITIES="\n".join(CITIES))