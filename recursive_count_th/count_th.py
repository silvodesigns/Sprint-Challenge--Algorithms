'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    toFind = 'th'
    #this is the base case
    if len(word) == 0 or len(word) < len(toFind):
        return 0

    #Recursive Case
    if word[0:len(toFind)] == toFind:
        return 1 + count_th(word[len(toFind) - 1:])
    else:
        return count_th(word[len(toFind)-1:])

    

  
