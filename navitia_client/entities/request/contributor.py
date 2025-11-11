from dataclasses import dataclass
from typing import Dict, Any

from .base_entity_request import BaseEntityRequest


@dataclass
class ContributorRequest(BaseEntityRequest):
    """
    Request class for Contributor queries.

    This class only uses the pagination parameters (count, start_page)
    inherited from BaseEntityRequest.
    """

    def to_filters(self) -> Dict[str, Any]:
        """
        Converts the ContributorRequest instance into a dictionary of filters.

        Returns
        -------
        Dict[str, Any]
            A dictionary representation of the request filters.
        """
        return {
            "count": self.count,
            "start_page": self.start_page,
        }
