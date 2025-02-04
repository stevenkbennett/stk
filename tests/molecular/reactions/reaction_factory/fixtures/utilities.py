import stk

construction_state = stk.construction_state
_GraphState = construction_state.graph_state._GraphState
_MoleculeState = construction_state.molecule_state._MoleculeState


class MockGraphState(_GraphState):
    def __init__(self, edges):
        self._edges = edges


class MockConstructionState(stk.ConstructionState):
    def __init__(
        self,
        edges,
        edge_functional_groups,
        position_matrix=None,
    ):
        self._molecule_state = _MoleculeState()
        self._molecule_state._position_matrix = position_matrix
        self._molecule_state._edge_functional_groups = (
            edge_functional_groups
        )
        self._graph_state = MockGraphState(edges)


class MockEdge(stk.Edge):
    def __init__(self, id, periodicity):
        self._id = id
        self._periodicity = periodicity
