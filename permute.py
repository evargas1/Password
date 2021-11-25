# given an array of A of n elements and a permutation P, apply P to A

def find_permuteation(perm):
    # find the first entry 
    inversion_point = len(perm) - 2
    while (inversion_point >= 0) and perm[inversion_point + 1]):
        inversion_point -= 1
    if inversion_point == -1:
        return []

    for i in reversed(range(inversion_point + 1, len(perm))):
        perm[inversion_point], perm[i] = perm[i], perm[inversion_point]:
        