#!/usr/bin/env python3

"""
This module defines the NLP Document Agent component of the Hybrid Database Model.

An NLP Document Agent is responsible for a subset of the context that is being handled
by the system, with the intent to handle and respond to queries within its area of expertise.
"""

# Standard library imports
import json
import os

# Project specific imports
from utils.error_handling import ErrorHandler

class NlpDocumentAgent:
    """
    A class to represent an NLP Document Agent.

    ...

    Attributes
    ----------
    context : dict
        A dictionary representing the context that the agent is responsible for.
    max_context_size : int
        An integer representing the maximum size of the agent's context.
    error_handler : ErrorHandler
        An instance of ErrorHandler to handle any errors during the agent's operations.

    Methods
    -------
    handle_query(query: str) -> dict:
        Handles the incoming query and returns the response.
    update_context(new_context: dict):
        Updates the agent's context with the new context.
    save_context():
        Saves the current context to a JSON file.
    load_context():
        Loads the context from a JSON file into the agent's context.
    """

    def __init__(self, context_filename: str, max_context_size: int = 1000):
        """
        Constructs all the necessary attributes for the NLP Document Agent object.

        Parameters:
            context_filename : str
                A string representing the filename of the agent's context JSON file.
            max_context_size : int, optional
                An integer representing the maximum size of the agent's context (default is 1000).
        """
        self.context_filename = context_filename
        self.max_context_size = max_context_size
        self.context = {}
        self.error_handler = ErrorHandler()

    def handle_query(self, query: str) -> dict:
        """
        Handles the incoming query and returns the response.

        Parameters:
            query : str
                A string representing the query.

        Returns:
            response : dict
                A dictionary representing the response.
        """
        # To be implemented based on the NLP library/framework chosen
        pass

    def update_context(self, new_context: dict):
        """
        Updates the agent's context with the new context.

        Parameters:
            new_context : dict
                A dictionary representing the new context.
        """
        try:
            if len(self.context) + len(new_context) > self.max_context_size:
                # Remove the oldest items in the context
                keys_to_remove = list(self.context.keys())[:len(new_context)]
                for key in keys_to_remove:
                    del self.context[key]
            
            # Add the new context
            self.context.update(new_context)
            
        except Exception as e:
            self.error_handler.handle_error(e)

    def save_context(self):
        """
        Saves the current context to a JSON file.
        """
        try:
            with open(self.context_filename, 'w') as file:
                json.dump(self.context, file, indent=4)
        except Exception as e:
            self.error_handler.handle_error(e)

    def load_context(self):
        """
        Loads the context from a JSON file into the agent's context.
        """
        try:
            if os.path.exists(self.context_filename):
                with open(self.context_filename, 'r') as file:
                    self.context = json.load(file)
        except Exception as e:
            self.error_handler.handle_error(e)
