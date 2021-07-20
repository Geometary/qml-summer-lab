# Exercise 1
def maxcut_cost_fn(graph: nx.Graph, bitstring: List[int]) -> float:
    """
    Computes the maxcut cost function value for a given graph and cut represented by some bitstring
    Args:
        graph: The graph to compute cut values for
        bitstring: A list of integer values '0' or '1' specifying a cut of the graph
    Returns:
        The value of the cut
    """
    #Get the weight matrix of the graph
    weight_matrix = nx.adjacency_matrix(graph).toarray()
    size = weight_matrix.shape[0]
    value = 0.
    
    # Computes the total weight of all cuts
    for i in range(size):
        for j in range(size):
            weight = weight_matrix[i, j] * bitstring[i] * (1 - bitstring[j])
            value += weight

    return value
  
  
  # Exercise 2
  def quadratic_program_from_graph(graph: nx.Graph) -> QuadraticProgram:
    """Constructs a quadratic program from a given graph for a MaxCut problem instance.
    Args:
        graph: Underlying graph of the problem.
    Returns:
        QuadraticProgram
    """
    #Get weight matrix of graph
    weight_matrix = nx.adjacency_matrix(graph)
    shape = weight_matrix.shape
    size = shape[0]
    #Build qubo matrix Q from weight matrix W
    qubo_matrix = np.zeros((size, size))
    qubo_vector = np.zeros(size)
    for i in range(size):
        for j in range(size):
            qubo_matrix[i, j] -= weight_matrix[i, j]
    for i in range(size):
        for j in range(size):
            qubo_vector[i] += weight_matrix[i, j]

    quadratic_program = QuadraticProgram('maxcut_problem')

    for var_index in range(size):
        name = 'x_{}'.format(var_index)
        quadratic_program.binary_var(name = name)
    quadratic_program.maximize(quadratic = qubo_matrix, linear = qubo_vector, constant = 0)

    
    return quadratic_program]
    
  
  # Exercise 3 (partial code)
  for i in range(p):

    #Apply R_Z rotational gates from cost layer

    #Apply R_ZZ rotational gates for entangled qubit rotations from cost layer
    for i_qubit in range(size):
        for j_qubit in range(size):
            matrix_term = qubo_matrix[i_qubit][j_qubit]
            angle_z = 0.5 * matrix_term * gammas[i]
            if (matrix_term == 0.0) or (i_qubit == j_qubit):
                continue
            else:
                qaoa_circuit.cx(j_qubit, i_qubit)
                qaoa_circuit.rz(angle_z, i_qubit)
                qaoa_circuit.cx(j_qubit, i_qubit)
                        
    # Apply single qubit X - rotations with angle 2*beta_i to all qubits
    angle_x = 2.0 * betas[i]
    qaoa_circuit.rx(angle_x, range(size))
    
    
 # Exercise 4 (partial code)
if cvar is None:
                #Calculate the mean of all cut values
                energy = sum(measured_cuts)/num_shots
            else:
                measured_cuts.sort(reverse=True)
                energy = sum(measured_cuts[:int(cvar * num_shots)]) / (cvar * num_shots)

     
  
