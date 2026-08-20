import os
from config import SUPABASE_URL, SUPABASE_KEY

_client = None
_mode = None


def get_supabase():
    global _client, _mode

    if _client is not None:
        return _client

    use_local = (
        not SUPABASE_URL
        or not SUPABASE_KEY
        or "placeholder" in SUPABASE_URL
        or os.getenv("STORAGE_MODE", "").lower() == "local"
    )

    if use_local:
        from local_db import LocalClient
        _client = LocalClient()
        _mode = "local"
        print("[STORAGE] Using local file-based storage (data/)")
        return _client

    from supabase import create_client
    _client = create_client(SUPABASE_URL, SUPABASE_KEY)
    _mode = "supabase"
    print("[STORAGE] Using Supabase")
    return _client


def get_storage_mode():
    return _mode
