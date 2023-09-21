import random

#Using mix of alpha numerics
def namegen(no_of_names):
     alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
                 'V', 'W', 'X', 'Y', 'Z']

     for _ in range(no_of_names):
         names = [random.choice(alphabet) for _ in range(8)]
         number = [str((random.randint(1, 9))) for _ in range(4)]
         mname= names + number
         random.shuffle(mname)
         fname= ''.join(mname)
         print(fname)
namegen(10)