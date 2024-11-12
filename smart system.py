import random
# to calculate fitness for each bitstring
def fitness_function(initial):
    fitness=0
    for j in range(1,8):
      if  initial[j]==1 and initial[j+1]==0 and initial[j-1]==0 :
        fitness=fitness+1
    return fitness 
# to form a list of values to sort bitstrings according to their fitness           
def calculate_fitness(population):
    values_of_fitness=[]
    for i in range(len(population)):
       values_of_fitness.append(fitness_function(population[i]))
    print('values_of_fitness',values_of_fitness)
    return values_of_fitness
# sorting the population  
def my_function(k):
   return k['value'] 
def sorted_population(population,values):
   dict1={'bitstring':population[0],'value':values[0]}
   dict2={'bitstring':population[1],'value':values[1]}
   dict3={'bitstring':population[2],'value':values[2]}
   dict4={'bitstring':population[3],'value':values[3]}
   population_list=[dict1,dict2,dict3,dict4]
   population_list.sort(reverse=True,key=my_function)
   print('sorted_population',population_list)
   return population_list
# selecting the best two fitness function to be parent1,2 "selection"
def selection(population_list):
   parent1=population_list[0]['bitstring'] 
   parent2=population_list[1]['bitstring']
   print('chosen_parent:',parent1,parent2)
   return parent1,parent2
# to reproduce and form offsprings    
def crossover(parent1,parent2):
   offspring1=parent1.copy()
   offspring2=parent2.copy()
   for i in range(5,9):
      offspring1[i]=parent2[i]
      offspring2[i]=parent1[i]
   print('offspring1',offspring1,'offspring2',offspring2)   
   return offspring1,offspring2      
def mutation(child):
   if child[8]==0:
    child[8]=1
   else:
      child[8]=0 
   return child
# main function 'genetic' that has 4 steps: calculate fitness,selection,crossover,mutation    
def genetic_algorithm(population):
    list_of_values=calculate_fitness(population)
    population2=sorted_population(population,list_of_values)
    parent1,parent2=selection(population2)
    offspring1,offspring2=crossover(parent1,parent2)
    generation=[offspring1,offspring2]
    random_index=random.randint(0,1)
    generation[random_index]=mutation(generation[random_index])
    generation.append(parent1)
    generation.append(parent2)
    return generation
# test of functions 
bitstring1=[0,1,0,1,1,0,1,0,0]
bitstring2=[1,0,0,0,1,1,0,1,1]
bitstring3=[0,1,0,1,0,1,0,1,0]
bitstring4=[1,0,1,0,1,1,0,1,1]

initial_population=[bitstring1,bitstring2,bitstring3,bitstring4]
generation1=genetic_algorithm(initial_population)
print('generation1:',generation1)
generation2=genetic_algorithm(generation1)
print('generation2:',generation2)
