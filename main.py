#!/usr/bin/env python3

"""
Hybrid Database Model for Extended NLP Context
Main script for the Hybrid Database Model application.

This script ties together the functionality of NLP Agent Manager, NLP Database Manager, and NLP Document Agents.
"""

# Standard library imports
import os
import sys
import json

# Project specific imports
from agents.nlp_agent_manager import NlpAgentManager
from agents.nlp_database_manager import NlpDatabaseManager
from agents.nlp_document_agent import NlpDocumentAgent
from utils.communication import Communication
from utils.error_handling import ErrorHandler
from interfaces.user_interface import UserInterface

# Setup the error handling
error_handler = ErrorHandler()

def main():
    """
    The main function of the application.
    """
    try:
        # Load NLP Database
        with open('database/nlp_database.json') as db:
            database = json.load(db)

        # Initialize NLP Database Manager
        nlp_database_manager = NlpDatabaseManager(database)

        # Initialize NLP Agent Manager
        nlp_agent_manager = NlpAgentManager(nlp_database_manager)

        # Initialize User Interface
        user_interface = UserInterface(nlp_agent_manager)

        # Start the application
        user_interface.start()

    except Exception as e:
        error_handler.handle_error(e)

if __name__ == "__main__":
    main()
