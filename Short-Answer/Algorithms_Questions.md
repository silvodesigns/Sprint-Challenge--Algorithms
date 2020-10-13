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
       #0(n)
```

## Exercise II
```python
Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.

Write out your proposed algorithm in plain English or pseudocode AND give the runtime complexity of your solution.

#GOAL: DETERMINE THE VALUE OF F


#PROBLEM ANALYSIS:

1) There is an n-story building.
2) There are plenty of eggs.
3) There is a floor F.
4) Egg gets broken if thrown from floor F or higher
5) Egg does not get broken if thrown from F or lower


#HIGH LEVEL ALGORITHM:

1) Start at middle of N floor
2) Drop an Egg from N/2 floor
3) if it breaks, moves one step lower until it does not break
4) it it does not break, move one step higher until it does break

#MORE DETAILED:

1) Supposed we given the value 10 as N
  N = 10
  - Lets divide N by half.
  - N = 5
2) Lets drop an Egg from the new N value(n= 5)
    - if the egg breaks:
        move one step lower until it does not break n = n - 1
        when it does not break then F becomes  N + 1
    - if the egg does not break:
        move one step higher until it does break n = n + 1
        when it does finally break then F becomes N value


#Pseudocode:

N = 10
current_floor = n // 2
F = unknown 

drop_Egg(egg):  #0(1)
  if egg == broken:
      return true
  else:
      return false

while F == unknown: #0(n)
    if(drop_Egg(egg) == True): 
        current_floor = current_floor - 1 #0(1)
        if(drop_Egg(egg)==false):
            F = current_floor + 1  #0(1)
    else:
        current_floor = current_floor + 1 #0(1)


        # So the while loop in worst case scenario, would iterate over more than half
        # of the values given in N in order to find the value of F, best case would only 
        # go over half of N to get F, so since the time of operation depends on the size of N
        # the longer N is , the longer it would take so is 0(log N)

```