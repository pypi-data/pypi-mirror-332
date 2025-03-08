# Hieralog

**Hieralog** is a hierarchical logging library for Python that provides enhanced logging and printing functions. It supports multiple levels, color coding, framed and plain output, and integrates seamlessly with progress bars.

## Features

- **Hierarchical Logging:** Auto-detect log levels with a "[x]" prefix.
- **Color-Coded Output:** Different colors for each log level.
- **Enhanced Print Functions:** 
  - **hprint()**: Hierarchical (framed) logging output.
  - **pprint()**: Plain print with hierarchical indentation.
  - **fprint()**: Framed print with hierarchical indentation.
  - **progress_write()**: Writes progress messages with the proper indent.
- **Automatic Completion Message:** A final completion log is printed automatically when the program ends.

## Installation

Install via pip:

```bash
pip install hieralog1
