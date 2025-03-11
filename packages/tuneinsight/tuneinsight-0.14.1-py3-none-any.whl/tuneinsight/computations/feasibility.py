"""Implementation of the advanced feasibility operation."""

from typing import List, Union

from tuneinsight.computations.base import ModelBasedComputation
from tuneinsight.computations.aggregation import Aggregation
from tuneinsight.api.sdk import models
from tuneinsight.api.sdk.types import none_if_unset, false_if_unset, value_if_unset


class Feasibility(ModelBasedComputation):
    """The feasibility computation computes multiple statistics from a single query to the data.

    The values computed can include:
     - the record count across al instances (feasibility count),
     - the counts disaggregated by grouping parameters.
     - the counts disaggregated by instance.
    """

    def __init__(
        self,
        project: "Project",
        groups: Union[List[any], any] = None,
        include_global_count: bool = True,
        per_instance_breakdown: bool = True,
        local_breakdown: bool = False,
        dp_epsilon: float = None,
    ):
        """Creates a new feasibility computation on this project.

        Args:
            project (Project): The project to run the computation with.
            groups (Union[List[any], any], optional): Groups to use to disaggregate the counts by (by default, no groups).
                See `aggregation.py` for the syntax to use to specify this operation.
            include_global_count (bool, optional): whether to include the global count. Defaults to True.
            per_instance_breakdown (bool, optional): whether to also disaggregate the global count by instance. Defaults to True.
            local_breakdown (bool, optional): whether to also show the breakdown when running locally (one bin only). Defaults to False.
            dp_epsilon (float, optional): the privacy budget to use with this workflow. Defaults to None, in which case differential privacy is not used.
        """
        # convert groups to appropriate API representation
        groups = Aggregation._parse_groups(groups=groups)
        super().__init__(
            project,
            model_class=models.Feasibility,
            type=models.ComputationType.FEASIBILITY,
            groups=groups,
            global_count=include_global_count,
            per_instance_breakdown=per_instance_breakdown,
            local_breakdown=local_breakdown,
            dp_epsilon=dp_epsilon,
        )

    def _process_results(self, results):
        print(len(results))
        return results[0].get_dataframe()

    @classmethod
    def from_model(cls, project: "Project", model: models.Feasibility) -> "Aggregation":
        """Initializes a Feasibility from its API model."""
        model = models.Feasibility.from_dict(model.to_dict())
        with project.disable_patch():
            comp = cls(
                project,
                groups=none_if_unset(model.groups),
                include_global_count=value_if_unset(model.global_count, True),
                per_instance_breakdown=value_if_unset(
                    model.per_instance_breakdown, True
                ),
                local_breakdown=false_if_unset(model.local_breakdown),
                dp_epsilon=model.dp_epsilon,
            )
        comp._adapt(model)
        return comp
