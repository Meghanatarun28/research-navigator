class CitationFaithfulness:
    def evaluate(
        self,
        answer,
        citations,
    ):
        if not citations:
            return {"faithfulness": 0.0}

        return {"faithfulness": 1.0}
