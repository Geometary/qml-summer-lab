# Exercise 1-1
def lab1_ex1():
    qc = QuantumCircuit(1)
    qc.x(0)
    return qc

state = Statevector.from_instruction(lab1_ex1())
plot_bloch_multivector(state)


# Exercise 1-2
def lab1_ex2():
    qc = QuantumCircuit(1)
    qc.h(0)
    return qc

state = Statevector.from_instruction(lab1_ex2())
plot_bloch_multivector(state)


# Exercise 1-3
def lab1_ex3():
    qc = QuantumCircuit(1)
    qc.x(0)
    qc.h(0)
    return qc

state = Statevector.from_instruction(lab1_ex3())
plot_bloch_multivector(state)


# Exercise 1-4
def lab1_ex4():
    qc = QuantumCircuit(1)
    qc.h(0)
    qc.sdg(0)
    return qc
state = Statevector.from_instruction(lab1_ex4())
plot_bloch_multivector(state)


# Exercise 1-5
def lab1_ex5():
    qc = QuantumCircuit(2,2)
    qc.H(0)
    qc.cx()
    return qc

qc = lab1_ex5()
qc.draw()


# Exercise 1-6
def lab1_ex6():
    qc = QuantumCircuit(3)
    qc.x(0)
    qc.h(0)
    qc.cx(0, 1)
    qc.x(1)
    qc.cx(0, 2)
    return qc

qc = lab1_ex6()
qc.draw()


# Exercise 2-1
def lab1_ex7():
    min_nr_inputs = 2
    max_nr_inputs = 9
    return [min_nr_inputs, max_nr_inputs]
  
 
# Exercise 2-2 (4 parts)
n=4
def psi_0(n):
    qc = QuantumCircuit(n+1,n)
    qc.x(n)
    qc.h(n)
    return qc

dj_circuit = psi_0(n)
dj_circuit.draw()


def psi_1(n):
    qc = psi_0(n)
    for qubit in range(n):
        qc.h(qubit)
    return qc

dj_circuit = psi_1(n)
dj_circuit.draw()


def psi_2(oracle,n):
    qc = psi_1(n)
    qc.append(oracle, range(n+1)) 
    return qc

dj_circuit = psi_2(oracle, n)
dj_circuit.draw()


def lab1_ex8(oracle, n):
    qc = psi_2(oracle, n)
    for qubit in range(n):
        qc.h(qubit)
    qc.measure(range(n), range(n))
    return qc

dj_circuit = lab1_ex8(oracle, n)
dj_circuit.draw()
