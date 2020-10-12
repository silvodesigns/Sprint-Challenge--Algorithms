# Analysis of Algorithms

## Exercise I

Give an analysis of the running time of each snippet of
pseudocode with respect to the input size n of each of the following:

```python
a)  a = 0
    while (a < n * n * n):
      a = a + n * n

      #t = o(1) + o(n) + #o(1)

      #assigning a value to variable is a contant time 
      #since it doesnt depend on the value of the input
      #and we have liner 0(n) in the while loop because
      #the time it takes will depend on the size of N
      #so at the end we drop the 0(1)s and we have biggest constant
      #0(n) as worst case scenario
```


```python
b)  sum = 0 #0(1)
    for i in range(n): #O(n)
      j = 1 #0(1)
      while j < n: #O(n)
        j *= 2 #0(1)
        sum += 1 #0(1)

    #t = 0(1) +0(n) x 0(1) + 0(n) x 0(1) + 0(1)
    #t = o(n) + o(n)
    #t = o(n log(n) )
```

```python
c)  def bunnyEars(bunnies):
      if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1) #0(1)+ N

       #T = 0(1) + 0(1) + n
```

## Exercise II

Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.

Write out your proposed algorithm in plain English or pseudocode AND give the runtime complexity of your solution.
