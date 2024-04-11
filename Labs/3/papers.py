from constraint import *


def sort_by_first_arg(item):
    return int(item[0].split(' ')[0][5:])


def max4(*args):
    counts = {'T1': 0, 'T2': 0, 'T3': 0, 'T4': 0}
    for arg in args:
        counts[arg] += 1
        if counts[arg] > 4:
            return False
    return True


if __name__ == '__main__':
    num = int(input())

    papers = dict()

    paper_info = input()
    while paper_info != 'end':
        title, topic = paper_info.split(' ')
        papers[title] = topic
        paper_info = input()

    # Tuka definirajte gi promenlivite
    variables = []
    ai = []
    ml = []
    nlp = []

    for paper in papers:
        # title->key(pr Paper1)   topic->value(pr ai)
        variables.append(f"{paper} ({papers[paper]})")
        if papers[paper] == "AI":
            ai.append(f"{paper} ({papers[paper]})")
        if papers[paper] == "ML":
            ml.append(f"{paper} ({papers[paper]})")
        if papers[paper] == "NLP":
            nlp.append(f"{paper} ({papers[paper]})")

    domain = [f'T{i + 1}' for i in range(num)]

    problem = Problem(BacktrackingSolver())

    # Dokolku vi e potrebno moze da go promenite delot za dodavanje na promenlivite
    problem.addVariables(variables, domain)
    # T1 T2 T3 (T4)

    # Tuka dodadete gi ogranichuvanjata
    problem.addConstraint(max4, variables)

    if 0 < len(ai) <= 4:
        problem.addConstraint(AllEqualConstraint(), ai)
    if 0 < len(ml) <= 4:
        problem.addConstraint(AllEqualConstraint(), ml)
    if 0 < len(nlp) <= 4:
        problem.addConstraint(AllEqualConstraint(), nlp)

    result = problem.getSolution()
  
    # Tuka dodadete go kodot za pechatenje
    if result:
        sorted_res = sorted(result.items(), key=sort_by_first_arg)
        for i, val in sorted_res:
            print(f"{i}: {val}")
