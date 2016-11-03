from django.db import models

# Create your models here.


class Rotor:
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
                'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
                'Y', 'Z']

    # The shift in effect defines a Ceasar Cipher for each letter
    # of the alphabet. In this case, each letter is mapped onto itself and
    # the plaintext and ciphertext would be one and the same.
    shift = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
             'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    # The turnover point is the contact (in reference to the shift) that is
    # visible in the Enigma's rotor window when the rotation notch will rotate
    # the neighboring rotor with its next rotation.
    turnover = ['A']

    def __init__(self, next_rotor=None):
        self.next_rotor = next_rotor
        self.get_wiring()

    def get_wiring(self):
        wiring = []
        for a, s in zip(self.alphabet, self.shift):
            dist = self.alphabet.index(s) - self.alphabet.index(a)
            wire = (dist, s)
            wiring.append(wire)
        self.wiring = wiring

    # The .calibrate() method allows the rotors to be oriented to start on any
    # of their 26 contact points. While the Python code utilizes zero-based
    # indexing, the user experience of this program attempts to be true to the
    # original Enigma by using one-based indexing as the actual rotors
    # were labeled.
    def calibrate(self, letter):
        idx = self.alphabet.index(letter)
        rotation = self.wiring[:idx]
        self.wiring.extend(rotation)
        del self.wiring[:idx]

    def rotate(self):
        x = self.wiring.pop(0)
        if x[1] in self.turnover and isinstance(self.next_rotor, Rotor):
            self.next_rotor.rotate()
        self.wiring.append(x)

    # Since the shift of each rotor is effectively a Ceasar Cipher, the
    # .encrypt_connect() method is simply performing a Ceasar Cipher on
    # an input number according to the shift in the contact whose index is the
    # same as incoming number.
    def encrypt_connect(self, num):
        x = (num + self.wiring[num][0]) % len(self.alphabet)
        return x

    # Effectively does the reverse of the .encrypt_connect() method by
    # finding which shift would correspond to the input number and returns
    # that contact's index.
    def decrypt_connect(self, num):
        for idx, wire in enumerate(self.wiring):
            if ((idx + wire[0]) % len(self.alphabet)) == num:
                return idx


class RotorI(Rotor):
    shift = ['E', 'K', 'M', 'F', 'L', 'G', 'D', 'Q', 'V', 'Z', 'N', 'T', 'O',
             'W', 'Y', 'H', 'X', 'U', 'S', 'P', 'A', 'I', 'B', 'R', 'C', 'J']

    # wiring = [(4, 'A'), (9, 'B'), (10, 'C'), (2, 'D'), (7, 'E'), (1, 'F'),
    #           (-3, 'G'), (9, 'H'), (13, 'I'), (16, 'J'), (3, 'K'), (8, 'L'),
    #           (2, 'M'), (9, 'N'), (10, 'O'), (-8, 'P'), (7, 'Q'), (3, 'R'),
    #           (0, 'S'), (-4, 'T'), (-20, 'U'), (-13, 'V'), (-21, 'W'),
    #           (-6, 'X'), (-22, 'Y'), (-16, 'Z')]

    turnover = ['Q']


class RotorII(Rotor):
    shift = ['A', 'J', 'D', 'K', 'S', 'I', 'R', 'U', 'X', 'B', 'L', 'H', 'W',
             'T', 'M', 'C', 'Q', 'G', 'Z', 'N', 'P', 'Y', 'F', 'V', 'O', 'E']

    # wiring = [(0, 'A'), (8, 'B'), (1, 'C'), (7, 'D'), (14, 'E'), (3, 'F'),
    #           (11, 'G'), (13, 'H'), (15, 'I'), (-8, 'J'), (1, 'K'), (-4, 'L'),
    #           (10, 'M'), (6, 'N'), (-2, 'O'), (-13, 'P'), (0, 'Q'), (-11, 'R'),
    #           (7, 'S'), (-6, 'T'), (-5, 'U'), (3, 'V'), (-17, 'W'), (-2, 'X'),
    #           (-10, 'Y'), (-21, 'Z')]

    turnover = ['E']


