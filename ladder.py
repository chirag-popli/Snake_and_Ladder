import random
class LadderBenifit():
    def LadderValues():
        Benifits = {random.randint(1, 10): random.randint(11, 30), random.randint(21, 30): random.randint(31, 60),
                       random.randint(31, 40): random.randint(41, 80), random.randint(51, 60): random.randint(61, 99),
                       random.randint(71, 90): random.randint(91, 99)}
        return Benifits
    def main(temp,Query):
        staticbenifits=temp.copy()
        for value in staticbenifits.items():
            if value[0]==Query:
                Benifit=value[1]
                Pos=Benifit
                if Pos<=100:
                    return Pos
            return Query