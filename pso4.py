from __future__ import division
import random
import math
import sys

def squareFunction (location):
    total = 0
    for i in range(len(location)):
        total += location[i]**2
    return total

def ackleyFunction (location):
    a = 20
    b = 0.2
    c = 2.0 * math.pi
    firstSum = 0.0
    secondSum = 0.0
    for i in range(len(location)):
        firstSum += location[i]**2.0
        secondSum += math.cos(c * location[i])
    n = float(len(location))
    return -a * math.exp(-b * math.sqrt(firstSum / n)) - math.exp(secondSum / n) + a + math.e

def sphereFunction (location):
    total = 0
    for i in range(len(location)):
        total += i * location[i]**2
    return total

class particle:
    def __init__(self, location):
        self.dimensions = len(location)
        self.velocity = []
        self.best_location = []
        self.best_cost = -1
        self.current_location = []
        self.cost = -1
        for i in range (0, self.dimensions):
            self.velocity.append(random.uniform(0, 0))
            self.current_location.append(location[i])
     
    # updating velocity
    def velocity_update(self,global_best_location):
        intertia_coefficient = 0.5
        p_acceleration_coefficient = 2
        s_acceleration_coefficient = 2
        for i in range(0,self.dimensions):
            r1=random.uniform(0, 1)
            r2=random.uniform(0, 1)
            cognitive_component = p_acceleration_coefficient * r1 * (self.best_location[i]-self.current_location[i])
            social_component = s_acceleration_coefficient * r2 * (global_best_location[i]-self.current_location[i])
            self.velocity[i]=intertia_coefficient * self.velocity[i] + cognitive_component + social_component
            
    # updating location
    def location_update(self,lowerlimit, upperlmit):
       for i in range(0,self.dimensions):
           self.current_location[i]=self.current_location[i] + self.velocity[i]

           if self.current_location[i] < lowerlimit:
               self.current_location[i]=lowerlimit

           if self.current_location[i] > upperlimit:
               self.current_location[i]= upperlimit
           
    # distance function
    def run_cost_function(self,costFunc):
       self.cost = costFunc(self.current_location)

       # checkng current location is best
       if self.cost < self.best_cost or self.best_cost == -1:
           self.best_location = self.current_location
           self.best_cost = self.cost
           
class PSO():
    def __init__(self, costfunc, locations, lowerlimit, upperlimit, population_size, maximum_iteration):
    
        dimensions = len(locations)
        global_best_cost = -1
        global_best_location = []
        
        house_of_particle = []
        for i in range (0, population_size):
            house_of_particle.append(particle(locations))

        i = 0
        while i < maximum_iteration:
            for j in range (0, population_size):
                house_of_particle[j].run_cost_function(costfunc)
                if (house_of_particle[j].cost) < global_best_cost or global_best_cost == -1:
                    global_best_cost = float(house_of_particle[j].cost)
                    global_best_location = list(house_of_particle[j].current_location)
                    
            for k in range (0, population_size):
                house_of_particle[k].velocity_update(global_best_location)
                house_of_particle[k].location_update(lowerlimit, upperlimit)
            print "iteration i = " , i , "   " , global_best_location
            print "iteration i = " , i , "   " , global_best_cost
            i+=1

        print global_best_location
        print global_best_cost

#input from user

print sys.argv

locations = list(map(int, sys.argv[1].split(',')))
lowerlimit = int(sys.argv[2])
upperlimit = int(sys.argv[3])
no_of_locations = int(sys.argv[4])
maximum_iterations = int(sys.argv[5])
choose_function = int(sys.argv[6])
print choose_function
if choose_function == 1:
    print "Square function", locations, lowerlimit, upperlimit, no_of_locations, maximum_iterations
    PSO(squareFunction, locations, lowerlimit, upperlimit, no_of_locations, maximum_iterations)
if choose_function == 2:
    print "Ackley function", locations, lowerlimit, upperlimit, no_of_locations, maximum_iterations
    PSO(ackleyFunction, locations, lowerlimit, upperlimit, no_of_locations, maximum_iterations)
if choose_function == 3:
    print "Sphere Function", locations, lowerlimit, upperlimit, no_of_locations, maximum_iterations
    PSO(sphereFunction, locations, lowerlimit, upperlimit, no_of_locations, maximum_iterations)
#locations=[10, 12]
#lowerlimit = -10
#upperlimit = 10
#no_of_birds = 30
#maximum_iterations = 15
#PSO(squareFunction, locations, lowerlimit, upperlimit, no_of_birds, maximum_iterations)
#PSO(ackleyFunction, locations, lowerlimit, upperlimit, no_of_birds, maximum_iterations)
#PSO(sphereFunction, locations, lowerlimit, upperlimit, no_of_birds, maximum_iterations)
