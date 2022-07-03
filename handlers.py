import re

from generate_ticket import generate_ticket
from intents import CITIES, INTENTS

re_name = re.compile(r'^[\w\-\s]{3,40}$')
re_email = re.compile(r'\b[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+\b')
re_day = re.compile(r'^[а-яА-Я\d+:.\d+]{2,11}$')


def handle_city(text, context, city):
    match = re.match(re_name, text)
    if match:
        if text.title() in CITIES:
            if city == 'out':
                context['city_out'] = text.title()
            elif city == 'in':
                context['city_in'] = text.title()
                if handle_check_city(text, context, city):
                    context['city_transfer'] = 'Без пересадок'
                    return True, 0
                else:
                    return True, 1
            else:
                context['city_transfer'], context['city_in'] = context['city_in'], text.title()  # Временно меняем пересадку с городом назначения.
                if handle_check_city(text, context, city):
                    pass
            return True, 0
        else:
            return False, 0
    else:
        return False, 0


def handle_check_city(text, context, city):  # Проверка прямого авиасообщения.
    for index, city in enumerate(INTENTS):
        if context['city_out'] == city['city']:
            if context['city_in'] in city['where']:
                index = city['where'].index(context['city_in'])
                context['departure_time'] = ', '.join(city['when'][index])
                return True
            else:
                break
    context['city_transfer'] = search_for_transfers(context)
    return False


def search_for_transfers(context):  # Поиск города для пересадок.
    cities_transfers = []
    for city in INTENTS:
        if city['city']:
            if context['city_in'] in city['where']:
                cities_transfers.append(city['city'])
    return ', '.join(cities_transfers)


def handle_departure_time(text, context, city):
    match = re.match(re_day, text)
    context['departure_time'] = context['departure_time'].split(', ')
    if match:
        for index, day in enumerate(context['departure_time']):
            if text in day:
                context['departure_time'] = day
                if context['city_transfer'] != 'Без пересадок':
                    context['city_transfer'], context['city_in'] = context['city_in'], context['city_transfer']
                return True, 0
        else:
            return False, 0


def handle_name(text, context, city):
    match = re.match(re_name, text)
    if match:
        context['name'] = text
        return True, 0
    else:
        return False, 0


def handle_email(text, context, city):
    matches = re.findall(re_email, text)
    if len(matches) > 0:
        context['email'] = text
        return True, 0
    else:
        return False, 0


def handle_generate_ticket(text, context):
    return generate_ticket(
        context['city_in'],
        context['city_out'],
        context['city_transfer'],
        context['departure_time'],
        context['name'],
        context['email'])
