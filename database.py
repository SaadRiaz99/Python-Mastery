from supabase import create_client, Client
from config import SUPABASE_URL, SUPABASE_KEY

_client: Client | None = None


def get_supabase() -> Client:
    global _client
    if _client is not None:
        return _client

    if not SUPABASE_URL or not SUPABASE_KEY:
        raise RuntimeError(
            "Missing Supabase credentials. "
            "Set SUPABASE_URL and SUPABASE_KEY in your .env file."
        )

    _client = create_client(SUPABASE_URL, SUPABASE_KEY)
    return _client
