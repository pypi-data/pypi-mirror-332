from luna_sdk.schemas.solver_parameters.base_parameter import BaseParameter
from luna_sdk.schemas.solver_parameters.dwave import Embedding, SamplingParams
from pydantic import StringConstraints

import sys

if sys.version_info >= (3, 9):
    from typing import Annotated
else:
    from typing_extensions import Annotated


class QuantumAnnealingParameters(BaseParameter):
    """
    Parameters for the Quantum Annealing solver.

    Parameters
    ----------
    embedding: Embedding
        Parameters for the auto embedding.
    sampling_params: SamplingParams
        Parameters for the sampling. See https://docs.dwavesys.com/docs/latest/c_solver_parameters.html
        for more details.
    qpu_backend: str
        Specific D-Wave quantum processing unit (QPU) for your optimization
    """

    embedding: Embedding = Embedding()
    sampling_params: SamplingParams = SamplingParams()
    qpu_backend: Annotated[
        str, StringConstraints(strip_whitespace=True, min_length=1)
    ] = "default"