class RotorIII(Rotor):
    shift = ['B', 'D', 'F', 'H', 'J', 'L', 'C', 'P', 'R', 'T', 'X', 'V', 'Z',
             'N', 'Y', 'E', 'I', 'W', 'G', 'A', 'K', 'M', 'U', 'S', 'Q', 'O']
    #
    # wiring = [(1, 'A'), (2, 'B'), (3, 'C'), (4, 'D'), (5, 'E'), (6, 'F'),
    #           (-4, 'G'), (8, 'H'), (9, 'I'), (10, 'J'), (13, 'K'), (10, 'L'),
    #           (13, 'M'), (0, 'N'), (10, 'O'), (-11, 'P'), (-8, 'Q'), (5, 'R'),
    #           (-12, 'S'), (-19, 'T'), (-10, 'U'), (-9, 'V'), (-2, 'W'),
    #           (-5, 'X'), (-8, 'Y'), (-11, 'Z')]

    turnover = ['V']


class RotorIV(Rotor):
    shift = ['E', 'S', 'O', 'V', 'P', 'Z', 'J', 'A', 'Y', 'Q', 'U', 'I', 'R',
             'H', 'X', 'L', 'N', 'F', 'T', 'G', 'K', 'D', 'C', 'M', 'W', 'B']

    # wiring = [(4, 'A'), (17, 'B'), (12, 'C'), (18, 'D'), (11, 'E'), (20, 'F'),
    #           (3, 'G'), (-7, 'H'), (16, 'I'), (7, 'J'), (10, 'K'), (-3, 'L'),
    #           (5, 'M'), (-6, 'N'), (9, 'O'), (-4, 'P'), (-3, 'Q'), (-12, 'R'),
    #           (1, 'S'), (-13, 'T'), (-10, 'U'), (-18, 'V'), (-20, 'W'),
    #           (-11, 'X'), (-2, 'Y'), (-24, 'Z')]

    turnover = ['J']


class RotorV(Rotor):
    shift = ['V', 'Z', 'B', 'R', 'G', 'I', 'T', 'Y', 'U', 'P', 'S', 'D', 'N',
             'H', 'L', 'X', 'A', 'W', 'M', 'J', 'Q', 'O', 'F', 'E', 'C', 'K']

    # wiring = [(21, 'A'), (24, 'B'), (-1, 'C'), (14, 'D'), (2, 'E'), (3, 'F'),
    #           (13, 'G'), (17, 'H'), (12, 'I'), (6, 'J'), (8, 'K'), (-8, 'L'),
    #           (1, 'M'), (-6, 'N'), (-3, 'O'), (8, 'P'), (-16, 'Q'), (5, 'R'),
    #           (-6, 'S'), (-10, 'T'), (-4, 'U'), (-7, 'V'), (-17, 'W'),
    #           (-19, 'X'), (-22, 'Y'), (-15, 'Z')]

    turnover = ['Z']


# Rotors VI, VII, and VIII were added later in the war due to a belief that
# Enigma had been compromised (...it had...). The key differences between them
# and previous rotors were that they had two turnover points rather than just
# one, meaning it would turnover the neighboring rotor twice as frequently.
class RotorVI(Rotor):
    shift = ['J', 'P', 'G', 'V', 'O', 'U', 'M', 'F', 'Y', 'Q', 'B', 'E', 'N',
             'H', 'Z', 'R', 'D', 'K', 'A', 'S', 'X', 'L', 'I', 'C', 'T', 'W']

    # wiring = [(9, 'A'), (14, 'B'), (4, 'C'), (18, 'D'), (10, 'E'), (15, 'F'),
    #           (6, 'G'), (-2, 'H'), (16, 'I'), (7, 'J'), (-9, 'K'), (-7, 'L'),
    #           (1, 'M'), (-6, 'N'), (11, 'O'), (2, 'P'), (-13, 'Q'), (-7, 'R'),
    #           (-18, 'S'), (-1, 'T'), (3, 'U'), (-10, 'V'), (-14, 'W'),
    #           (-21, 'X'), (-5, 'Y'), (-3, 'Z')]

    turnover = ['Z', 'M']


