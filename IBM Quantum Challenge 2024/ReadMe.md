<img src="https://github.com/arishma108/arishma108/blob/main/assets/IBMQC24.png" height="100%" width="100%">    

As a Quantum Developer, we’re not just making discoveries about how the world works—we’re trying to use quantum mechanics as a tool to solve meaningful problems and enact positive change in the world.
We’ve entered the era of quantum utility—for the first time, quantum computers can do things beyond the abilities of brute-force classical computing. 
Now, we’re looking for quantum advantage, where quantum computers are the best way to solve the problem.

This challenge is to uncover and implement quantum algorithms and apply them to real-world use cases
Solving problems with real-world impact means thinking about who we’re impacting and how.

***UN Declares 2025 International Year Of Quantum Science And Technology*** 
June 7, 2024, the United Nations officially recognised the importance and potential of quantum technologies after a General Assembly meeting declared 2025 as the International Year of Quantum Science and Technology (IYQ) 

We MUST research and develop technology responsibly. 
To that end, I have been researching the societal implications of quantum computing, and my role as a quantum computing developer in mitigating potentially undesired consequences of the technology. 


### LAB 0 Hello World
Use the challenge notebooks, grade work, and manage the general flow of setting up, running, and evaluating the results of my quantum code.
- Configure my challenge environment
- Generate a two-qubit Bell state using Qiskit patterns
- Map circuits and operators
- Optimize the circuit
- Execute the circuit
- Post-process the results

Successfully created a two-qubit Bell state, and showed that it was properly entangled by visualizing the operators. 

### LAB 1 Qiskit 1.0
Set up quantum states using Qiskit, and implement an optimization algorithm using variational quantum eigensolvers (VQE).

### LAB 2 Transpilation with Qiskit 1.0
Contributing my own transpiler to the Qiskit ecosystem.
Key features of Qiskit 1.0's transpiler - the four pre-defined transpilation paths, the six stages of transpilation, and building my own transpiler pass manager with the flexibility of Qiskit 1.0 transpiler.

### LAB 3 Sneak Preview of Upcoming Qiskit Beta Features
I get exclusive access to groundbreaking new features in development for the Qiskit stack to explore and test these features, and see how they could enhance quantum development workflows. 
Keep in mind that these features are in beta, so I encountered some bugs, nonetheless I dived in, experimented fearlessly, and pushed the boundaries of what's possible in quantum computing.
- AI-Powered Transpilation with Qiskit Transpiler Service
-- Set up the Qiskit Transpiler service to transpile our circuit on cloud
-- Transpile my quantum circuits by utilizing AI to optimize gate counts and circuit depth.
-- Experimenting with various high-depth and high-width circuits using the Qiskit Transpiler Service!

- Qiskit Code Assistant
-- Generate a 3 qubit GHZ circuit.
-- Design a 2 qubit CH gate with only CX and RY gate.
-- Generate a quantum circuit that produces a q-sphere resembling the Qiskit logo

- Circuit Kinitting Toolbox
-- Toffoli circuit with circuit cutting

- Qiskit Serverless
-- Part 1: Creating and deploying programs on Qiskit Serverless
-- Part 2: Deploying parallel workflows on Qiskit Serverless

### LAB 4 Testing a Variational Quantum Classifier on a Real Backend
In this lab, I build and train a simple Variational Quantum Classifier (VQC) on an ideal backend using the Qiskit Patterns workflow. 
Once the VQC is trained, I will experience how the presence of noise has an impact on its performance. 
Finally, I learn how to reduce the depth of the VQC and then run the resulting circuit on quantum hardware to see how error suppression and error mitigation techniques have an impact on the results.

### BONUS LAB Scaling to 50 qubits!
Scale up the results from Lab 4 to 50 qubits! 

As the system size grows, we'll need to optimize our Variational Quantum Classifier (VQC) and reduce its depth. This is crucial because the mapping used for the GHZ state scales linearly with the number of qubits. We’ll adapt our quantum circuits to fit this larger scale and while we're provide with pre-trained optimal parameters. The task is to test the functionality of the VQC in this extended qubit range.

Why is this important? Simulating more than 50 qubits is a significant feat in the quantum world and not many have ventured into running circuits of this size—it's a unique opportunity to push the boundaries of what's achievable in quantum simulations.

Please note, the bonus lab is intended only for those who have successfully completed Lab 4, as it builds directly on the foundations and solutions we've developed. Diving into this advanced challenge and joining the elite group experimenting at this level in quantum computing!













