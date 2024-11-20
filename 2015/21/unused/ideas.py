    
import itertools
import string

from shop import Shop, ShopItem, Weapon, Armor, Ring 

def get_mixes_product(spoons, ingredients, valid=lambda mix, spoons:sum(mix)==spoons):
    '''returns all possible combinations of n ingredients for a max total of spoons'''
    for mix in itertools.product(range(1, spoons), repeat=ingredients):
        if valid(mix, spoons):
            yield mix

shop = Shop()
weapons = shop.weapons()
armors = shop.armors()
leftrings = shop.rings()
rightrings = shop.rings()
assert leftrings is not rightrings, 'fuck'
assert leftrings == rightrings, 'fuck'

# for weapon, armor, lring, rring in zip(weapons, armors, leftrings, rightrings):
    # print(weapon.name, armor.name, lring.name, rring.name)
    # print()

l = []
for weapon, armor, lring, rring in itertools.product(weapons, armors, leftrings, rightrings):
# for weapon, armor, lring, rring in itertools.combinations(shop.items(), r=4):
    if lring is not rring:
        print(weapon.name, armor.name, lring.name, rring.name)
        tpl = (weapon.name, armor.name, lring.name, rring.name)
        l.append(tpl)
print(len(l))
print(len(set(l)))

def test_combinations(data, max_len=None):
    '''test itertools.combinations'''
    for r in range(max_len if max_len is not None else len(data)):
        print(f'{r=}')
        for combo in itertools.combinations(data, r=r):
            print(combo)
        print()


def password_wordlist(start_range=8, end_range=10, file_name="brute.txt"):
    # string with all characters needed or have potential for being password
    chars = string.ascii_lowercase + string.ascii_uppercase + string.digits + '@' + '#' + '$' + '.'
    # attempts counter
    attempts = 0
    # open file
    f = open(file_name, 'w')

    for password_length in range(start_range, end_range):
        print(f"{password_length = }")
        # input()
        buffer = []
        max_buffer = 1000000
        for guess in itertools.product(chars, repeat=password_length):
            attempts += 1
            guess = ''.join(guess)
            # f.write(guess)  # write in file
            # f.write("\n")
            buffer.append(guess)
            print(f"{guess:{end_range+1}}: {attempts:20,}")
            if not attempts % max_buffer:
                print("-------------------------------------------write buffer")
                # input()
                f.write('\n'.join(buffer) + '\n')
                buffer = []
                print("-------------------------------------------reset buffer")

    # close file
    f.close()