class RotorVII(Rotor):
    shift = ['N', 'Z', 'J', 'H', 'G', 'R', 'C', 'X', 'M', 'Y', 'S', 'W', 'B',
             'O', 'U', 'F', 'A', 'I', 'V', 'L', 'P', 'E', 'K', 'Q', 'D', 'T']

    # wiring = [(13, 'A'), (24, 'B'), (7, 'C'), (4, 'D'), (2, 'E'), (12, 'F'),
    #           (-4, 'G'), (16, 'H'), (4, 'I'), (15, 'J'), (8, 'K'), (11, 'L'),
    #           (-11, 'M'), (1, 'N'), (6, 'O'), (-10, 'P'), (-16, 'Q'),
    #           (-9, 'R'), (3, 'S'), (-8, 'T'), (-5, 'U'), (-17, 'V'),
    #           (-12, 'W'), (-7, 'X'), (-21, 'Y'), (-6, 'Z')]

    turnover = ['Z', 'M']


class RotorVIII(Rotor):
    shift = ['F', 'K', 'Q', 'H', 'T', 'L', 'X', 'O', 'C', 'B', 'J', 'S', 'P',
             'D', 'Z', 'R', 'A', 'M', 'E', 'W', 'N', 'I', 'U', 'Y', 'G', 'V']

    # wiring = [(5, 'A'), (9, 'B'), (14, 'C'), (4, 'D'), (15, 'E'), (6, 'F'),
    #           (17, 'G'), (7, 'H'), (-6, 'I'), (-8, 'J'), (-1, 'K'), (7, 'L'),
    #           (3, 'M'), (-10, 'N'), (11, 'O'), (2, 'P'), (-16, 'Q'), (-5, 'R'),
    #           (-14, 'S'), (3, 'T'), (-7, 'U'), (-13, 'V'), (-2, 'W'), (1, 'X'),
    #           (-18, 'Y'), (-4, 'Z')]

    turnover = ['Z', 'M']


# Simulates Enigma M4, which was used exclusively by the U-Boot
# division of the German Navy (Kriegsmarine).
class Enigma:
    # Simulates UKW-B reflector, which was used throughout the war
    reflector = {0: 4, 1: 13, 2: 10, 3: 16, 4: 0, 5: 20, 6: 24, 7: 22, 8: 9,
                 9: 8, 10: 2, 11: 14, 12: 15, 13: 1, 14: 11, 15: 12, 16: 3,
                 17: 23, 18: 25, 19: 21, 20: 5, 21: 19, 22: 7, 23: 17, 24: 6,
                 25: 18}

    entrywheel = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6,
                  'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12, 'N': 13,
                  'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19,
                  'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25}

    reentry_wheel = {number: letter for letter, number in entrywheel.items()}

    def __init__(self, slow_rotor=RotorI(),
                 middle_rotor=RotorII(), fast_rotor=RotorIII(),
                 initial_settings=['A', 'A', 'A']):

        self.slow_rotor = slow_rotor
        self.middle_rotor = middle_rotor
        self.fast_rotor = fast_rotor

        # Making the fast and middle rotors aware of their neighbor allows
        # their .rotate() method to rotate their neighbor too when the contact
        # containing the turnover point is rotated (like an odometer rolling
        # over)
        self.fast_rotor.next_rotor = middle_rotor
        self.middle_rotor.next_rotor = slow_rotor

        self.slow_rotor.calibrate(initial_settings[0])
        self.middle_rotor.calibrate(initial_settings[1])
        self.fast_rotor.calibrate(initial_settings[2])

    # Turns input letter into a number on the entry wheel, then passes the
    # number through the three rotors via the .encrypt_connect() method to the
    # reflector, turned back to the rotors then back through the three rotors
    # via the .decrypt_connect() method to the reentry wheel, which is just
    # the dictionary inverse of the entry wheel. This returns an encrypted
    # letter.
    def encrypt(self, letter):
        number = self.entrywheel[letter]
        # self.fast_rotor.rotate() This line should be handled by JS
        fr = self.fast_rotor.encrypt_connect(number)
        mr = self.middle_rotor.encrypt_connect(fr)
        sr = self.slow_rotor.encrypt_connect(mr)
        reflection = self.reflector[sr]
        sr_ref = self.slow_rotor.decrypt_connect(reflection)
        mr_ref = self.middle_rotor.decrypt_connect(sr_ref)
        fr_ref = self.fast_rotor.decrypt_connect(mr_ref)
        cipherletter = self.reentry_wheel[fr_ref]
        return cipherletter
