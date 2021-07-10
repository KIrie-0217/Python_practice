from Gene_alg import Evaluator
import numpy as np
from Gene_alg import Gene

def main():
    class Genealg(Evaluator):
        def Evaluate_function(self,genes):
            return genes**2

    test =  Genealg()

    print("hello word")
    print(test.evaluate(np.array([1,2,3,4])))



if __name__ == "__main__":
    main()