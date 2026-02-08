# LoggingSystem

A small, extensible Python logging system implemented as a learning LLD project.

**Project structure**
- `client.py` — example usage / runner
- `appenders/`
  - `base_appender.py` — abstract base for appenders
  - `console_appender.py` — writes logs to console
  - `file_appender.py` — writes logs to file
- `logger/`
  - `log_level.py` — log level definitions (enum)
  - `formatter.py` — formats `LogMessage` into string output
  - `log_message.py` — small data holder for message metadata
  - `logger.py` — orchestrates logging, holds appenders

## Purpose and responsibilities
- The system separates concerns: formatting, message representation, destination (appenders), and logger orchestration.
- `Logger` coordinates: it accepts `LogMessage` instances, delegates formatting to `Formatter`, and forwards formatted output to each configured `Appender`.
- `Append` implementations (`ConsoleAppender`, `FileAppender`) implement the `BaseAppender` contract so the `Logger` can remain unaware of destination details.

## Logging flow (sequence)
1. Client code in `client.py` calls `Logger.log(...)` (or similar API).
2. `Logger` constructs a `LogMessage` (or accepts one) with level, text, timestamp, etc.
3. `Formatter` formats the `LogMessage` into a string.
4. The `Logger` iterates configured appenders and calls each appender's `append(formatted_message)`.
5. Each appender handles writing to its target (console, file, etc.).

## Design analysis — Low-Level Design (LLD) & patterns
- Strategy pattern: Appendable destinations and formatters act like strategies. You can swap `ConsoleAppender` for `FileAppender` or any other appender implementing `BaseAppender` without changing `Logger` internals.
- Dependency Injection: `Logger` receives its appenders (and optionally a `Formatter`) from outside, which improves testability and modularity.
- Open/Closed Principle: To add a new output (e.g., network appender), implement the `BaseAppender` interface and register the new appender — no changes to `Logger` required.
- Suggested Singleton (optional): Many logging frameworks provide a global `Logger` instance. If you want a global logger, implement a controlled singleton/factory to avoid multiple competing instances.
- Thread-safety note: If `Logger` will be used from multiple threads, consider adding synchronization (locks) around appender iteration and file writes, or use a queue + worker thread to avoid interleaved output.

## Classes & responsibilities (quick map)
- `LogMessage` — data holder: level, message text, timestamp, optional metadata.
- `Formatter` — converts `LogMessage` → string. Keep formatting rules here.
- `BaseAppender` — interface/abstract base defining `append(formatted_message)` (and possibly `close()`).
- `ConsoleAppender` — simple implementation that prints to stdout.
- `FileAppender` — writes to file, handles file open/close/rotation as needed (extension).
- `Logger` — public API used by clients: `debug/info/warn/error` helpers or a generic `log(level, message)`; holds list of appenders and a formatter.

## How to use
Run the example client:

```bash
python client.py
```

Typical setup in `client.py`:
- create `ConsoleAppender` and/or `FileAppender`
- create `Logger` and register appenders
- call `logger.info("...")` or `logger.log(LogLevel.INFO, "...")`

## Extension ideas / improvements
- Add configuration support (JSON/YAML) to declare appenders and formatting rules.
- Add log message buffering and asynchronous flush for high-throughput scenarios.
- Support log rotation in `FileAppender`.
- Add structured logging (JSON) support via alternate `Formatter` implementations.
- Provide a global `LoggerFactory` or singleton helper for convenience.

## Notes & assumptions
- The README is based on the project layout in this folder; adapt wording if you rename classes or change APIs.
- If you want, I can update the `Logger` to include a thread-safe queue or provide a `LoggerFactory` singleton example.

---
If you want changes to the README (more diagrams, UML, or code snippets extracted from the source), tell me which parts to expand and I'll update the file.