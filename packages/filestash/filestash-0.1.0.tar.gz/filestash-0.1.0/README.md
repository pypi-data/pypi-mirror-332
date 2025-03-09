# Stash CLI

Stash CLI is a command-line interface (CLI) tool for uploading and downloading files to and from the FileStash server. It simplifies file management by using file hashes for identification and retrieval.  It supports both public and private uploads and downloads.  The tool also includes an analysis feature that extracts information about an uploaded file.

This CLI is useful for developers and users who need a convenient way to store, share, and retrieve files securely.

## Installation

Stash CLI requires Python 3.10 or later.  We recommend managing your Python environment with `pyenv` or `conda`.

1.  **Install `pipx`:** If you don't have `pipx` installed, use `pip install pipx`.  `pipx` will install Stash CLI into its own isolated environment, preventing dependency conflicts.
2.  **Install stash:**  `pipx install stash`

Stash CLI will then be available in your system's PATH.

## Usage

### Uploading a File

```bash
stash up <file_path> [--server <server_url>] [--token <token>] [--analyze <boolean>]
```

*   `file_path`: Path to the file to upload (required).
*   `server`: URL of the FileStash server. Defaults to `http://localhost:8181/upload`. The stash/constants.py file defines the base URL as `http://localhost:8181`. When using the `up` command, `/upload` is appended. For the remote FileStash server, set it to `https://filestash.xyz/upload`.
*   `token`: Authentication token (optional, but required for private uploads).  If not provided, it uses the `FILESTASH_TOKEN` environment variable. Set this variable in a `.env` file or directly in your environment.
*   `analyze <boolean>`: Analyze the contents of the file and describe it (default is True).


### Downloading a File

```bash
stash down <hash> [--server <server_url>] [--token <token>] [--output-dir <output_directory>]
```

*   `hash`: Hash of the file to download (required).
*   `server`: URL of the FileStash server. Defaults to `http://localhost:8181/download`.  For the remote FileStash server, set it to `https://filestash.xyz/download`.
*   `token`: Authentication token (optional, but required for private downloads). If not provided, it uses the `FILESTASH_TOKEN` environment variable.
*   `output-dir`: Directory to save the downloaded file (optional; defaults to the current directory).


### Listing Files

```bash
stash list [--server <server_url>] [--token <token>] [--limit <integer>] [--filter-by <string>]
```

*   `server`: URL of the FileStash server. Defaults to `http://localhost:8181/list`.  For the remote FileStash server, set it to `https://filestash.xyz/list`.
*   `token`: Authentication token (optional but recommended). If not provided, it uses the `FILESTASH_TOKEN` environment variable.  The token increases the number of files that can be listed.
*   `limit`: Maximum number of files to list (optional; defaults to 50).
*   `filter_by`: Filter the files by a string pattern (optional).


### Version

```bash
stash version
```

Displays the installed version of Stash CLI.

## Development

Stash CLI uses `poetry` for dependency management.

1.  **Install Poetry:**  `pipx install poetry` (recommended)
2.  **Clone the Repository:** `git clone https://github.com/ogre-run/stash-cli.git`
3.  **Navigate to Project:** `cd stash-cli`
4.  **Install Dependencies:** `poetry install`
5.  **Activate Virtual Environment:** `poetry shell`

You can now run the CLI from within the virtual environment with `stash <command>`.
