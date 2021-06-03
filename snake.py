import random
class SnakeAttacks():
    def AttackValues():
        Attacks = {random.randint(11, 20): random.randint(1, 10), random.randint(21, 30): random.randint(1, 20),
                       random.randint(31, 40): random.randint(1, 30), random.randint(41, 50): random.randint(1, 40),
                       random.randint(51, 60): random.randint(1, 50), random.randint(61, 70): random.randint(1, 60),
                       random.randint(71, 80): random.randint(1, 70), random.randint(81, 90): random.randint(1, 60),
                       random.randint(91, 99): random.randint(1, 50)}
        return Attacks
    def main(temp,Query):
        staticattacks=temp.copy()
        for value in staticattacks.items():
            if value[0]==Query:
                Attack=value[1]
                pos=Attack
                if pos<=100:
                    return pos
            return Query