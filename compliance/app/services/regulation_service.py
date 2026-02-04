from compliance.app.models.regulation_model import Regulation
from compliance.app.utils.region_util import get_region_criteria
from typing import List
import logging

logger = logging.getLogger(__name__)

class RegulationService:
    @staticmethod
    def identify_applicable_regulations(region: str) -> List[Regulation]:
        """
        Identify applicable regulations based on the region.

        :param region: The region for which to identify regulations.
        :return: List of applicable Regulation objects.
        """
        try:
            criteria = get_region_criteria(region)
            regulations = Regulation.query.filter_by(country=criteria['country']).all()
            applicable_regulations = [reg for reg in regulations if reg.applicability_criteria == criteria['criteria']]
            logger.info("Identified {} applicable regulations for region {}", len(applicable_regulations), region)
            return applicable_regulations
        except Exception as e:
            logger.error("Failed to identify regulations: {}", e)
            return []