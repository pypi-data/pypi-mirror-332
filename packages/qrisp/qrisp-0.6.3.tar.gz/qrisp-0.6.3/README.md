<p align="center" width="100%"><img src="logo/qrisp_logo.png" width=30% height=30%></p>

Qrisp is an open-source python framework for high-level programming of Quantum computers.
By automating many steps one usually encounters when progrmaming a quantum computer, introducing quantum types, and many more features Qrisp makes quantum programming more user-friendly yet stays performant when it comes to compiling programs to the circuit level.

## Documentation
The full documentation, alongside with many tutorials and examples, is available under [Qrisp Documentation](https://www.qrisp.eu/).

## Installing
The easiest way to install Qrisp is via ``pip``
```bash
pip install qrisp
```
Qrisp has been confirmed to work with Python version 3.8, 3.9 & 3.10.

If you want to work with IQM quantum computers as a backend, you need to install additional dependencies using
```bash
pip install qrisp[iqm]
```

## First Quantum Program with Qrisp
The very first program you usually write, when learning a new programming language, is printing 'hello world'.
We want to do the same, but in a quantum way.

For this we can make use of the ``QuantumString`` type implemented in Qrisp. So we start by creating a new variable of the type QuantumString and assign the value 'hello world':
```python
from qrisp import QuantumString

q_str = QuantumString()
q_str[:] = "hello world"

print(q_str)
```

With the ``print(q_str)`` command, we automatically simulate the circuit generated when assigning ``hello world`` to ``q_str``. And es expected we get ``hello world`` with a probility of 1 as output:
```python
{'hello world': 1.0}
```

Now, let's make things more interesting: What happens, if we apply a Hadamard gate to the first qubit of the 7th character in our string?
```python
from qrisp import h, QuantumString

q_str = QuantumString()
q_str[:] = "hello world"
h(q_str[6][0])

print(q_str)
```
Go on, install Qrisp and try it yourself!

Of course, Qrisp offers much more than just handling strings with a quantum computer. More examples, like how to solve a quadratic equation with Grover's algorithm or how to solve the Travelling Salesman Problem on a quantum computer, can be found [here](https://www.qrisp.eu/general/tutorial.html).


## Authors and Citation
Qrisp was mainly devised and implemented by Raphael Seidel, supported by Sebastian Bock, Nikolay Tcholtchev, René Zander, Niklas Steinmann and Matic Petric.

If you have comments, questions or love letters, feel free to reach out to us:

raphael.seidel@fokus.fraunhofer.de

sebastian.bock@fokus.fraunhofer.de

nikolay.tcholtchev@fokus.fraunhofer.de

If you want to cite Qrisp in your work, please use:

```
@misc{seidel2024qrisp,
      title={Qrisp: A Framework for Compilable High-Level Programming of Gate-Based Quantum Computers}, 
      author={Raphael Seidel and Sebastian Bock and René Zander and Matic Petrič and Niklas Steinmann and Nikolay Tcholtchev and Manfred Hauswirth},
      year={2024},
      eprint={2406.14792},
      archivePrefix={arXiv},
      primaryClass={quant-ph},
      url={https://arxiv.org/abs/2406.14792}, 
}
```


## License
[Eclipse Public License 2.0](https://github.com/fraunhoferfokus/Qrisp/blob/main/LICENSE)

