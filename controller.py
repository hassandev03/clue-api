"""
Controller for the Alan Wake Clue API.
This module provides functions to manage the storage of clues.
"""

import json


from clue import Clue
from clue_db import ClueDB


class ClueController:
    """Static controller handling business logic and JSON operations."""

    _clue_database: list[Clue] = ClueDB.clues

    @classmethod
    def add_clue(
        cls,
        title: str,
        description: str,
        chapter: int | None = None,
        location: str | None = None,
        clue_type: str = "case_fact",
        discovered: bool = False,
        media_url: str | None = None,
    ) -> str:
        """Creates a clue, adds it to the central store, and returns it as JSON."""
        new_clue = Clue(
            title=title,
            description=description,
            chapter=chapter,
            location=location,
            clue_type=clue_type,
            discovered=discovered,
            media_url=media_url,
        )
        cls._clue_database.append(new_clue)
        return json.dumps(new_clue.to_dict(), indent=2)

    @classmethod
    def get_all_clues(
        cls,
    ) -> str:
        """Serializes all central clues into a JSON array."""
        clues = cls._clue_database

        data = [clue.to_dict() for clue in clues]
        return json.dumps(data, indent=2)

    @classmethod
    def get_clue_by_id(cls, clue_id: str) -> str:
        """Finds a specific clue by ID and returns its JSON representation."""
        for clue in cls._clue_database:
            if clue.id == clue_id:
                return json.dumps(clue.to_dict(), indent=2)
        return json.dumps({"error": "Clue not found"}, indent=2)
    
    @classmethod
    

    @classmethod
    def clear_database(cls) -> None:
        """Utility method to reset the central store."""
        cls._clue_database.clear()
