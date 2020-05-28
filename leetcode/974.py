import numpy
def subarraysDivByK(self, A: List[int], K: int) -> int:
    dict = {0: 1}
    pred, addSum = 0, 0
    for i in A:
        pred = (pred + i) % K
        if pred in dict:
            addSum += dict[pred]
        dict[pred] = dict.get(pred, 0) + 1
    return addSum

if __name__ == "__main__":
    A = [4,5,0,-2,-3,1]
    K = 5
    subarraysDivByK(A, K)