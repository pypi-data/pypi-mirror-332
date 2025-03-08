# --- render code block -----
from datafoundry._core.postgres_core import PostgresqlBase

class ABC(PostgresqlBase):
    @classmethod
    def get_uuid(cls) -> str:
        """
        initialize credential for the class
        """
        return "67c80335535b6a2668124ffb"
# --- render code block -----
