#!/usr/bin/env python3

"""
Module: nlp_agent_manager.py

This module provides functionality to manage NLP Document Agents and distribute
queries among them. It receives the queries and forwards them to the NLP Database Manager.
"""

# Standard library imports
import json
from typing import Dict, Any

# Project specific imports
from .nlp_database_manager import NlpDatabaseManager
from utils.communication import Communication
from utils.error_handling import ErrorHandler

class NlpAgentManager:
    """
    A class to manage the interactions between NLP Document Agents.

    Attributes:
        db_manager (NlpDatabaseManager): An instance of NlpDatabaseManager to manage database queries.
        error_handler (ErrorHandler): An instance of ErrorHandler to manage exceptions.
    """

    def __init__(self, db_manager: NlpDatabaseManager):
        """Initialize NlpAgentManager with a NlpDatabaseManager."""
        self.db_manager = db_manager
        self.error_handler = ErrorHandler()

    def run_query(self, query: Dict[str, Any]) -> Dict[str, Any]:
        """
        Receives a query and forwards it to the NlpDatabaseManager.

        Args:
            query (dict): A dictionary containing the query parameters.

        Returns:
            dict: The response from the NlpDatabaseManager.
        """
        try:
            # Forward the query to the NlpDatabaseManager
            response = self.db_manager.run_query(query)

            # Return the response
            return response

        except Exception as e:
            self.error_handler.handle_error(e)
            return {'status': 'error', 'message': 'Failed to run query.'}

    def communicate(self, message: Dict[str, Any]) -> Dict[str, Any]:
        """
        Communicate with other agents using JSON.

        Args:
            message (dict): A dictionary containing the message to send.

        Returns:
            dict: The response from the recipient.
        """
        try:
            # Convert the message to JSON and send it
            Communication.send_json(message)

            # Wait for a response and return it
            response = Communication.receive_json()
            return response

        except Exception as e:
            self.error_handler.handle_error(e)
            return {'status': 'error', 'message': 'Failed to communicate.'}
