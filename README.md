## Ant Salesman Problem
This is the solution of asynchronous traveling salesman problem (ATSP)  
that uses ant colony optimization (ACO) written in Python 3.12.0

### How to run
This script needs two files aside of main.py to run properly:  
dataset file and properties file.

Dataset file must be a .csv file containing distances between nodes.
Values should be separated using single character, provided in properties file.

Properties file must contain seven pair in format KEY=VALUE, that are used in algorithm.  
Required keys are:  
- COLONY_SIZE (how many ants are in colony)
- DATA_FILE_DELIMITER (character that separates values in dataset)
- DATA_FILE_PATH (path to dataset file)
- ITERATION_NUMBER (how many iterations shoulb algorithm do)
- PHEROMONES_DEPOSIT_AMOUNT (how many pheromones ant deposits on its path)
- PHEROMONES_EVAPORATION_COEFFICIENT (how many pheromones evaporate between iterations)
- PHEROMONES_INITIAL_AMOUNT (initial amount of pheromones)

Before script is run, main.py file should be modified:  
in sixth line, "ant.properties" should be replaced with path to custom properties file.
