# libscan - Python Dependency Scanner

**libscan** is a Python utility that helps you easily detect and install external dependencies for your Python project. It scans the imports of a given Python script, identifies missing dependencies, and allows you to install them interactively. Additionally, it can generate a `requirements.txt` file for your project with the installed versions of the detected dependencies.

## Features

- **Dependency Detection**: Scans a Python script to detect all external dependencies that need to be installed.
- **Interactive Installation**: Prompts you to install missing dependencies.
- **Generate `requirements.txt`**: Optionally generate a `requirements.txt` file containing all detected dependencies with their installed versions.
- **Customizable Output**: Beautiful and colorful output using `rich` for a better user experience.
- **Help Command**: Use `--help` to get details on the available commands.

## Installation

To install **libscan**, use the following command:

```bash
pip install libscan
```

## Usage

### 1. Scan for Missing Dependencies and Install

Run the following command to scan for missing dependencies in your Python script and install them interactively:

```bash
libscan /path/to/your_script.py
```

It will detect any external dependencies that are not already installed and prompt you with:

```
📦 Dependencies found:
Module1
Module2
...

Do you want to install these packages? (y/n): [y]:
```

If you choose **`y`**, the script will install the packages.

### 2. Generate a `requirements.txt` File

To generate a `requirements.txt` file with the dependencies of your project, use the `-r` option:

```bash
libscan -r /path/to/your_script.py
```

This will create a `requirements.txt` file in the current directory with the names and versions of the external dependencies.

### 3. Show Help

To view the available commands and options, use the `--help` flag:

```bash
libscan --help
```

This will display information about the available options and their usage.

## Example Commands

- Scan a script and install missing dependencies:
  ```bash
  libscan myscript.py
  ```
  Output will display a list of found dependencies and ask for confirmation to install them.

- Generate a `requirements.txt` for your project:
  ```bash
  libscan -r myscript.py
  ```
  This will create a `requirements.txt` file containing the detected dependencies.

- Display help:
  ```bash
  libscan --help
  ```

## Example Output

### Detecting Dependencies

```bash
📦 Dependencies found:
requests
numpy
pandas

Do you want to install these packages? (y/n): [y]: y
✅ requests installed successfully.
✅ numpy installed successfully.
✅ pandas installed successfully.
```

### Generating `requirements.txt`

```bash
📦 Dependencies found:
requests
numpy
pandas

Do you want to save them to `requirements.txt`? (y/n): [y]
✅ `requirements.txt` generated successfully!
```

## Options

- **`-r` / `--requirements`**: Generate a `requirements.txt` file with the detected dependencies and their versions.
- **`--help`**: Show help and usage information for the tool.

## License

This project is open-source and available under the MIT License.

---

**libscan** is designed to simplify your Python dependency management. Whether you're working on a new project or maintaining an existing one, it helps you manage your dependencies efficiently.
