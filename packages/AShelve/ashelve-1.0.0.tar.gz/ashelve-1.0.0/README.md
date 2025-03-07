# AShelve

An asynchronous wrapper for Python's shelve module, providing thread-safe persistent dictionary-like storage with async/await support.

## Installation

You can install this library using pip:

```bash
pip install AShelve
```

## Features

- Asynchronous Interface: All operations are async, perfect for use in asyncio applications

- Thread-Safe: Uses locks to prevent data corruption during concurrent operations

- Persistent Storage: Data is stored on disk using Python's shelve module

- Simple API: Easy to use with familiar dictionary-like methods

## Usage

```python
import asyncio
from AShelve import AShelve

async def main():
    # Create a new AShelve instance
    db = AShelve("mydata")
    
    # Store some data
    await db.set("user1", "Alice")
    await db.set("user2", "Bob")
    
    # Retrieve data
    user1 = await db.get("user1")
    print(user)  # Alice
    
    # List all keys
    keys = await db.keys()
    print(keys)  # ['user1', 'user2']
    
    # Delete an item
    await db.delete("user2")
    
    # Clear all data
    await db.clear()

if __name__ == "__main__":
    asyncio.run(main())
```

## API Reference

### Constructor

```python
AShelve(filename, flag='c', protocol=None, writeback=True)
```

- `filename`: Base filename for the shelve database

- `flag`: Access mode ('c' for read/write/create, 'r' for read-only, 'w' for read/write)

- `protocol`: Pickle protocol version to use

- `writeback`: If True, all entries accessed are cached in memory

## Methods

### `async set(key, value)`

Store a key-value pair in the database

### `async get(key, default=None)`

Retrieves a value for the given key, or returns default if not found.

### `async set(key, value)`

Sets the value for the given key.

### `async delete(key)`

Deletes the specified key and its value.

### `async keys()`

Returns a list of all keys in the database.

### `async values()`

Returns a list of all values in the database.

### `async items()`

Returns a list of all (key, value) pairs in the database.

### `async clear()`

Removes all items from the database.

## Thread Safety

AShelve uses two different locks to ensure thread safety:

- A reentrant lock (`threading.RLock`) for general operations
- A separate lock (`threading.Lock`) for write operations
This approach prevents race conditions and ensures data integrity.

## License

MIT License

## Contributing

Contributions are welcome! Please feel free to submit a pull request.
