# AI-Snap

AI-Snap is a Python utility that captures the structure and contents of a project directory and saves
them into a text file.

It's designed for quick documentation of your project's file system before creating a prompt to AI chat.

# Features
 - Complete Capture: Records the entire file structure and contents of the project.
 - Customizable Filters: Offers whitelist option for targeted scanning, Git .gitignore / rsync pathspec supported.
 - Command-Line Interface: Simple and easy-to-use command-line tool.

# Installation

## Install AI-Snap with pip:

```
pip install AI-Snap
```

## Standalone executable (Windows only)

It's possible not to utilize Python at all and download standalone AI-Snap executable from the project site.

# Usage

## Command-line help

```
Usage: ai-snap [OPTIONS] COMMAND [ARGS]...

  Save project structure and file contents, considering rules from the config
  file.

Options:
  --version           Show the version and exit.
  --instruct PATH     Path to the instruction file to include at the beginning
  --config-file PATH  Path to the config file (e.g., .gitignore-like file with whitelist and exclusions)
  --help              Show this message and exit.

  See more at https://github.com/ai-snap/ai-snap
```

By default, AI-Snap will scan all files and directories in the current folder and produce an output file called project_contents.txt.

## Example

Let's assume that we are going to improve some aspect of AI-snap with ChatGPT.

First of all, we need to create .ai-snap file in the project directory (or specify your own file with --config-file):

```
ai_snap/
!scripts
!.ai-snap
ai-snap
ai-snap.py
!LICENSE
!README.md
PipFile
pyproject.toml
```

# Contributing

Contributions to AI-Snap are welcome! Feel free to fork the repository, make your changes, and submit a pull request.

# License

AI-Snap is open-sourced software licensed under the MIT license.

# Support

For support, questions, or feedback, please open an issue in the GitHub repository.
