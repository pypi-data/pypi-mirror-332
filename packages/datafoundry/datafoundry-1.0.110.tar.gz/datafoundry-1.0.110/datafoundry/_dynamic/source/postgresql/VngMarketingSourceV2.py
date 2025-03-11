# --- render code block -----
from datafoundry._core.postgres_core import PostgresqlBase

class VngMarketingSourceV2(PostgresqlBase):
    @classmethod
    def get_uuid(cls) -> str:
        """
        initialize credential for the class
        """
        return "67ce55f0cc9763e2d191eea9"
# --- render code block -----
