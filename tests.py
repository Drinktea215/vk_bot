from unittest import TestCase
from unittest.mock import patch, Mock
from copy import deepcopy

from pony.orm import db_session, rollback
from vk_api.bot_longpoll import VkBotEvent

import settings
import intents
from Bot import Bot
from generate_ticket import generate_ticket


def isolate_db(test_func):
    def wrapper(*args, **kwargs):
        with db_session:
            test_func(*args, **kwargs)
            rollback()

    return wrapper


class Test1(TestCase):
    RAW_EVENT = {
        'type': 'message_new',
        'object': {'message': {'peer_id': 29530640, 'text': 'Привет!', 'random_id': 0}},
        'group_id': 192594482}

    def test_run(self):
        count = 5
        obj = {'a': 1}
        events = [obj] * count
        long_poller_mock = Mock(return_value=events)
        long_poller_listen_mock = Mock()
        long_poller_listen_mock.listen = long_poller_mock

        with patch('Bot.vk_api.VkApi'):
            with patch('Bot.VkBotLongPoll', return_value=long_poller_listen_mock):
                bot = Bot('', '')
                bot.on_event = Mock()
                bot.send_image = Mock()
                bot.run()

                bot.on_event.assert_called()
                bot.on_event.assert_any_call(obj)

                assert bot.on_event.call_count == count

    INPUTS = [
        'Привет!',
        'Help!',
        'москв',
        'Хабаровск',
        'билет',
        'Москва',
        'Сызрань',
        'Хабаровск',
        'Казань',
        '23:00',
        'Мефистофель',
        'Мой адрес mefis@tofel',
        'mefis@tof.el'
    ]
    EXPECTED_OUTPUTS = [
        intents.DEFAULT_ANSWER,
        intents.HELP,
        f"Из города {intents.INTENTS[0]['city']} авиакомпания совершает рейсы в следующие города: " \
        f"{', '.join(intents.INTENTS[0]['where'])}.",
        f"Из города {intents.INTENTS[8]['city']} авиакомпания совершает рейсы в следующие города: " \
        f"{', '.join(intents.INTENTS[8]['where'])}.",
        settings.SCENARIOS['registration']['steps']['step1']['text'],
        settings.SCENARIOS['registration']['steps']['step2']['text'],
        settings.SCENARIOS['registration']['steps']['step2']['failure_text'],
        settings.SCENARIOS['registration']['steps']['step3']['text'].format(city_out='Москва', city_in='Хабаровск',
                                                                            city_transfer=', '.join(
                                                                                intents.INTENTS[0]['where'])),
        settings.SCENARIOS['registration']['steps']['step4']['text'].format(
            departure_time=', '.join(intents.INTENTS[0]['when'][1])),
        settings.SCENARIOS['registration']['steps']['step5']['text'],
        settings.SCENARIOS['registration']['steps']['step6']['text'],
        settings.SCENARIOS['registration']['steps']['step6']['failure_text'],
        settings.SCENARIOS['registration']['steps']['step7']['text'].format(name='Мефистофель', email='mefis@tof.el')
    ]

    @isolate_db
    def test_run_ok(self):
        send_mock = Mock()
        api_mock = Mock()
        api_mock.messages.send = send_mock
        events = []
        for input_text in self.INPUTS:
            event = deepcopy(self.RAW_EVENT)
            event['object']['message']['text'] = input_text
            events.append(VkBotEvent(event))
        long_poller_mock = Mock()
        long_poller_mock.listen = Mock(return_value=events)
        with patch('Bot.VkBotLongPoll', return_value=long_poller_mock):
            bot = Bot('', '')
            bot.api = api_mock
            bot.send_image = Mock()
            bot.run()
        assert send_mock.call_count == len(self.INPUTS)
        real_outputs = []
        for call in send_mock.call_args_list:
            args, kwargs = call
            real_outputs.append(kwargs['message'])
        assert real_outputs == self.EXPECTED_OUTPUTS

    def test_image_generation(self):
        with open('files/kras@avch.ik.png', 'rb') as avatar_file:
            avatar_mock = Mock()
            avatar_mock.content = avatar_file.read()
        with patch('requests.get', return_value=avatar_mock):
            ticket_file = generate_ticket('Москва', 'Хабаровск', 'Казань', 'пт. 23:00', 'Красавчик', 'kras@avch.ik')
        with open('files/ticket_example.png', 'rb') as expected_file:
            expected_bytes = expected_file.read()
        assert ticket_file.read() == expected_bytes
