import itertools

class CollectorsCache:

    def __init__(self) -> None:
        self.__cache = list()

    async def add_many(self, data: list) -> None:
        self.__cache = list(itertools.chain(self.__cache, data))
    
    async def add_one(self, data) -> None:
        self.__cache.append(data)

    async def read_cache(self) -> list:
        return self.__cache
    
    async def remove(self, data) -> None:
        self.__cache.remove(data)


