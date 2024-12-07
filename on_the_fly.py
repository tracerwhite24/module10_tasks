import random

first = 'Мама мыла раму'
second = 'Рамена мало было'

result = list(map(lambda x, y: x == y, first, second))

print(result)

def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'w', encoding='utf-8') as file:
            for item in data_set:
                if isinstance(item, list):
                    file.write(' '.join(map(str, item)) + '\n')
                else:
                    file.write(str(item) + '\n')
    return write_everything

write = get_advanced_writer('example.txt')

write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

class MysticBall:
    def __init__(self, *words):
        self.words = words

    def call(self):
        return random.choice(self.words)

first_ball = MysticBall(
    'It is certain',
    'It is decidedly so',
    'Without a doubt',
    'Yes definitely',
    'You may rely on it',
    'As I see it, yes',
    'Most likely',
    'Outlook good',
    'Yes',
    'Signs point to yes',
    'Reply hazy, try again',
    'Ask again later',
    'Better not tell you now',
    'Cannot predict now',
    'Concentrate and ask again',
    "Don't count on it",
    'My reply is no',
    'My sources say no',
    'Outlook not so good',
    'Very doubtful'
)

print(first_ball.call())
print(first_ball.call())
print(first_ball.call())

