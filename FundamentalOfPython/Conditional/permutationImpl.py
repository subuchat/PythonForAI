from itertools import permutations

def permutation_of_3leters():
    # How can we find all possible permutation from letters 'A', 'B' and 'C' ?
    letters = ['A', 'B', 'C']

    '''
    perms = list(permutations(letters))
    for perm in perms:
        print(''.join(perm))
    '''
    perms = list(permutations(letters))
    print("Permutations : " , perms)
    print("Number of permutations : " , len(perms))

def permutation_of_4Letters():
    # How many ways we could pick 3 letters of of A, B , C & D. P(4,2)
    items = ['A','B','C','D']
    k =2
    perms = list(permutations(items,k))
    print("Permutation : ", perms)
    print("Number of permutations P(4,2) : ", len(perms))

'''
set of n objects , where n1 object of type1 , n2 object of type2 ..nk object of type k
then P(n) = n!
            ----
            n1! n2 ! ..nk!
'''
def permutation_wth_identicalObject():
   number = len(set(permutations('INFORMATION')))
   print("Permutation of identical object for INFORMATION are :", number)


def main(): 
    permutation_of_3leters()
    permutation_of_4Letters()
    permutation_wth_identicalObject()


if __name__ == "__main__":
    main()