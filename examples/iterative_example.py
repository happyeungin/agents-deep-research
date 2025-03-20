"""
Example usage of the DeepResearcher to produce a report.

See iterative_output.txt for the console output from running this script, and iterative_output.pdf for the final report
"""

import asyncio
from app.iterative_research import IterativeResearcher

manager = IterativeResearcher(
    max_iterations=5,
    max_time_minutes=10,
    verbose=True,
    tracing=True
)

query = "Write a report on Plato - who was he, what were his main works " \
        "and what are the main philosophical ideas he's known for"
output_length = "1000 words"
output_instructions = ""

report = asyncio.run(
    manager.run(
        query, 
        output_length=output_length, 
        output_instructions=output_instructions
    )
)

print("\n=== Final Report ===")
print(report)