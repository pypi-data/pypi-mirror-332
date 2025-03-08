"""
\********************************************************************************
* Copyright (c) 2025 the Qrisp authors
*
* This program and the accompanying materials are made available under the
* terms of the Eclipse Public License 2.0 which is available at
* http://www.eclipse.org/legal/epl-2.0.
*
* This Source Code may also be made available under the following Secondary
* Licenses when the conditions for such availability set forth in the Eclipse
* Public License, v. 2.0 are satisfied: GNU General Public License, version 2
* with the GNU Classpath Exception which is
* available at https://www.gnu.org/software/classpath/license.html.
*
* SPDX-License-Identifier: EPL-2.0 OR GPL-2.0 WITH Classpath-exception-2.0
********************************************************************************/
"""

import time

import numpy as np
from scipy.optimize import minimize
from sympy import Symbol

from qrisp import QuantumArray, h, x, parallelize_qc
from qrisp.algorithms.qaoa.qaoa_benchmark_data import QAOABenchmark


class QAOAProblem:
    r"""
    Central structure to facilitate treatment of QAOA problems.

    This class encapsulates the cost operator, mixer operator, and classical cost function for a specific QAOA problem instance. It also provides methods to set the initial state preparation function, classical cost post-processing function, and optimizer for the problem.

    For a quick demonstration, we import the relevant functions from already implemented problem instances:
        
    ::
        
        from networkx import Graph

        G = Graph()

        G.add_edges_from([[0,3],[0,4],[1,3],[1,4],[2,3],[2,4]])

        from qrisp.qaoa import (QAOAProblem, 
                                create_maxcut_cost_operator, 
                                create_maxcut_cl_cost_function,
                                RX_mixer)

        maxcut_instance = QAOAProblem(cost_operator = create_maxcut_cost_operator(G),
                                       mixer = RX_mixer,
                                       cl_cost_function = create_maxcut_cl_cost_function(G))
        
        
        from qrisp import QuantumVariable
        
        res = maxcut_instance.run(qarg = QuantumVariable(5),
                                  depth = 4, 
                                  max_iter = 25)
        
        print(res)
        #Yields: {'11100': 0.2847, '00011': 0.2847, '10000': 0.0219, '01000': 0.0219, '00100': 0.0219, '11011': 0.0219, '10111': 0.0219, '01111': 0.0219, '00010': 0.02, '11110': 0.02, '00001': 0.02, '11101': 0.02, '00000': 0.0173, '11111': 0.0173, '10010': 0.0143, '01010': 0.0143, '11010': 0.0143, '00110': 0.0143, '10110': 0.0143, '01110': 0.0143, '10001': 0.0143, '01001': 0.0143, '11001': 0.0143, '00101': 0.0143, '10101': 0.0143, '01101': 0.0143, '11000': 0.0021, '10100': 0.0021, '01100': 0.0021, '10011': 0.0021, '01011': 0.0021, '00111': 0.0021}
        
    For an in-depth tutorial, make sure to check out :ref:`MaxCutQAOA`!
        
    Parameters
    ----------
    cost_operator : function
        A function receiving a :ref:`QuantumVariable` or :ref:`QuantumArray` and parameter $\gamma$. This function performs the application of the cost operator.
    mixer : function
        A function receiving a :ref:`QuantumVariable` or :ref:`QuantumArray` and parameter $\beta$. This function performs the application mixing operator.
    cl_cost_function : function
        The classical cost function for the specific QAOA problem instance, which takes a dictionary of measurement results as input.
    init_function : function, optional
        A function receiving a :ref:`QuantumVariable` or :ref:`QuantumArray` for preparing the inital state.
        By default, the uniform superposition state $\ket{+}^n$ is prepared.
    callback : Booelan, optional
        If ``True``, intermediate results are stored. The default is ``False``.

    """
    
    def __init__(self, cost_operator, mixer, cl_cost_function, init_function = None, callback=False):
        self.cost_operator = cost_operator
        self.mixer = mixer
        self.cl_cost_function = cl_cost_function
        
        self.init_function = init_function
        self.cl_post_processor = None
        self.init_type = 'random'

        # parameters for callback
        self.callback = callback
        self.optimization_params = []
        self.optimization_costs = []

    def set_callback(self):
        """
        Sets ``callback=True`` for saving intermediate results.

        """

        self.callback = True

    def set_init_function(self, init_function):
        """
        Set the initial state preparation function for the QAOA problem.

        Parameters
        ----------
        init_function : function
            The initial state preparation function for the specific QAOA problem instance.
        """
        self.init_function = init_function

    def computeParams(self, p, dt):
        """
        Compute the angle parameters gamma and beta based on the given inputs. Used for the TQA warm starting the initial parameters for QAOA.

        Parameters
        ----------
        p : int
            The number of partitions for the time interval.
        dt : float
            The time step.

        Returns
        -------
        np.array
            A concatenated numpy array of gamma and beta values.
        """
        t = (np.arange(1, p + 1) - 0.5)/p
        gamma = t * dt
        beta = (1 - t) * dt
        return  np.concatenate((gamma,beta)) 
    

    def compile_circuit(self, qarg, depth):
        """
        Compiles the circuit that is evaluated by the :meth:`run <qrisp.qaoa.QAOAProblem.run>` method.

        Parameters
        ----------
        qarg : :ref:`QuantumVariable` or :ref:`QuantumArray`
            The argument the cost function is called on.
        depth : int
            The amount of QAOA layers.

        Returns
        -------
        compiled_qc : :ref:`QuantumCircuit`
            The parametrized, compiled quantum circuit without measurements.
        list[sympy.Symbol]
            A list of the parameters that appear in ``compiled_qc``.

        Examples
        --------
        
        We create a MaxCut instance and compile the circuit:
        
            
        >>> from networkx import Graph
        >>> G = Graph([(0,1),(1,2),(2,0)])
        >>> from qrisp.qaoa import maxcut_problem
        >>> from qrisp import QuantumVariable
        >>> p = 5
        >>> qaoa_instance = maxcut_problem(G)
        >>> qarg = QuantumVariable(len(G))
        >>> qrisp_qc, symbols = qaoa_instance.compile_circuit(qarg, p)
        >>> print(qrisp_qc)
                     ┌───┐┌────────┐┌────────┐                          »
        qarg_dupl.0: ┤ H ├┤ gphase ├┤ gphase ├──■────────────────────■──»
                     ├───┤└────────┘└────────┘┌─┴─┐┌──────────────┐  │  »
        qarg_dupl.1: ┤ H ├────────────────────┤ X ├┤ P(2*gamma_0) ├──┼──»
                     ├───┤                    └───┘└──────────────┘┌─┴─┐»
        qarg_dupl.2: ┤ H ├─────────────────────────────────────────┤ X ├»
                     └───┘                                         └───┘»
        «                                            ┌──────────────┐   ┌────────┐   »
        «qarg_dupl.0: ───────■────────────────────■──┤ Rx(2*beta_0) ├───┤ gphase ├───»
        «                  ┌─┴─┐      ┌────────┐  │  └──────────────┘   └────────┘   »
        «qarg_dupl.1: ─────┤ X ├──────┤ gphase ├──┼─────────■────────────────────────»
        «             ┌────┴───┴─────┐└────────┘┌─┴─┐     ┌─┴─┐      ┌──────────────┐»
        «qarg_dupl.2: ┤ P(2*gamma_0) ├──────────┤ X ├─────┤ X ├──────┤ P(2*gamma_0) ├»
        «             └──────────────┘          └───┘     └───┘      └──────────────┘»
        «             ┌────────┐                                          »
        «qarg_dupl.0: ┤ gphase ├──────────────────■────────────────────■──»
        «             └────────┘┌──────────────┐┌─┴─┐┌──────────────┐  │  »
        «qarg_dupl.1: ────■─────┤ Rx(2*beta_0) ├┤ X ├┤ P(2*gamma_1) ├──┼──»
        «               ┌─┴─┐   ├──────────────┤└───┘└──────────────┘┌─┴─┐»
        «qarg_dupl.2: ──┤ X ├───┤ Rx(2*beta_0) ├─────────────────────┤ X ├»
        «               └───┘   └──────────────┘                     └───┘»
        «                                            ┌──────────────┐   ┌────────┐   »
        «qarg_dupl.0: ───────■────────────────────■──┤ Rx(2*beta_1) ├───┤ gphase ├───»
        «                  ┌─┴─┐      ┌────────┐  │  └──────────────┘   └────────┘   »
        «qarg_dupl.1: ─────┤ X ├──────┤ gphase ├──┼─────────■────────────────────────»
        «             ┌────┴───┴─────┐└────────┘┌─┴─┐     ┌─┴─┐      ┌──────────────┐»
        «qarg_dupl.2: ┤ P(2*gamma_1) ├──────────┤ X ├─────┤ X ├──────┤ P(2*gamma_1) ├»
        «             └──────────────┘          └───┘     └───┘      └──────────────┘»
        «             ┌────────┐                                          »
        «qarg_dupl.0: ┤ gphase ├──────────────────■────────────────────■──»
        «             └────────┘┌──────────────┐┌─┴─┐┌──────────────┐  │  »
        «qarg_dupl.1: ────■─────┤ Rx(2*beta_1) ├┤ X ├┤ P(2*gamma_2) ├──┼──»
        «               ┌─┴─┐   ├──────────────┤└───┘└──────────────┘┌─┴─┐»
        «qarg_dupl.2: ──┤ X ├───┤ Rx(2*beta_1) ├─────────────────────┤ X ├»
        «               └───┘   └──────────────┘                     └───┘»
        «                                            ┌──────────────┐   ┌────────┐   »
        «qarg_dupl.0: ───────■────────────────────■──┤ Rx(2*beta_2) ├───┤ gphase ├───»
        «                  ┌─┴─┐      ┌────────┐  │  └──────────────┘   └────────┘   »
        «qarg_dupl.1: ─────┤ X ├──────┤ gphase ├──┼─────────■────────────────────────»
        «             ┌────┴───┴─────┐└────────┘┌─┴─┐     ┌─┴─┐      ┌──────────────┐»
        «qarg_dupl.2: ┤ P(2*gamma_2) ├──────────┤ X ├─────┤ X ├──────┤ P(2*gamma_2) ├»
        «             └──────────────┘          └───┘     └───┘      └──────────────┘»
        «             ┌────────┐                                          »
        «qarg_dupl.0: ┤ gphase ├──────────────────■────────────────────■──»
        «             └────────┘┌──────────────┐┌─┴─┐┌──────────────┐  │  »
        «qarg_dupl.1: ────■─────┤ Rx(2*beta_2) ├┤ X ├┤ P(2*gamma_3) ├──┼──»
        «               ┌─┴─┐   ├──────────────┤└───┘└──────────────┘┌─┴─┐»
        «qarg_dupl.2: ──┤ X ├───┤ Rx(2*beta_2) ├─────────────────────┤ X ├»
        «               └───┘   └──────────────┘                     └───┘»
        «                                            ┌──────────────┐   ┌────────┐   »
        «qarg_dupl.0: ───────■────────────────────■──┤ Rx(2*beta_3) ├───┤ gphase ├───»
        «                  ┌─┴─┐      ┌────────┐  │  └──────────────┘   └────────┘   »
        «qarg_dupl.1: ─────┤ X ├──────┤ gphase ├──┼─────────■────────────────────────»
        «             ┌────┴───┴─────┐└────────┘┌─┴─┐     ┌─┴─┐      ┌──────────────┐»
        «qarg_dupl.2: ┤ P(2*gamma_3) ├──────────┤ X ├─────┤ X ├──────┤ P(2*gamma_3) ├»
        «             └──────────────┘          └───┘     └───┘      └──────────────┘»
        «             ┌────────┐                                          »
        «qarg_dupl.0: ┤ gphase ├──────────────────■────────────────────■──»
        «             └────────┘┌──────────────┐┌─┴─┐┌──────────────┐  │  »
        «qarg_dupl.1: ────■─────┤ Rx(2*beta_3) ├┤ X ├┤ P(2*gamma_4) ├──┼──»
        «               ┌─┴─┐   ├──────────────┤└───┘└──────────────┘┌─┴─┐»
        «qarg_dupl.2: ──┤ X ├───┤ Rx(2*beta_3) ├─────────────────────┤ X ├»
        «               └───┘   └──────────────┘                     └───┘»
        «                                            ┌──────────────┐                »
        «qarg_dupl.0: ───────■────────────────────■──┤ Rx(2*beta_4) ├────────────────»
        «                  ┌─┴─┐      ┌────────┐  │  └──────────────┘                »
        «qarg_dupl.1: ─────┤ X ├──────┤ gphase ├──┼─────────■────────────────────────»
        «             ┌────┴───┴─────┐└────────┘┌─┴─┐     ┌─┴─┐      ┌──────────────┐»
        «qarg_dupl.2: ┤ P(2*gamma_4) ├──────────┤ X ├─────┤ X ├──────┤ P(2*gamma_4) ├»
        «             └──────────────┘          └───┘     └───┘      └──────────────┘»
        «                                  
        «qarg_dupl.0: ─────────────────────
        «                  ┌──────────────┐
        «qarg_dupl.1: ──■──┤ Rx(2*beta_4) ├
        «             ┌─┴─┐├──────────────┤
        «qarg_dupl.2: ┤ X ├┤ Rx(2*beta_4) ├
        «             └───┘└──────────────┘
        """
        
        temp = list(qarg.qs.data)
        
        # Define QAOA angle parameters gamma and beta for QAOA circuit
        
        gamma = [Symbol("gamma_" + str(i)) for i in range(depth)]
        beta = [Symbol("beta_" + str(i)) for i in range(depth)]
        

        # Prepare initial state - if no init_function is specified, prepare uniform superposition
        if self.init_function is not None:
            self.init_function(qarg)
        elif self.init_type=='tqa': # Prepare the ground state (eigenvalue -1) of the X mixer
            x(qarg)
            h(qarg)
        else:
            h(qarg)
            
        # Apply p layers of phase separators and mixers
        for i in range(depth):                           
            self.cost_operator(qarg, gamma[i])
            self.mixer(qarg, beta[i])

        # Compile quantum circuit with intended measurements    
        if isinstance(qarg, QuantumArray):
            intended_measurement_qubits = sum([list(qv) for qv in qarg.flatten()], [])
        else:
            intended_measurement_qubits = list(qarg)
        
        compiled_qc = qarg.qs.compile(intended_measurements=intended_measurement_qubits)
        
        qarg.qs.data = temp
        
        return compiled_qc, gamma + beta

    #def optimization_routine(self, qarg, compiled_qc, symbols , depth, mes_kwargs, max_iter):    
    def optimization_routine(self, qarg, depth, mes_kwargs, max_iter, optimizer="COBYLA"): 
        """
        Wrapper subroutine for the optimization method used in QAOA. The initial values are set and the optimization via ``COBYLA`` is conducted here.

        Parameters
        ----------
        qarg : :ref:`QuantumVariable` or :ref:`QuantumArray`
            The argument the cost function is called on.
        complied_qc : :ref:`QuantumCircuit`
            The compiled quantum circuit.
        depth : int
            The amont of QAOA layers.
        symbols : list
            The list of symbols used in the quantum circuit.
        mes_kwargs : dict, optional
            The keyword arguments for the measurement function. Default is an empty dictionary, as defined in previous functions.
        max_iter : int, optional
            The maximum number of iterations for the optimization method. Default is 50, as defined in previous functions.
        init_type : string, optional
            Specifies the way the initial optimization parameters are chosen. Available are ``random`` and ``TQA``. The default is ``random``.
        optimizer : str, optional
            Specifies the optimization routine. Available are, e.g., ``COBYLA``, ``COBYQA``, ``Nelder-Mead``. 
            The Default is "COBYLA". 

        Returns
        -------
        res_sample
            The optimized parameters of the problem instance.
        """

        # Define optimization wrapper function to be minimized using QAOA
        def optimization_wrapper(theta, qc, symbols, qarg, mes_kwargs):
            """
            Wrapper function for the optimization method used in QAOA.

            This function calculates the value of the classical cost function after post-processing if a post-processing function is set, otherwise it calculates the value of the classical cost function.

            Parameters
            ----------
            theta : list
                The list of angle parameters gamma and beta for the QAOA circuit.
            qc : :ref:`QuantumCircuit
                The compiled quantum circuit.
            symbols : list
                The list of symbols used in the quantum circuit.
            qarg_dupl : :ref:`QuantumVariable` or :ref:`QuantumArray`
                The duplicated quantum argument to which the quantum circuit is applied.
            mes_kwargs : dict
                The keyword arguments for the measurement function.

            Returns
            -------
            float
                The expected value of the classical cost function.
            """         
            subs_dic = {symbols[i] : theta[i] for i in range(len(symbols))}
            
            res_dic = qarg.get_measurement(subs_dic = subs_dic, precompiled_qc = qc, **mes_kwargs)
            
            cl_cost = self.cl_cost_function(res_dic)

            if self.callback:
                self.optimization_costs.append(cl_cost)
            
            if self.cl_post_processor is not None:
                return self.cl_post_processor(cl_cost)
            else:
                return cl_cost
            
        def tqa_angles(p, qc, symbols, qarg_dupl, mes_kwargs, steps=10): #qarg only before
            """
            Compute the optimal parameters for the Trotterized Quantum Annealing (`TQA <https://quantum-journal.org/papers/q-2021-07-01-491/>`_) algorithm.

            The function first creates a linspace array `dt` from 0.1 to 1 with `steps` steps. 
            Then for each `dt_` in `dt`, it computes the parameters `x` using the `computeParams` 
            function and calculates the energy `energy_` using the `optimization_wrapper` function. 
            The energy values are stored in the `energy` list. The `dt_max` corresponding to the 
            minimum energy is found and used to compute the optimal parameters which are returned.

            Parameters
            ----------
            p : int
                The number of partitions for the time interval.
            qc : :ref:`QuantumCircuit`
                The quantum circuit for the specific problem instance.
            symbols : list
                The list of symbols in the quantum circuit.
            qarg_dupl : :ref:`QuantumVariable` or :ref:`QuantumArray`
                The duplicated quantum argument to which the quantum circuit is applied.
            mes_kwargs : dict
                The measurement keyword arguments.
            steps : int, optional
                The number of steps for the linspace function, default is 10.

            Returns
            -------
            np.array
                A concatenated numpy array of optimal gamma and beta values.
            """
            dt = np.linspace(0.1, 1, steps)
            energy = []
            for dt_ in dt:      
                x = self.computeParams(p,dt_)
                energy_ = optimization_wrapper(x,qc,symbols,qarg_dupl,mes_kwargs)
                energy.append(energy_)
            
            idx = np.argmin(energy)
            dt_max = dt[idx]
            return self.computeParams(p,dt_max)


        compiled_qc, symbols = self.compile_circuit(qarg, depth)
        
        # Set initial random values for optimization parameters 
        # init_point = np.pi * np.random.rand(2 * depth)/2
        
        # initial point is set here, potentially subject to change

        if self.init_type=='random':
            # Set initial random values for optimization parameters
            init_point = np.pi * np.random.rand(2 * depth)/2

        elif self.init_type=='tqa':
            # TQA initialization
            init_point = tqa_angles(depth,compiled_qc, symbols, qarg, mes_kwargs)


        # Perform optimization using COBYLA method

        compiled_qc, symbols = self.compile_circuit(qarg, depth)
        # Perform optimization using COBYLA method
        res_sample = minimize(optimization_wrapper,
                            init_point, 
                            method=optimizer, 
                            options={'maxiter':max_iter}, 
                            args = (compiled_qc, symbols, qarg, mes_kwargs))
            
        return res_sample['x']
        

    def run(self, qarg, depth, mes_kwargs = {}, max_iter = 50, init_type = "random", optimizer="COBYLA"):
        """
        Run the specific QAOA problem instance with given quantum arguments, depth of QAOA circuit,
        measurement keyword arguments (mes_kwargs) and maximum iterations for optimization (max_iter).
        
        Parameters
        ----------
        qarg : :ref:`QuantumVariable` or :ref:`QuantumArray`
            The quantum argument to which the QAOA circuit is applied.
        depth : int
            The amount of QAOA layers.
        mes_kwargs : dict, optional
            The keyword arguments for the measurement function. Default is an empty dictionary.
        max_iter : int, optional
            The maximum number of iterations for the optimization method. Default is 50.
        init_type : string, optional
            Specifies the way the initial optimization parameters are chosen. Available are ``random`` and ``tqa``. The default is ``random``: 
            The parameters are initialized uniformly at random in the interval $[0,\pi/2]$.
            For ``tqa``, the parameters are chosen based on the `Trotterized Quantum Annealing <https://quantum-journal.org/papers/q-2021-07-01-491/>`_ protocol.
            If ``tqa`` is chosen, and no ``init_function`` for the :ref:`QAOAProblem` is specified, the $\ket{-}^n$ state is prepared (the ground state for the X mixer).
        optimizer : str, optional
            Specifies the `optimization routine <https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.minimize.html>`_. 
            Available are, e.g., ``COBYLA``, ``COBYQA``, ``Nelder-Mead``. The Default is ``COBYLA``.

        Returns
        -------
        opt_res : dict
            The optimal result after running QAOA problem for a specific problem instance. It contains the measurement results after applying the optimal QAOA circuit to the quantum argument.
        """

        self.init_type = init_type

        # Delete callback
        self.optimization_params = []
        self.optimization_costs = []

        #alternative to everything below:
        #bound_qc = self.train_circuit(qarg, depth)
        #opt_res = bound_qc(qarg).get_measurement(**mes_kwargs)
        #return opt_res
        if not "shots" in mes_kwargs:
            mes_kwargs["shots"] = 5000
        
        #res_sample = self.optimization_routine(qarg, compiled_qc, symbols , depth,  mes_kwargs, max_iter)
        res_sample = self.optimization_routine(qarg, depth, mes_kwargs, max_iter, optimizer)
        optimal_theta = res_sample 

        
        # Prepare initial state - if no init_function is specified, prepare uniform superposition
        if self.init_function is not None:
            self.init_function(qarg)
        elif self.init_type=='tqa': # Prepare the ground state (eigenvalue -1) of the X mixer
            x(qarg)
            h(qarg)
        else:
            h(qarg)

        # Apply p layers of phase separators and mixers    
        for i in range(depth):                          
            self.cost_operator(qarg, optimal_theta[i])
            self.mixer(qarg, optimal_theta[i+depth])
        opt_res = qarg.get_measurement(**mes_kwargs)
        return opt_res
    
    def train_function(self, qarg, depth, mes_kwargs = {}, max_iter = 50, init_type = "random", optimizer="COBYLA"):
        r"""
        This function allows for training of a circuit with a given ``QAOAProblem`` instance. It returns a function that can be applied to a ``QuantumVariable``,
        such that it represents a solution to the problem instance. When applied to a ``QuantumVariable``, the function therefore prepares the state
         
        .. math::
         
            \ket{\psi_p}=U_M(B,\beta_p)U_P(C,\gamma_p)\dotsb U_M(B,\beta_1)U_P(C,\gamma_1)\ket{\psi_0}

        with optimized parameters $\gamma, \beta$.

        Parameters
        ----------
        qarg : :ref:`QuantumVariable`
            The quantum argument to which the QAOA circuit is applied.
        depth : int
            The amount of QAOA layers.
        mes_kwargs : dict, optional
            The keyword arguments for the measurement function. Default is an empty dictionary.
        max_iter : int, optional
            The maximum number of iterations for the optimization method. Default is 50.
        init_type : string, optional
            Specifies the way the initial optimization parameters are chosen. Available are ``random`` and ``tqa``. The default is ``random``: 
            The parameters are initialized uniformly at random in the interval $[0,\pi/2]$.
            For ``tqa``, the parameters are chosen based on the `Trotterized Quantum Annealing <https://quantum-journal.org/papers/q-2021-07-01-491/>`_ protocol.
            If ``tqa`` is chosen, and no ``init_function`` for the :ref:`QAOAProblem` is specified, the $\ket{-}^n$ state is prepared (the ground state for the X mixer).
        optimizer : str, optional
            Specifies the `optimization routine <https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.minimize.html>`_. 
            Available are, e.g., ``COBYLA``, ``COBYQA``, ``Nelder-Mead``. The Default is ``COBYLA``.
        
        Returns
        -------
        circuit_generator : function
            A function that can be applied to a ``QuantumVariable`` , with optimized parameters for the problem instance. The ``QuantumVariable`` then represents a solution of the problem.

        Examples
        --------

        We create a :ref:`MaxIndepSet <maxIndepSetQAOA>` instance and train a ciruit with the :ref:`QAOAProblem` instance.
        
        ::
            
            from qrisp import QuantumVariable
            from qrisp.qaoa import QAOAProblem, RZ_mixer, create_max_indep_set_cl_cost_function, create_max_indep_set_mixer, max_indep_set_init_function
            import networkx as nx
            import matplotlib.pyplot as plt
            
            G = nx.erdos_renyi_graph(9, 0.5, seed =  133)

            qaoa_instance = QAOAProblem(cost_operator=RZ_mixer,
                                            mixer=create_max_indep_set_mixer(G),
                                            cl_cost_function=create_max_indep_set_cl_cost_function(G),
                                            init_function=max_indep_set_init_function)

            # create a blueprint-qv to train the circuit with the problem instance 
            qarg_new = QuantumVariable(G.number_of_nodes())
            training_func = qaoa_instance.train_function(qarg=qarg_new, depth=5)

            # apply the trained function to a new qv 
            qarg_trained = QuantumVariable(G.number_of_nodes())
            training_func(qarg_trained)

            # get the measurement results 
            opt_res = qarg_trained.get_measurement()

            cl_cost = create_max_indep_set_cl_cost_function(G)

            print("5 most likely solutions")
            max_five = sorted(opt_res.items(), key=lambda item: item[1], reverse=True)[:5]
            for res, prob in max_five:
                print([index for index, value in enumerate(res) if value == '1'], prob, cl_cost({res : 1}))

        """

        self.init_type = init_type

        compiled_qc, symbols = self.compile_circuit(qarg, depth)
        res_sample = self.optimization_routine(qarg, depth, mes_kwargs, max_iter, optimizer)
        
        def circuit_generator(qarg_gen):
            # Prepare initial state - if no init_function is specified, prepare uniform superposition
            if self.init_function is not None:
                self.init_function(qarg_gen)
            elif self.init_type=='tqa': # Prepare the ground state (eigenvalue -1) of the X mixer
                x(qarg_gen)
                h(qarg_gen)
            else:
                h(qarg_gen)

            for i in range(depth): 
                
                self.cost_operator(qarg_gen, res_sample[i])
                self.mixer(qarg_gen, res_sample[i+depth])
            
        return circuit_generator
    
    def benchmark(self, qarg, depth_range, shot_range, iter_range, optimal_solution, repetitions = 1, mes_kwargs = {}, init_type = "random", optimizer="COBYLA"):
        """
        This method enables convenient data collection regarding performance of the implementation.

        Parameters
        ----------
        qarg : QuantumVariable or QuantumArray
            The quantum argument, the benchmark is executed on. Compare to the :meth:`.run <qrisp.qaoa.QAOAProblem.run>` method.
        depth_range : list[int]
            A list of integers indicating, which depth parameters should be explored. Depth means the amount of QAOA layers.
        shot_range : list[int]
            A list of integers indicating, which shots parameters should be explored. Shots means the amount of repetitions, the backend performs per iteration.
        iter_range : list[int]
            A list of integers indicating, what iterations parameter should be explored. Iterations means the amount of backend calls, the optimizer is allowed to do.
        optimal_solution : -
            The optimal solution to the problem. Should have the same type as the keys of the result of ``qarg.get_measurement()``.
        repetitions : int, optional
            The amount of repetitions, each parameter constellation should go though. Can be used to get a better statistical significance. The default is 1.
        mes_kwargs : dict, optional
            The keyword arguments, that are used for the ``qarg.get_measurement``. The default is {}.
        init_type : string, optional
            Specifies the way the initial optimization parameters are chosen. Available are ``random`` and ``tqa``. The default is ``random``: 
            The parameters are initialized uniformly at random in the interval $[0,\pi/2]$.
            For ``tqa``, the parameters are chosen based on the `Trotterized Quantum Annealing <https://quantum-journal.org/papers/q-2021-07-01-491/>`_ protocol.
            If ``tqa`` is chosen, and no ``init_function`` for the :ref:`QAOAProblem` is specified, the $\ket{-}^n$ state is prepared (the ground state for the X mixer).
        optimizer : str, optional
            Specifies the `optimization routine <https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.minimize.html>`_. 
            Available are, e.g., ``COBYLA``, ``COBYQA``, ``Nelder-Mead``. The Default is ``COBYLA``.

        Returns
        -------
        :ref:`QAOABenchmark`
            The results of the benchmark.
            
        Examples
        --------
        
        We create a MaxCut instance and benchmark several parameters
        
        ::
            
            from qrisp import *
            from networkx import Graph
            G = Graph()

            G.add_edges_from([[0,3],[0,4],[1,3],[1,4],[2,3],[2,4]])

            from qrisp.qaoa import maxcut_problem

            max_cut_instance = maxcut_problem(G)

            benchmark_data = max_cut_instance.benchmark(qarg = QuantumVariable(5),
                                       depth_range = [3,4,5],
                                       shot_range = [5000, 10000],
                                       iter_range = [25, 50],
                                       optimal_solution = "11100",
                                       repetitions = 2
                                       )
        
        We can investigate the data by calling ``visualize``:
        
        ::
            
            benchmark_data.visualize()
        
        .. image:: benchmark_plot.png
            
        The :ref:`QAOABenchmark` class contains a variety of methods to help 
        you drawing conclusions from the collected data. Make sure to check them out!

        """
        
        data_dict = {"layer_depth" : [],
                     "circuit_depth" : [],
                     "qubit_amount" : [],
                     "shots" : [],
                     "iterations" : [],
                     "counts" : [],
                     "runtime" : [],
                     "cl_cost" : []
                     }
        
        for p in depth_range:
            for s in shot_range:
                for it in iter_range:
                    for k in range(repetitions):
                        
                        if isinstance(qarg, QuantumArray):
                            qarg_dupl = QuantumArray(qtype = qarg.qtype, shape = qarg.shape)
                            mes_qubits = sum([qv.reg for qv in qarg_dupl.flatten()], [])
                        else:
                            qarg_dupl = qarg.duplicate()
                            mes_qubits = list(qarg_dupl)
                            
                        start_time = time.time()
                        
                        temp_mes_kwargs = dict(mes_kwargs)
                        temp_mes_kwargs["shots"] = s
                        if init_type=='random':
                            counts = self.run(qarg=qarg_dupl, depth = p, max_iter = it, mes_kwargs = temp_mes_kwargs, init_type='random', optimizer=optimizer)
                        elif init_type=='tqa':
                            counts = self.run(qarg=qarg_dupl, depth = p, max_iter = it, mes_kwargs = temp_mes_kwargs, init_type='tqa', optimizer=optimizer)
                        final_time = time.time() - start_time
                        
                        compiled_qc = qarg_dupl.qs.compile(intended_measurements=mes_qubits)
                        
                        data_dict["layer_depth"].append(p)
                        data_dict["circuit_depth"].append(compiled_qc.depth())
                        data_dict["qubit_amount"].append(compiled_qc.num_qubits())
                        data_dict["shots"].append(s)
                        data_dict["iterations"].append(it)
                        data_dict["counts"].append(counts)
                        data_dict["runtime"].append(final_time)
                        
                        
        return QAOABenchmark(data_dict, optimal_solution, self.cl_cost_function)
    

    def visualize_cost(self):
        """
        Visualizes the cost during the optimization process. Can only be used if ``callback=True``.

        """

        import matplotlib.pyplot as plt

        if not self.callback:
            raise Exception("Visualization can only be performed for a QAOA instance with callback=True")
        
        x = list(range(len(self.optimization_costs)))
        y = self.optimization_costs
        plt.scatter(x, y, color='#20306f',marker="o", linestyle='solid', linewidth=1, label='QAOA cost')
        plt.xlabel("Iterations", fontsize=15, color="#444444")
        plt.ylabel("Cost", fontsize=15, color="#444444")
        plt.tick_params(axis='both', labelsize=12)
        plt.legend(fontsize=12, labelcolor="#444444")
        plt.grid()

        plt.show()
