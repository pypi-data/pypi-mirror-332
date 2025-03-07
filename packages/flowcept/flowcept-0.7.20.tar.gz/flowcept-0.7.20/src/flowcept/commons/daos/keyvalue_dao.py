"""Key value module."""

from redis import Redis

from flowcept.commons.flowcept_logger import FlowceptLogger
from flowcept.configs import (
    KVDB_HOST,
    KVDB_PORT,
    KVDB_PASSWORD,
)


class KeyValueDAO:
    """Key value DAO class."""

    _instance: "KeyValueDAO" = None

    def __new__(cls, *args, **kwargs) -> "KeyValueDAO":
        """Singleton creator for KeyValueDAO."""
        # Check if an instance already exists
        if cls._instance is None:
            # Create a new instance if not
            cls._instance = super(KeyValueDAO, cls).__new__(cls)
        return cls._instance

    def __init__(self, connection=None):
        if not hasattr(self, "_initialized"):
            self._initialized = True
            self.logger = FlowceptLogger()
            if connection is None:
                self._redis = Redis(
                    host=KVDB_HOST,
                    port=KVDB_PORT,
                    db=0,
                    password=KVDB_PASSWORD,
                )
            else:
                self._redis = connection

    def delete_set(self, set_name: str):
        """Delete it."""
        self._redis.delete(set_name)

    def add_key_into_set(self, set_name: str, key):
        """Add a key."""
        self._redis.sadd(set_name, key)

    def remove_key_from_set(self, set_name: str, key):
        """Remove a key."""
        self.logger.debug(f"Removing key {key} from set: {set_name}")
        self._redis.srem(set_name, key)
        self.logger.debug(f"Removed key {key} from set: {set_name}")

    def set_has_key(self, set_name: str, key) -> bool:
        """Set the key."""
        return self._redis.sismember(set_name, key)

    def set_count(self, set_name: str):
        """Set the count."""
        return self._redis.scard(set_name)

    def set_is_empty(self, set_name: str) -> bool:
        """Set as empty."""
        _count = self.set_count(set_name)
        self.logger.info(f"Set {set_name} has {_count}")
        return _count == 0

    def delete_all_matching_sets(self, key_pattern):
        """Delete matching sets."""
        matching_sets = self._redis.keys(key_pattern)
        for set_name in matching_sets:
            self.delete_set(set_name)

    def set_key_value(self, key, value):
        """
        Store a key-value pair in Redis.

        Parameters
        ----------
        key : str
            The key to store in Redis.
        value : str
            The value associated with the key.

        Returns
        -------
        None
        """
        self._redis.set(key, value)

    def get_key(self, key):
        """
        Retrieve a value from Redis by key.

        Parameters
        ----------
        key : str
            The key to look up in Redis.

        Returns
        -------
        str or None
            The decoded value if the key exists, otherwise None.
        """
        value = self._redis.get(key)
        return value.decode() if value else None

    def delete_key(self, key):
        """
        Delete the key if it exists.

        Parameters
        ----------
        key : str
            The key to look up in Redis.

        Returns
        -------
        None
        """
        self._redis.delete(key)
