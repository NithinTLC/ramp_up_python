import random


def namegen(no_of_names):
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
                'V', 'W', 'X', 'Y', 'Z']

    for _ in range(no_of_names):
        names = [random.choice(alphabet) for _ in range(8)]
        fnames = set(names)
        sname = ''.join(fnames)
        number = str(random.randint(8754, 98568))
        yield f"User Name: {sname + number}"
# To get from gen
for username in namegen(10):
    print(username)

