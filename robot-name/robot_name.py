import random
import string
class Robot:
    def __init__(self):
        letters = ''.join(random.choice(string.ascii_uppercase) for i in range(2))
        numbers = ''.join(random.choice(string.digits) for j in range(3))
        self.name = letters + numbers
    def reset(self):
        old = self.name
        while (old == self.name):
            letters = ''.join(random.choice(string.ascii_uppercase) for i in range(2))
            numbers = ''.join(random.choice(string.digits) for j in range(3))
            self.name = letters + numbers
        return self.name