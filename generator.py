import random
import string

l_a = string.ascii_lowercase
l_n = string.digits
l_s = string.punctuation
l = []
l.extend(list(string.ascii_lowercase.lower()) + list(string.ascii_lowercase.upper())
         + list(string.digits) + list(string.punctuation))

def gen_pass(num):
    d = []
    for x in l:
        d.append(x)
    if num >= 4:
        s = []
        for x in range(1):
            s.append(random.choice(l_a).lower() + random.choice(l_a).upper() + random.choice(l_n) + random.choice(l_s))
        min_pass = ''.join(s)
        while len(min_pass) < num:
            r = random.choice(d)
            if r in min_pass:
                d.remove(r)
                pass
            else:
                min_pass = min_pass + r
        return min_pass
    else:
        print('To low pasword')


while True:
    try:
        print('Max password', len(l))
        num = int(input('Enter len password(number): '))
        print(gen_pass(num))
    except Exception as ex:
        print('Error: ', ex)
