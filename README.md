# Archive Extractor


## Overview

This simple Python script serves as an archive extractor, allowing users to easily extract contents from various compressed file formats, including Zip, Tar, 7-Zip, and RAR.

## Features

- Supports extraction of Zip, Tar, 7-Zip, and RAR archives.
- User-friendly command-line interface.
- Built-in file type detection using the `magic` library.

## Usage

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/your-repo.git
    ```

2. Navigate to the project directory:

    ```bash
    cd your-repo
    ```

3. Run the script:

    ```bash
    python3 archive_extractor.py
    ```

4. Follow the on-screen instructions to enter the path of the compressed file you want to extract.

## Operating System Compatibility

This project is developed and tested on the Linux operating system. To run it on Windows:

### Windows

1. Ensure Python is installed on your system. You can download it [here](https://www.python.org/downloads/).

2. Open a command prompt and navigate to the project directory.

3. Run the script:

    ```bash
    python archive_extractor.py
    ```

4. Make the following changes to the script for Windows compatibility:
   
   - Replace any Linux-specific paths with Windows paths.
   - Ensure the required libraries (`zipfile`, `tarfile`, `py7zr`, `rarfile`, `magic`, `os`) are installed on your Windows environment.

### Linux

Follow the steps mentioned in the previous section for Linux.

## Example

```bash
[+] Enter the compressed file to extract it (or 'q' to quit): example.zip
[+] example.zip extracted successfully ...
