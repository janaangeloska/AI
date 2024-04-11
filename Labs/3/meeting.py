from constraint import *


def marija_prisustvo(a, vreme):
    if a == 1:
        return vreme == 14 or vreme == 15 or vreme == 18
    return True


def petar_prisustvo(a, vreme):
    if a == 1:
        return vreme == 12 or vreme == 13 or vreme == 16 or vreme == 17 or vreme == 18 or vreme == 19
    return True


def barem_1(a, b):
    if a == 1 or b == 1:
        return True


if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())

    # ---Dadeni se promenlivite, dodadete gi domenite-----
    problem.addVariable("Simona_prisustvo", [1])
    problem.addVariable("Marija_prisustvo", [0, 1])
    problem.addVariable("Petar_prisustvo", [0, 1])
    problem.addVariable("vreme_sostanok", [13, 14, 16, 19])
    # ----------------------------------------------------

    # ---Tuka dodadete gi ogranichuvanjata----------------
    problem.addConstraint(marija_prisustvo, ["Marija_prisustvo", "vreme_sostanok"])
    problem.addConstraint(petar_prisustvo, ["Petar_prisustvo", "vreme_sostanok"])
    problem.addConstraint(barem_1, ["Petar_prisustvo", "Marija_prisustvo"])
    # ----------------------------------------------------

    # [print(solution) for solution in problem.getSolutions()]

    for solution in problem.getSolutions():
        print("{'Simona_prisustvo':", solution.get('Simona_prisustvo'), end="")
        print(", 'Marija_prisustvo':", solution.get('Marija_prisustvo'), end="")
        print(", 'Petar_prisustvo':", solution.get('Petar_prisustvo'), end="")
        print(", 'vreme_sostanok':", solution.get('vreme_sostanok'), end="")
        print("}")
