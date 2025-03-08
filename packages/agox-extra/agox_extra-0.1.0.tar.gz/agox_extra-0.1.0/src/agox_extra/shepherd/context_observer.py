import numpy as np
from shepherd.experiment import ExperimentContext

from agox import Observer, State
from agox.databases import Database


class ContextObserver(Observer):
    name = "ContextObserver"

    def __init__(self, context: ExperimentContext, max_iterations: int = 500, database: Database = None) -> None:
        super().__init__()
        self.context = context
        self.max_iterations = max_iterations
        self.database = database
        self.add_observer_method(self.update_context, sets={}, gets={}, order=0)

    @Observer.observer_method
    def update_context(self, state: State) -> None:
        progress = f"{(self.get_iteration_counter() / self.max_iterations)*100:05.1f}%"
        self.context.update_progress(progress)

        candidates = self.database.get_all_candidates()
        if len(candidates) > 0:
            lowest_energy = np.min([c.get_potential_energy() for c in candidates])
            self.context.add("lowest_energy", f"{lowest_energy:.3f}")

        
