class Genetic_algorithm:

    def init(population_size, layers, initializing_range):
      import random
      global weights_amount
      global full_population_weights
      global full_population_biases
      weights_amount=0
      for i1 in range(len(layers)-1):
        weights_amount+=layers[i1]*layers[i1+1]
      full_population_weights=[]
      full_population_biases=[]
      for i2 in range(population_size):
            current_network_initializing_weights=[]
            current_network_initializing_biases=[]
            for i3 in range(weights_amount):
                current_network_initializing_weights.append(round(random.uniform(initializing_range[0], initializing_range[1]), 3))
                current_network_initializing_biases.append(round(random.uniform(initializing_range[0], initializing_range[1]), 3))
            full_population_weights.append(current_network_initializing_weights)
            full_population_biases.append(current_network_initializing_biases)

    def run_network(network_num_fitness, INPUTS, layers):
        global outputs
        outputs=[False, False, True, True, False]
        running_network_weights=full_population_weights[network_num_fitness]
        running_network_biases=full_population_biases[network_num_fitness]
        NODES_PROSCESSED=INPUTS
        nodes_proscessing=NODES_PROSCESSED
        computatinoal_part=0
        for i1 in range(len(layers)-1):
            nodes_proscessing=[]
            for i2 in range(layers[i1+1]):
                node_in_next_layer_VALUE=0
                for i3 in range(layers[i1]):
                    edge_value=running_network_weights[computatinoal_part]*NODES_PROSCESSED[i3]
                    edge_value+=running_network_biases[computatinoal_part]
                    computatinoal_part+=1
                    node_in_next_layer_VALUE+=edge_value
                nodes_proscessing.append(node_in_next_layer_VALUE)
            NODES_PROSCESSED=nodes_proscessing
        outputs=NODES_PROSCESSED

    def make_new_generation(selection_method, creation_method, fitness_scores, population_size, full_mutation_rate_percent, partial_mutation_rate_percent, partial_mutation_rate_change_range):
        import random
        if selection_method=='Top 2':
           parent1_ID=fitness_scores.index(max(fitness_scores))
           parent2_fitness=-1
           for i in range(len(fitness_scores)):
               if fitness_scores[i]>parent2_fitness and not i==parent1_ID:
                   parent2_fitness=fitness_scores[i]
                   parent2_ID=i

        elif selection_method=='Random Weighted':
            picking_list=[]
            for i in range(len(fitness_scores)):
                for i3 in range(fitness_scores[i]):
                    picking_list.append(i)
            parent1_ID=picking_list[random.randint(0,len(picking_list)-1)]
            parent2_ID=picking_list[random.randint(0, len(picking_list)-1)]

        else:
            raise Exception('That is not a valid selection method. Enter either the string "Top 2" or enter the string "Random Weighted" for the selection method.')

        parent1_weights, parent1_biases=full_population_weights[parent1_ID], full_population_biases[parent1_ID]
        parent2_weights, parent2_biases=full_population_weights[parent2_ID], full_population_biases[parent2_ID]

        if creation_method=='Sclice':
            parent1_contribution=round(weights_amount/2, 0)
            parent2_contribution=weights_amount-parent1_contribution
            for i1 in range(population_size):
                CHILD_WEIGHTS=[]
                CHILD_BIASES=[]
                for i2 in range(weights_amount):
                    if i2<parent1_contribution:
                        parent_num=0
                    else:
                        parent_num=1
                    if round(random.uniform(0,100), 3)<=full_mutation_rate_percent:
                        CHILD_WEIGHTS.append(round(random.uniform(-2,2), 3))
                        CHILD_BIASES.append(round(random.uniform(-2,2), 3))
                    elif round(random.uniform(0,100), 3)<=partial_mutation_rate_percent:
                        if parent_num==0:
                            CHILD_WEIGHTS.append(parent1_weights[i2]+round(random.uniform(partial_mutation_rate_change_range[0], partial_mutation_rate_change_range[1]),4))
                            CHILD_BIASES.append(parent1_biases[i2]+round(random.uniform(partial_mutation_rate_change_range[0], partial_mutation_rate_change_range[1]),4))
                        else:
                            CHILD_WEIGHTS.append(parent2_weights[i2]+round(random.uniform(partial_mutation_rate_change_range[0], partial_mutation_rate_change_range[1]),4))
                            CHILD_BIASES.append(parent2_biases[i2]+round(random.uniform(partial_mutation_rate_change_range[0], partial_mutation_rate_change_range[1]),4))
                    else:
                        if parent_num==0:
                            CHILD_WEIGHTS.append(parent1_weights[i2])
                            CHILD_BIASES.append(parent1_biases[i2])
                        else:
                            CHILD_WEIGHTS.append(parent2_weights[i2])
                            CHILD_BIASES.append(parent2_biases[i2])
                full_population_weights.append(CHILD_WEIGHTS)
                full_population_biases.append(CHILD_BIASES)

        elif creation_method=='Random':
            for i1 in range(population_size):
                CHILD_WEIGHTS=[]
                CHILD_BIASES=[]
                for i2 in range(weights_amount):
                    parent_num=random.randint(0,1)
                    if round(random.uniform(0,100), 3)<=full_mutation_rate_percent:
                        CHILD_WEIGHTS.append(round(random.uniform(-2,2), 3))
                        CHILD_BIASES.append(round(random.uniform(-2,2), 3))
                    elif round(random.uniform(0,100), 3)<=partial_mutation_rate_percent:
                        if parent_num==0:
                            CHILD_WEIGHTS.append(parent1_weights[i2]+round(random.uniform(partial_mutation_rate_change_range[0], partial_mutation_rate_change_range[1]),4))
                            CHILD_BIASES.append(parent1_biases[i2]+round(random.uniform(partial_mutation_rate_change_range[0], partial_mutation_rate_change_range[1]),4))
                        else:
                            CHILD_WEIGHTS.append(parent2_weights[i2]+round(random.uniform(partial_mutation_rate_change_range[0], partial_mutation_rate_change_range[1]),4))
                            CHILD_BIASES.append(parent2_biases[i2]+round(random.uniform(partial_mutation_rate_change_range[0], partial_mutation_rate_change_range[1]),4))
                    else:
                        if parent_num==0:
                            CHILD_WEIGHTS.append(parent1_weights[i2])
                            CHILD_BIASES.append(parent1_biases[i2])
                        else:
                            CHILD_WEIGHTS.append(parent2_weights[i2])
                            CHILD_BIASES.append(parent2_biases[i2])
                full_population_weights.append(CHILD_WEIGHTS)
                full_population_biases.append(CHILD_BIASES)
            print(full_population_weights, full_population_biases)
        
        else:
            raise Exception('You enetered an Invalid crossover method. To not get this error, give either the string "Sclice" or the string "Random" for the corresponding method.')

Genetic_algorithm.init(3, [2,2,2], (-2,2))
for i in range(3):
    Genetic_algorithm.run_network(i, [5,7], [2,2,2])
    Genetic_algorithm.make_new_generation("Top 2", 'Random', [5,3,10], 3, 10, 50, (-2,2))