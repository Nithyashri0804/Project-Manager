# Project Manager Git Test

This is a project management system with agent-based planning capabilities.

## Structure

- `agents/` - Contains agent modules
  - `planner_agent.py` - Planning agent implementation
- `tasks.xlsx` - Task management spreadsheet
- `team.xlsx` - Team information spreadsheet

## Setup

1. Install required dependencies
2. Configure your team in `team.xlsx`
3. Add tasks to `tasks.xlsx`
4. Run the planner agent

## Usage

```python
from agents.planner_agent import PlannerAgent

# Initialize and use the planner agent
agent = PlannerAgent()