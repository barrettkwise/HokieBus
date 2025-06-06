from datetime import datetime
from json import dumps
from pathlib import Path
from typing import Callable


class CacheHandler:
    """
    A class to handle the caching of data.

    :author: Barrett Wise
    :date: 1/22/25
    """

    def __init__(
        self,
        cache_file: str = "",
        update_freq: int = 72,
        update_function: Callable = lambda: None,
    ) -> None:
        """
        :param cache_file: The file to cache the data to and from.
        :type cache_file: str
        :param update_freq: The frequency to update the cache in hours.
        :type update_freq: int
        :param update_function: The function to call to update the cache.
        :type update_function: Callable
        """
        if not Path(cache_file).exists():
            print("Cache file does not exist. Creating cache file...")
            Path(cache_file).touch()
        self.cache_file = Path(cache_file)
        self.update_freq = update_freq
        self.update_function = update_function
        self.cache_update()

    def cache_update(self) -> None:
        """
        Checks the modification time of the cache file and updates the cache if it is older than
        the update frequency or if the cache file is empty or does not exist.

        :return: None
        """
        self.cache_file = Path(self.cache_file)
        last_modified = datetime.fromtimestamp(self.cache_file.stat().st_mtime)
        time_since_mod = datetime.now() - last_modified
        is_empty = self.cache_file.stat().st_size == 0
        if time_since_mod.total_seconds() / 3600 > self.update_freq or is_empty:
            print("Updating cache...")
            if not is_empty:
                open(self.cache_file, "w").close()  # Clear the cache file
                print("Cache cleared.")
            new_data = self.update_function(update=True)
            print("Data fetched.")
            self.cache_file.write_text(dumps(new_data))
            print("Cache updated.")
        else:
            print("Cache is up to date.")
