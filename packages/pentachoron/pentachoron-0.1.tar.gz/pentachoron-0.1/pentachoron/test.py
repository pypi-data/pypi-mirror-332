from Hypercube.qubits.gates import QuantumGate

I_gate = (QuantumGate.Idrees_gate(5))

qc = QuantumGate.get_matrix(I_gate)


print(qc)
