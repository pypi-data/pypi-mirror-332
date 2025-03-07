import shelve
import asyncio
import threading
from contextlib import contextmanager
from typing import Any, Optional, Generator, TypeVar

T = TypeVar("T")


class AShelve:
    def __init__(
        self,
        filename: str,
        flag: str = "c",
        protocol: Optional[int] = None,
        writeback: bool = True,
    ):
        self.filename = filename
        self.flag = flag
        self.protocol = protocol
        self.writeback = writeback
        self.lock = threading.RLock()
        self.write_lock = threading.Lock()

    @contextmanager
    def _open_shelf(self) -> Generator[shelve.Shelf, None, None]:
        with self.lock:
            shelf = shelve.open(
                self.filename,
                flag=self.flag,
                protocol=self.protocol,
                writeback=self.writeback,
            )
            try:
                yield shelf
            finally:
                shelf.close()

    async def get(self, key: str, default: Optional[T] = None) -> Optional[T]:
        def _get():
            with self._open_shelf() as shelf:
                return shelf.get(key, default)

        return await asyncio.to_thread(_get)

    async def set(self, key: str, value: Any) -> None:
        def _set():
            with self.write_lock:
                with self._open_shelf() as shelf:
                    shelf[key] = value
                    shelf.sync()

        await asyncio.to_thread(_set)

    async def delete(self, key: str) -> None:
        def _delete():
            with self.write_lock:
                with self._open_shelf() as shelf:
                    if key in shelf:
                        del shelf[key]
                        shelf.sync()

        await asyncio.to_thread(_delete)

    async def keys(self) -> list:
        def _keys():
            with self._open_shelf() as shelf:
                return list(shelf.keys())

        return await asyncio.to_thread(_keys)

    async def values(self) -> list:
        def _values():
            with self._open_shelf() as shelf:
                return list(shelf.values())

        return await asyncio.to_thread(_values)

    async def items(self) -> list:
        def _items():
            with self._open_shelf() as shelf:
                return list(shelf.items())

        return await asyncio.to_thread(_items)

    async def clear(self) -> None:
        def _clear():
            with self.write_lock:
                with self._open_shelf() as shelf:
                    shelf.clear()
                    shelf.sync()

        await asyncio.to_thread(_clear)
