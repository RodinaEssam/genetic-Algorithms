Step 1: Representation 

Write the each bitstring in form of list and the initial population has all these lists. 

 

Step 2: Calculate fitness function 

Let fitness=0 then create loop start from second element until the 7th element if the element equal to 1, check the two adjacent ones are equal to zero, so fitness=fitness+1. 

Calculate_fitness functions return a list of all values of fitness function of the population. 

In Sorted_population functions add each bitstring and its value in dictionary to sort them depending on their value and returns sorted dictionary of the population. 

  

Step 3: Selection 

Select best two of the population “high values” and discard the rest  

Step 4: Crossover 

Crossover function takes two parents and do one point crossover by a loop start from index 5 to the end, forming 2 offspring. Each offspring part from first parent and other part from second parent. 

Step 5: Mutation 

Import random to choose randomly between offsprings and change the last index if it equal to zero, then it will equal to 1and vice-versal. 

 

Main function: Genetic_algorithm 

It contains all the steps and form the generation.  

 

Test the function: 

Call the functions two times to form two generations. 

 


 

  

 

 
