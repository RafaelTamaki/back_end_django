from random import randint
from faker import Faker


def rand_ratio():
    return randint(840, 900), randint(473, 573)


fake = Faker('pt_BR')


def make_poetry():
    return {
        # Títulos de poesias geralmente são curtos
        'title': fake.sentence(nb_words=5),
        # Texto de poesia (supondo que seja menor que uma receita)
        'full_text': fake.text(250),
        'created_at': fake.date_time(),
        'author': {
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
        },
        'genre': {  # Gênero literário da poesia
            'name': fake.word()
        },
        'cover': {
            # Imagem relacionada a poesia ou livro
            'url': 'https://loremflickr.com/%s/%s/poetry,book' % rand_ratio(),
        },
        'is_popular': fake.boolean()
    }


if __name__ == '__main__':
    from pprint import pprint
    pprint(fazer_poema())