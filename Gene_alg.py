import numpy as np

class Generator():
    def __init__(self,max,min,dimension):
        self.max = max
        self.min = min
        self.dimension = dimension



class Evaluator():
    """Temporary Evaluate function
    """
    def __init__(self):
        pass
    def evaluate(self,Individual):
        return self.Evaluate_function(Individual)

class Crossover():
    """Crossover method selector
    """
    def __init__(self) -> None:
        pass

class Parents():
    """Parents selector
    """
    def __init__(self) -> None:
        pass

class Nextgen():
    """Next Generation generator
    """
    def __init__(self) -> None:
        pass

class Gene():
    def __init__(self, Evaluator,Crossover,Parents,Nextgen):
        self.Evaluator = Evaluator
        self.Crossover = Crossover
        self.Parents = Parents
        self.Nextgen = Nextgen

    def generate(self,individual_num,generetor):
        pass

    def next_generation(self):
        pass
