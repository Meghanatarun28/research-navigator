from typing import Dict


class QueryUnderstanding:
    def extract_filters(
        self,
        query: str,
    ) -> Dict[str, int]:
        query = query.lower()

        filters: Dict[str, int] = {}

        if "recent" in query:
            filters["year_gte"] = 2023

        return filters
