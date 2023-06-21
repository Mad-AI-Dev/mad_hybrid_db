#!/usr/bin/env python3

"""
User Interface for Hybrid Database Model
This script creates a user-friendly command-line interface for interacting with the NLP system.
"""

# Standard library imports
import json

# Project specific imports
from utils.error_handling import ErrorHandler
from agents.nlp_agent_manager import NlpAgentManager

class UserInterface:
    """
    User interface class that allows users to interact with the NLP system.
    """

    def __init__(self, nlp_agent_manager: NlpAgentManager):
        """
        Constructor of the UserInterface class.

        Parameters:
            nlp_agent_manager (NlpAgentManager): An instance of the NlpAgentManager.
        """
        self.nlp_agent_manager = nlp_agent_manager
        self.error_handler = ErrorHandler()

    def start(self):
        """
        Starts the User Interface.
        """
        while True:
            try:
                # Ask the user to input a query
                query = input("\nPlease enter your query or 'quit' to exit: ")

                # Check if user wants to quit
                if query.lower() == 'quit':
                    break

                # Pass the query to the NlpAgentManager and get the response
                response = self.nlp_agent_manager.run_query(query)

                # Print the response
                print("\nResponse: ", json.dumps(response, indent=4))

            except Exception as e:
                self.error_handler.handle_error(e)

    def display_instructions(self):
        """
        Display the instructions to the user.
        """
        print("Welcome to the Hybrid Database Model for Extended NLP Context!")
        print("You can type in your queries in natural language.")
        print("Type 'quit' to exit the application.\n")

if __name__ == "__main__":
    # This block is to test the UserInterface independently.
    nlp_agent_manager = NlpAgentManager(None)  # Replace None with the NlpDatabaseManager object when integrated.
    ui = UserInterface(nlp_agent_manager)
    ui.display_instructions()
    ui.start()
