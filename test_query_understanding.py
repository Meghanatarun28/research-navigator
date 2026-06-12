from research_navigator.retrieve.query_understanding import (
    QueryUnderstanding,
)

parser = QueryUnderstanding()

print(parser.extract_filters("recent transformer papers"))

print(parser.extract_filters("attention mechanisms"))
