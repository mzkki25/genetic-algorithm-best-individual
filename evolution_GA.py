import math
import random

def generate_chromosome(chromosome_size):
    chromosome = []
    for j in range(chromosome_size):
        chromosome.append(random.randint(0, 1))
    return chromosome

def calculate_fitness(x, y):
    heuristics = (math.pow(math.cos(math.radians(x)) + math.sin(math.radians(y)), 2)) / (math.pow(x, 2) + math.pow(y, 2) + 0.00000001)
    return 1 / (heuristics)

def binary_to_decimal(binary):
    decimal = 0
    for digit in binary:
        decimal = decimal*2 + int(digit)
    return str(decimal)

def biner_decode_chromosome(chromosome):
    X = binary_to_decimal(chromosome[:5])
    Y = binary_to_decimal(chromosome[5:])
    x = -5 + ((int(X)-0)/(31-0)) * (5-(-5))
    y = -5 + ((int(Y)-0)/(31-0)) * (5-(-5))
    return round(x, 5), round(y, 5)

def crossover(parent1, parent2):
    offspring1 = []
    offspring2 = []
    pc = 0.7
    for i in range(10):
        if random.random() < pc:
            offspring1.append(parent1[i])
            offspring2.append(parent2[i])
        else:
            offspring1.append(parent2[i])
            offspring2.append(parent1[i])
    return offspring1, offspring2

def mutatation(child1, child2):
    pm = 0.3
    for i in range(len(child1)):
        if random.random() < pm:
            child1[i] = str(1 - int(child1[i]))
    for i in range(len(child2)):
        if random.random() < pm:
            child2[i] = str(1 - int(child2[i]))
    return child1, child2

def main():
    population_size = 10
    chromosome_size = 10
    dict_population = {}

    print('='*76)
    print('{} {:^10} {} {:^10} {} {:^10} {} {:^10} {} {:^20} {}'.format('|', 'Population', '|', 'Chromosome', '|', 'X', '|', 'Y', '|', 'Fitness', '|'))
    print('='*76)
    for i in range(population_size):
        chromosome = "".join(list(map(str, [i for i in generate_chromosome(chromosome_size)])))
        x, y = biner_decode_chromosome(chromosome)
        dict_population[chromosome] = calculate_fitness(x, y)
        print('{} {:^10} {} {:^10} {} {:^10} {} {:^10} {} {:^20} {}'.format('|', i+1, '|', chromosome, '|', x, '|', y, '|', calculate_fitness(x, y), '|'))

    i = 0
    print('='*76)
    print('{} {:^10} {} {:^10} {} {:^10} {} {:^10} {} {:^20} {}'.format('|', 'Generation', '|', 'Chromosome', '|', 'X', '|', 'Y', '|', 'Fitness', '|'))
    print('='*76)
    while True:
        sort_population_highest = sorted(dict_population, key=dict_population.get, reverse=True)
        sort_population_lowest = sorted(dict_population, key=dict_population.get, reverse=False)
        parent1 = sort_population_highest[0]
        parent2 = sort_population_highest[1]

        offspring1, offspring2 = crossover(parent1, parent2)
        child1, child2 = mutatation(offspring1, offspring2)

        child1 = "".join(list(map(str, [i for i in child1])))
        child2 = "".join(list(map(str, [i for i in child2])))
        x1, y1 = biner_decode_chromosome(child1) 
        x2, y2 = biner_decode_chromosome(child2) 

        if (calculate_fitness(x1, y1) > min(dict_population.values()) and (calculate_fitness(x2, y2) > min(dict_population.values()))):
            dict_population.popitem()
            dict_population[child1] = calculate_fitness(x1, y1)
            dict_population[child2] = calculate_fitness(x2, y2)         

        dict_population = dict(sorted(dict_population.items(), key=lambda item: item[1], reverse=True))
        
        # j = 1
        # for key, value in dict_population.items():
        #     print(f'{j} Chromossome: {key}, X: {biner_decode_chromosome(key)[0]}, Y: {biner_decode_chromosome(key)[1]}, Fitness: {value}')
        #     j += 1

        print('{} {:^10} {} {:^10} {} {:^10} {} {:^10} {} {:^20} {}'.format('|', i+1, '|', sort_population_highest[0], '|', biner_decode_chromosome(parent1)[0], '|', biner_decode_chromosome(parent1)[1], '|', dict_population[sort_population_highest[0]], '|'))
        if dict_population[sort_population_highest[0]] > 60:
            break
        i += 1

if __name__ == '__main__':
    main()