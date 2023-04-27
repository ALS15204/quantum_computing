from matplotlib import pyplot
from qiskit import QuantumRegister, ClassicalRegister, Aer, execute, QuantumCircuit

# Initializing backend simulators to visualize circuits
S_simulator = Aer.backends(name='statevector_simulator')[0]
Q_simulator = Aer.backends(name='qasm_simulator')[0]
# Creating quantum registers to hold quibits
q = QuantumRegister(2)
# Creating classical registers to hold bits
c = ClassicalRegister(2)
# Create a quantum circuit with these registers
qc = QuantumCircuit(q, c)
qc.id(q[0])

# NOT gate
qc.x(q[0])

qc.cx(q[0], q[1])

qc.h([q[0], q[1]])
qc.draw(output="mpl")
pyplot.show()

