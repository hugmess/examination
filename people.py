class Person:
    def __init__(self, name='', health_status=0, mood=0, capital=0):
        self.name = name
        self.health_status = health_status
        self.max_health_status = health_status
        self.mood = mood
        self.max_mood = mood
        self.capital = capital

    def do(self):
        pass

    def change_state(self, health_status=0, mood=0, capital=0):
        self.health_status = health_status
        self.mood = mood
        self.capital = capital



    def __str__(self):
        return \
            f'=== {self.name} ===\n' \
               f'Состояние здоровья: {self.health_status} / {self.max_health_status} \n' \
               f'Настроение: {self.mood} \n' \
               f'Капитал: {self.capital} \n'


class Action:
    def __init__(self, name='', health_status=0, mood=0, capital=0 ):
        self.name = name
        self.health_status = health_status
        self.max_health_status = health_status
        self.mood = mood
        self.max_mood = mood
        self.capital = capital


class NegativeHealthError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


def health(health_status):
    if health_status < 0:
        raise NegativeHealthError('человек скончался')
    print(f'Отняли {health_status} здоровья.')


try:
    health(-1)
except NegativeHealthError:
    print('человек скончался')
except Exception as error:
    print(f'Что-то пошло не так: {error}')


class NegativeMoodError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


def sentiment(mood):
    if mood < 0:
        raise NegativeMoodError('Человек впал в депрессию')
    print(f'Отняли {mood} настроения.')


try:
    health(-1)
except NegativeHealthError:
    print('человек скончался')
except Exception as error:
    print(f'Что-то пошло не так: {error}')


class NegativeCapitalError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


def equity(capital):
    if capital < 0:
        raise NegativeHealthError('Человек обанкротился.')
    print(f'Отняли {capital} денег.')


try:
    equity(-1)
except NegativeCapitalError:
    print('Человек обанкротился.')
except Exception as error:
    print(f'Что-то пошло не так: {error}')

