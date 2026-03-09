"""
Planner Agent Module

This module contains the PlannerAgent class for managing and planning tasks.
"""

import pandas as pd
from typing import List, Dict, Optional
from datetime import datetime


class PlannerAgent:
    """
    A planning agent that manages tasks and team assignments.
    """
    
    def __init__(self, tasks_file: str = "tasks.xlsx", team_file: str = "team.xlsx"):
        """
        Initialize the PlannerAgent.
        
        Args:
            tasks_file: Path to the tasks Excel file
            team_file: Path to the team Excel file
        """
        self.tasks_file = tasks_file
        self.team_file = team_file
        self.tasks = None
        self.team = None
        
    def load_data(self) -> None:
        """Load tasks and team data from Excel files."""
        try:
            self.tasks = pd.read_excel(self.tasks_file)
            self.team = pd.read_excel(self.team_file)
            print("Data loaded successfully")
        except FileNotFoundError as e:
            print(f"Error loading data: {e}")
            
    def get_tasks(self) -> Optional[pd.DataFrame]:
        """
        Get all tasks.
        
        Returns:
            DataFrame containing all tasks or None if not loaded
        """
        return self.tasks
    
    def get_team_members(self) -> Optional[pd.DataFrame]:
        """
        Get all team members.
        
        Returns:
            DataFrame containing all team members or None if not loaded
        """
        return self.team
    
    def assign_task(self, task_id: int, team_member: str) -> bool:
        """
        Assign a task to a team member.
        
        Args:
            task_id: ID of the task to assign
            team_member: Name of the team member
            
        Returns:
            True if assignment was successful, False otherwise
        """
        if self.tasks is None:
            print("Tasks not loaded. Call load_data() first.")
            return False
            
        try:
            self.tasks.loc[self.tasks['id'] == task_id, 'assigned_to'] = team_member
            self.tasks.loc[self.tasks['id'] == task_id, 'assigned_date'] = datetime.now()
            return True
        except Exception as e:
            print(f"Error assigning task: {e}")
            return False
    
    def get_pending_tasks(self) -> Optional[pd.DataFrame]:
        """
        Get all pending tasks.
        
        Returns:
            DataFrame containing pending tasks or None if not loaded
        """
        if self.tasks is None:
            return None
        return self.tasks[self.tasks['status'] == 'pending']
    
    def save_tasks(self) -> bool:
        """
        Save tasks back to Excel file.
        
        Returns:
            True if save was successful, False otherwise
        """
        if self.tasks is None:
            print("No tasks to save")
            return False
            
        try:
            self.tasks.to_excel(self.tasks_file, index=False)
            print("Tasks saved successfully")
            return True
        except Exception as e:
            print(f"Error saving tasks: {e}")
            return False


if __name__ == "__main__":
    # Example usage
    agent = PlannerAgent()
    agent.load_data()
    
    # Display pending tasks
    pending = agent.get_pending_tasks()
    if pending is not None:
        print("\nPending Tasks:")
        print(pending)

# Made with Bob
