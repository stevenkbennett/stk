"""
Defines mutation operations via the ``Mutation`` class.

Extending MMEA: Adding mutation functions
-----------------------------------------
If a new mutation operation is to be added to MMEA it should be added
as a method in the ``Mutation`` class defined in this module. The only
requirement is that the first argument is ``macro_mol`` (excluding any
``self`` or ``cls`` arguments).

The naming requirement of ``macro_mol`` exists to help users identify 
which arguments are handled automatically by MMEA and which they need to 
define in the input file. The convention is that if the mutation 
function takes an argument called  ``macro_mol`` it does not have to be 
specified in the input file.

If the mutation function does not fit neatly into a single function
make sure that any helper functions are private, ie that their names 
start with a leading underscore. 

"""

import os
import numpy as np
from collections import Counter
import sys

from ..population import Population
from ..molecular import StructUnit3, Cage
from ..exception import MacroMolError
from ...convenience_tools import plot_counter

class Mutation:
    """
    Carries out mutations operations on a population.

    Instances of the ``Population`` class delegate mutation operations 
    to instances of this class. They do this by calling:
        
        >>> mutant_pop = pop.gen_mutants()
        
    which returns a new population consisting of molecules generated by
    performing mutation operations on members of ``pop``. This class
    invokes an instance of the ``Selection`` class to select molecules 
    for mutations. Both an instance of this class and the ``Selection``
    class are held in the `ga_tools` attribute of a ``Population`` 
    instance.
    
    This class is initialized with a list of  ``FunctionData`` 
    instances. Each ``FunctionData`` object holds the name of the 
    mutation function to be used by the population as well as any 
    additional parameters the function may require. Mutation functions 
    should be defined as methods within this class. 
    
    A mutation function from the list will be selected at random, with
    likelihoods modified if the user supplies a `weights` list during
    initialization.
    
    Members of this class are also initialized with an integer which
    holds the number of mutation operations to be performed each
    generation.
    
    Attributes
    ----------
    funcs : list of FunctionData instances
        This lists holds all the mutation functions which are to be 
        applied by the GA. One will be chosen at random when a mutation
        is desired. The likelihood can be modified by the optionally 
        supplied `weights` argument.
        
        The ``FunctionData`` object holding the name of the function
        chosen for mutation and any additional paramters and 
        corresponding values the function may require.
    
    num_mutations : int
        The number of mutations that needs to be performed each
        generation.
    
    n_calls : int
        The total number of times an instance of ``Mutation`` has been
        called during its lifetime.
    
    name : str
        A template string for naming ``MacroMolecule`` instances 
        produced during mutation.   
        
    weights : None or list of floats (default = None)
        When ``None`` each mutation function has equal likelihood of
        being picked. If `weights` is a list each float corresponds to
        the probability of selecting the mutation function at the
        corresponding index.
    
    """
    
    def __init__(self, funcs, num_mutations, weights=None):
        self.funcs = funcs
        self.weights = weights
        self.num_mutations = num_mutations
        self.n_calls = 0
        self.name = "mutation_{0}.mol"
    
    def __call__(self, population):
        """
        Carries out mutation operations on the supplied population.
        
        This function selects members of the population to be mutated
        and mutates them. This goes on until either all possible 
        molecules have been mutated or the required number of successful 
        mutation operations have been performed.
        
        The mutants generated are returned together in a ``Population`` 
        instance. Any molecules that are created as a result of mutation 
        that match a molecule present in the original population are 
        removed.

        Parameters
        ----------
        population : Population
            The population who's members are to be mutated.
            
        Returns
        -------
        Population
            A population with all the mutants generated held in the
            `members` attribute. This does not include mutants which
            correspond to molecules already present in `population`.            

        """
        
        parent_pool = population.select('mutation')
        mutant_pop = Population(population.ga_tools)
        counter = Counter()        
        
        num_mutations = 0
        for parent in parent_pool:
            counter.update([parent])
            func_data = np.random.choice(self.funcs, p=self.weights)
            func = getattr(self, func_data.name)            
           
            try:
                self.n_calls += 1
                mutant = func(parent, **func_data.params)
                mutant_pop.members.append(mutant)
                num_mutations += 1
                print('Mutation number {0}. Finish when {1}.'.format(
                                num_mutations, self.num_mutations))

                if num_mutations == self.num_mutations:
                    break

            except Exception as ex:
                MacroMolError(ex, parent, ('Error during mutation'
                    ' with {}.').format(func.__name__))

        mutant_pop -= population
        
        # Update counter with unselected members.
        for member in population:
            if member not in counter.keys():
                counter.update({member : 0})
        plot_counter(counter, os.path.join(os.getcwd(), 
                              'mutation_counter.png'))
        return mutant_pop

    def random_bb(self, macro_mol, database):
        """
        Substitutes a building-block* with a random one from a database.
        
        Parameters
        ----------
        macro_mol : Cage
            The cage who's building-block* will be exchanged. Note that
            the cage is not destroyed. It is used a template for a new
            cage.
            
        database : str
            The full path of the database from which a new 
            building-block* is to be found.
            
        Returns
        -------
        Cage
            A cage instance generated by taking all attributes of 
            `macro_mol` except its building-block* which is replaced by 
            a random building-block* from `database`.
        
        """

        _, lk = max(zip(macro_mol.topology.bb_counter.values(),
                        macro_mol.topology.bb_counter.keys()))
        
        _, og_bb = min(zip(macro_mol.topology.bb_counter.values(),
                        macro_mol.topology.bb_counter.keys()))        
        
        while True:
            try:
                bb_file = np.random.choice(os.listdir(database))
                bb_file = os.path.join(database, bb_file)
                bb = StructUnit3(bb_file)
                break
            
            except TypeError:
                continue        

        if len(og_bb.heavy_ids) != len(bb.heavy_ids):
            print(('MUTATION ERROR: Replacement building block does not'
                  ' have the same number of functional groups as the'
                  ' original building block.\n\nOriginal building '
                  'block:\n\n{}\n\nReplacement building block:\n\n'
                  '{}\n\n').format(og_bb.prist_mol_file, 
                                    bb.prist_mol_file))
            sys.exit()
            
        return Cage((bb, lk), type(macro_mol.topology),
            os.path.join(os.getcwd(), self.name.format(self.n_calls)))

    def random_lk(self, macro_mol, database):
        """
        Substitutes a linker with a random one from a database.
        
        Parameters
        ----------
        macro_mol : Cage
            The cage who's linker will be exchanged. Note that
            the cage is not destroyed. It is used a template for a new
            cage.
            
        database : str
            The full path of the database from which a new linker is to
            be found.
            
        Returns
        -------
        Cage
            A cage instance generated by taking all attributes of 
            `macro_mol` except its linker which is replaced by a random 
            linker from `database`.
        
        """        

        _, og_lk = max(zip(macro_mol.topology.bb_counter.values(),
                        macro_mol.topology.bb_counter.keys()))
        lk_type = type(og_lk)
        
        _, bb = min(zip(macro_mol.topology.bb_counter.values(),
                        macro_mol.topology.bb_counter.keys()))

        while True:
            try:
                lk_file = np.random.choice(os.listdir(database))
                lk_file = os.path.join(database, lk_file)
                lk = lk_type(lk_file)
                break
            
            except TypeError:
                continue
            
        if len(og_lk.heavy_ids) != len(lk.heavy_ids):
            print(('MUTATION ERROR: Replacement linker does not'
                  ' have the same number of functional groups as the'
                  ' original linker.\n\nOriginal linker:\n\n{}\n\n'
                  'Replacement linker:\n\n{}\n\n').format(
                                                   og_lk.prist_mol_file, 
                                                   lk.prist_mol_file))
            sys.exit()
        
        return Cage((bb, lk), type(macro_mol.topology),
            os.path.join(os.getcwd(), self.name.format(self.n_calls)))

    def random_cage_topology(self, macro_mol, topologies):
        """
        Changes `macro_mol` topology to a random one from `topologies`.
        
        Parameters
        ----------
        macro_mol : Cage
            The cage which is to be mutated.
        
        topologies : list of CageTopology instances        
            This lists holds the topology classes from which one is 
            selected at random to form a new cage. If the `macro_mol` 
            has a topology found in `topologies` that topology will not 
            be selected.
            
        Returns
        -------
        Cage
            A cage generated by initializing a new ``Cage`` instance
            with all the same paramters as `macro_mol` except for the
            topology.
        
        """
        
        tops = list(topologies)        
        tops.remove(type(macro_mol.topology))
        topology = np.random.choice(tops)        
        
        return Cage(macro_mol.building_blocks, topology, 
             os.path.join(os.getcwd(), self.name.format(self.n_calls)))

    def similar_bb(self, macro_mol, database):
        """
        Substitute the building-block* with similar one from `database`.
        
        All of the molecules in `database` are checked for similarity to
        the building-block* of `macro_mol`. The first time this mutation
        function is run on a cage, the most similar molecule in
        `database` is used to substitute the building-block*. The next
        time this mutation function is run on the same cage, the second 
        most similar molecule from `database` is used and so on.
        
        Parameters
        ----------
        macro_mol : Cage
            The cage which is to have its building-block* substituted.
            
        database : str
            The full path of the database from which molecules are used
            to substitute the building-block* of `macro_mol`.

        Modifies
        --------
        macro_mol._similar_bb_mols : generator
            Creates this attribute on the `macro_mol` instance. This 
            allows the function to keep track of which molecule from 
            `database` should be used in the substitution.
            
        Returns
        -------
        Cage
            A new cage with the same linker as `macro_mol` but a 
            different building-block*. The building-block* is selected 
            according to the description in this docstring.
        
        """
        
        # The idea here is to create a list of molecules from `database`
        # ordered by similarity to the building-block* of `macro_mol`. 
        # Each time this function is called on `cage` the next molecule 
        # from this list is used to substitute the building-block* of 
        # the cage and create a new mutant. The most elegant way to do 
        # this would be with a generator. However, because generators 
        # can't be dumped with ``pickle`` this is not possible. The idea 
        # would be to save the generator into an attribute of 
        # `macro_mol` and yield the next building-block* from it each 
        # time this function is used on that cage. Instead of the 
        # generator the list is saved to the attribute alongside the 
        # index which is to be accessed the next time this function is 
        # run on the same `macro_mol`.

        _, lk = max(zip(macro_mol.topology.bb_counter.values(),
                        macro_mol.topology.bb_counter.keys()))
        
        _, og_bb = min(zip(macro_mol.topology.bb_counter.values(),
                        macro_mol.topology.bb_counter.keys()))  
        
        if not hasattr(macro_mol, '_similar_bb_mols'):
            macro_mol._similar_bb_mols = (
                                   og_bb.similar_molecules(database), 0)
        
        sim_mols, cur_index = macro_mol._similar_bb_mols
        new_bb = StructUnit3(sim_mols[cur_index][-1])
        
        if len(og_bb.heavy_ids) != len(new_bb.heavy_ids):
            print(('MUTATION ERROR: Replacement building block does not'
                  ' have the same number of functional groups as the'
                  ' original building block.\n\nOriginal building '
                  'block:\n\n{}\n\nReplacement building block:\n\n'
                  '{}\n\n').format(og_bb.prist_mol_file, 
                                   new_bb.prist_mol_file))
            sys.exit()        
        
        macro_mol._similar_bb_mols = sim_mols, cur_index + 1
        
        return Cage((new_bb, lk), type(macro_mol.topology),
              os.path.join(os.getcwd(), self.name.format(self.n_calls)))
        
    def similar_lk(self, macro_mol, database):
        """
        Substitute the linker with a similar one from `database`.
        
        All of the molecules in `database` are checked for similarity to
        the linker of `macro_mol`. The first time this mutation function 
        is run on a cage, the most similar molecule in `database` is 
        used to substitute the linker. The next time this mutation 
        function is run on the same cage, the second most similar 
        molecule from `database` is used and so on.
        
        Parameters
        ----------
        macro_mol : Cage
            The cage which is to have its linker substituted.
            
        database : str
            The full path of the database from which molecules are used
            to substitute the linker of `macro_mol`.

        Modifies
        --------
        macro_mol._similar_lk_mols : generator
            Creates this attribute on the `macro_mol` instance. This 
            allows the function to keep track of which molecule from 
            `database` should be used in the substitution.
            
        Returns
        -------
        Cage
            A new cage with the same building-block* as `macro_mol` but 
            a different linker. The linker is selected according to the 
            description in this docstring.
        
        """

        # The idea here is to create a list of molecules from `database`
        # ordered by similarity to the linker of `macro_mol`. Each time 
        # this function is called on `macro_mol` the next molecule from 
        # this list is used to substitute the linker of the cage and 
        # create a new mutant. The most elegant way to do this would be 
        # with a generator. However, because generators can't be dumped 
        # with ``pickle`` this is not possible. The idea would be to 
        # save the generator into an attribute of `macro_mol` and yield 
        # the next linker from it each time this function is used on 
        # that cage. Instead of the generator the list is saved to the 
        # attribute alongside the index which is to be accessed the next 
        # time this function is run on the same `macro_mol`.

        _, og_lk = max(zip(macro_mol.topology.bb_counter.values(),
                        macro_mol.topology.bb_counter.keys()))
        lk_type = type(og_lk)
        
        _, bb = min(zip(macro_mol.topology.bb_counter.values(),
                        macro_mol.topology.bb_counter.keys()))  
        
        if not hasattr(macro_mol, '_similar_lk_mols'):
            macro_mol._similar_lk_mols = (
                            og_lk.similar_molecules(database), 0)

        sim_mols, cur_index = macro_mol._similar_lk_mols
        new_lk = lk_type(sim_mols[cur_index][-1])
        
        if len(og_lk.heavy_ids) != len(new_lk.heavy_ids):
            print(('MUTATION ERROR: Replacement linker does not'
                  ' have the same number of functional groups as the'
                  ' original linker.\n\nOriginal linker:\n\n{}\n\n'
                  'Replacement linker:\n\n{}\n\n').format(
                                                 og_lk.prist_mol_file, 
                                                 new_lk.prist_mol_file))
            sys.exit()
        
        macro_mol._similar_lk_mols = sim_mols, cur_index + 1
        
        return Cage((new_lk, bb), type(macro_mol.topology),
              os.path.join(os.getcwd(), self.name.format(self.n_calls)))