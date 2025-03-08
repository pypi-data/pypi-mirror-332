# Instructions for GitHub Copilot

This repository holds evohome, a Python 3 based RESTful client library based upon aiohttp.

- Python code must be compatible with Python 3.13
- Dependencies must be compatible with the latest release of HomeAssistant
- Use the newest Python language features if possible:
  - Pattern matching
  - Type hints
  - f-strings for string formatting over `%` or `.format()`
  - Dataclasses
  - Walrus operator
- Code quality tools:
  - Formatting: Ruff
  - Linting: PyLint and Ruff
  - Type checking: MyPy
  - Testing: pytest with plain functions and fixtures
- Inline code documentation:
  - File headers should be short and concise:
    ```python
    """Integration for Peblar EV chargers."""
    ```
  - Every method and function needs a docstring:
    ```python
    async def async_setup_entry(hass: HomeAssistant, entry: PeblarConfigEntry) -> bool:
        """Set up Peblar from a config entry."""
        ...
    ```
- All code and comments and other text are written in American English
- Follow existing code style patterns as much as possible
- All external I/O operations must be async
- Async patterns:
  - Avoid sleeping in loops
  - Avoid awaiting in loops, gather instead
  - No blocking calls
- Polling:
  - Follow update coordinator pattern, when possible
  - Polling interval may not be configurable by the user
  - For local network polling, the minimum interval is 5 seconds
  - For cloud polling, the minimum interval is 60 seconds
- Error handling:
  - Use specific exceptions from `evohome.exceptions`
- Logging:
  - Message format:
    - No periods at end
    - No integration names or domains (added automatically)
    - No sensitive data (keys, tokens, passwords), if when those are incorrect.
  - Be very restrictive on the use if logging info messages, use debug for
    anything which is not targeting the user.
  - Use lazy logging (no f-strings):
    ```python
    _LOGGER.debug("This is a log message with %s", variable)
    ```
