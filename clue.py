from datetime import datetime, timezone
import uuid


class Clue:
    """Model representing an individual clue."""

    ALLOWED_TYPES = {
        "case_fact",
        "profile",
        "manuscript_page",
        "nursery_rhyme",
        "cult_stash",
        "echo",
        "other",
    }

    def __init__(
        self,
        title: str,
        description: str,
        case_id: str,
        chapter: int|None = None,
        location: str|None  = None,
        clue_type: str = "case_fact",
        discovered: bool = False,
        media_url: str|None  = None,
    ):
        if not (1 <= len(title) <= 120):
            raise ValueError("Title must be between 1 and 120 characters.")
        if clue_type not in self.ALLOWED_TYPES:
            raise ValueError(f"Invalid clue type: {clue_type}")

        # Server-managed fields
        self.id = str(uuid.uuid4())
        self.discovered_at = (
            datetime.now(timezone.utc).isoformat() if discovered else None
        )

        # Content fields
        self.title = title
        self.description = description
        self.case_id = case_id
        self.chapter = chapter
        self.location = location
        self.clue_type = clue_type
        self.discovered = discovered
        self.media_url = media_url

    def to_dict(self) -> dict:
        """Converts model fields to a dictionary for JSON serialization."""
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "case_id": self.case_id,
            "chapter": self.chapter,
            "location": self.location,
            "clue_type": self.clue_type,
            "discovered": self.discovered,
            "discovered_at": self.discovered_at,
            "media_url": self.media_url,
        }