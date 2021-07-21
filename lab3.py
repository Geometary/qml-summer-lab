# Exercise 3-1
x = [-0.1,0.2]
ex1_circuit = ZZFeatureMap(feature_dimension=2, reps=4)
ex1_circuit = ex1_circuit.bind_parameters(x)
ex1_circuit.draw('mpl')

# Exercise 3-2
x = [-0.1,0.2]
y = [0.4,-0.6]

zz_map_ex = ZZFeatureMap(feature_dimension=2, reps=4)
zz_kernel_ex = QuantumKernel(feature_map = zz_map_ex, quantum_instance = Aer.get_backend('statevector_simulator'))
zz_circuit_ex = zz_kernel_ex.construct_circuit(x, y)
backend_ex = Aer.get_backend('qasm_simulator')
job_ex = execute(zz_circuit_ex, backend_ex, shots=8192, seed_simulator=1024, seed_transpiler=1024)
counts_ex = job_ex.result().get_counts(zz_circuit_ex)

amplitude = counts_ex['00'] / sum(counts_ex.values())
