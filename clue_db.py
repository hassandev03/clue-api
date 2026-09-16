from alan_wake_clue_api.clue import Clue


class ClueDB:
    """A simple in-memory database for storing clues."""

    clues: list[Clue] = []
