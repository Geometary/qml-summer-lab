# Question 1
target = QuantumCircuit(2)
target.h(range(2))
target.rx(np.pi / 2, range(2))
target.cx(0, 1)
target.p(np.pi, 1)
target.cx(0, 1)
target_unitary = qi.Operator(target)

# Question 2a
simulator = Aer.get_backend('qasm_simulator')
qpt_circs = process_tomography_circuits(target, measured_qubits=[0, 1])
qpt_job = execute(qpt_circs,simulator,seed_simulator=3145,seed_transpiler=3145,shots=8192)
qpt_result = qpt_job.result()

# Question 2b
fitter = ProcessTomographyFitter(qpt_result, qpt_circs)
qpt_lstsq = fitter.fit(method='lstsq')
fidelity = qi.average_gate_fidelity(qpt_lstsq, target_unitary)

# Question 3
noise_thermal = NoiseModel()
for j in range(4):
    noise_thermal.add_quantum_error(errors_reset[j], "reset", [j])
    noise_thermal.add_quantum_error(errors_measure[j], "measure", [j])
    noise_thermal.add_quantum_error(errors_u1[j], "u1", [j])
    noise_thermal.add_quantum_error(errors_u2[j], "u2", [j])
    noise_thermal.add_quantum_error(errors_u3[j], "u3", [j])
    for k in range(4):
        noise_thermal.add_quantum_error(errors_cx[j][k], "cx", [j, k])

# Question 4
np.random.seed(0)
noisy_qpt_job = execute(qpt_circs,simulator,seed_simulator=3145,seed_transpiler=3145,shots=8192, noise_model=noise_thermal)
noisy_qpt_result = noisy_qpt_job.result()
noisy_fitter = ProcessTomographyFitter(noisy_qpt_result, qpt_circs)
noisy_qpt_lstsq = noisy_fitter.fit(method='lstsq')
fidelity = qi.average_gate_fidelity(noisy_qpt_lstsq, target_unitary)

# Question 5
np.random.seed(0)
meas_cal_circs, meas_labels = complete_meas_cal(qubit_list=[0, 1])
meas_cal_job = execute(meas_cal_circs, simulator, seed_simulator=3145, seed_transpiler=3145, shots=8192, noise_model=noise_thermal)
meas_cal_result = meas_cal_job.result()
meas_cal_fitter = CompleteMeasFitter(meas_cal_result, meas_labels)
meas_filter = meas_cal_fitter.filter
miti_result = meas_filter.apply(noisy_qpt_result)
miti_fitter = ProcessTomographyFitter(miti_result, qpt_circs)
miti_lstsq = miti_fitter.fit(method='lstsq')
fidelity = qi.average_gate_fidelity(miti_lstsq, target_unitary)

