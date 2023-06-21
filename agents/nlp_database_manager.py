#!/usr/bin/env python3

"""
NLP Database Manager Module for the Hybrid Database Model Application.

This module is responsible for managing the context of each NLP Document Agent and
distributing queries to the relevant NLP Document Agents based on their expertise.
"""

# Standard library imports
import json
import os

# Project specific imports
from utils.communication import Communication
from utils.error_handling import ErrorHandler
from agents.nlp_document_agent import NlpDocumentAgent

class NlpDatabaseManager:
    """
    A class used to manage the NLP Database in the Hybrid Database Model Application.
    """

    def __init__(self, database):
        """
        Initialize the NlpDatabaseManager with a given database.

        :param database: A dictionary representing the database of NLP Document Agents.
        """
        self.database = database
        self.document_agents = self.load_document_agents()

    def load_document_agents(self):
        """
        Load the NLP Document Agents from the NLP Database.

        :return: A dictionary mapping agent IDs to NlpDocumentAgent objects.
        """
        document_agents = {}

        # Iterate over the agents in the database
        for agent_data in self.database["agents"]:
            agent_id = agent_data["agent_id"]

            # Load context data for the agent from the individual context file
            with open(f"database/nlp_documents/{agent_id}_documents.json") as context_file:
                context_data = json.load(context_file)

            document_contexts = context_data["document_contexts"]

            # Initialize the NlpDocumentAgent for this agent with the loaded context
            document_agents[agent_id] = NlpDocumentAgent(agent_id, document_contexts)
        return document_agents

    def distribute_query(self, query):
        """
        Distribute a query to the relevant NLP Document Agents based on their expertise.

        :param query: A string representing the user's query.
        :return: A dictionary mapping agent IDs to their responses.
        """
        responses = {}

        for agent_id, document_agent in self.document_agents.items():
            if document_agent.can_answer(query):
                response = document_agent.answer(query)
                responses[agent_id] = response

        return responses

    def update_context(self, agent_id, context_update):
        """
        Update the context of a specific NLP Document Agent.

        :param agent_id: The ID of the NLP Document Agent.
        :param context_update: A dictionary representing the context update.
        """
        if agent_id not in self.document_agents:
            raise ValueError(f"No NLP Document Agent found with ID {agent_id}")

        self.document_agents[agent_id].update_context(context_update)

        # Save the updated context to a file
        with open(f"database/nlp_documents/{self.database[agent_id]}", 'w') as file:
            json.dump(self.document_agents[agent_id].context, file)
