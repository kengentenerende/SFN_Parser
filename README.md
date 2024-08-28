# SFN (Short File Name) and File Metadata Parser

This Python script parses and decodes various metadata fields from a given hex string representing a file's short file name (SFN) entry. It supports the decoding of file attributes, creation/modification times, dates, and file size, considering little-endian format as needed.

##  What is SFN?

An 8.3 filename (also called a short filename or SFN) is one that obeys the filename convention used by old versions of DOS and versions of Microsoft Windows prior to Windows 95 and Windows NT 3.5. It is also used in modern Microsoft operating systems as an alternate filename to the long filename, to provide compatibility with legacy programs. The filename convention is limited by the FAT file system. Similar 8.3 file naming schemes have also existed on earlier CP/M, TRS-80, Atari, and some Data General and Digital Equipment Corporation minicomputer operating systems.
- [8.3 filename](https://en.wikipedia.org/wiki/8.3_filename)

## Features

- **SFN Name & Extension**: Extracts the short file name and file extension.
- **File Attributes**: Decodes the file attributes (e.g., Archive, Read-Only, etc.).
- **Creation Time/Date**: Extracts and converts the creation time and date from the hex string.
- **Last Accessed Date**: Extracts and converts the last accessed date.
- **Last Modification Time/Date**: Extracts and converts the last modification time and date.
- **File Size**: Decodes the file size in bytes, correctly handling little-endian format.

## Prerequisites

- Python 3.x

## Usage

1. **Clone the Repository**:

    ```bash
    git clone https://github.com/kengentenerende/SFN_Parser.git
    cd sfn_parser
    ```

2. **Run the Script**:

    Execute the script with Python:

    ```bash
    python SFN_calculator.py
    ```

3. **Input**:

    When prompted, enter the hex string representing the SFN entry. For example:

    ```bash
    Enter the hex string: 544558542D4F7E314A5047200000436B714B714B0100EB4EFA4A58400C990200
    ```

4. **Output**:

    The script will output the parsed data:

    ```
    SFN Name: TEXT-O~1
    Extension: JPG
    Attributes: Archive
    Reserved: 00
    Create Time Tenths: 00
    Creation Time: 13:26:06
    Creation Date: 2017-11-17
    Last Date Accessed: 2017-11-17
    First Cluster High: 0100
    Last Modification Time: 09:55:22
    Last Modification Date: 2017-07-26
    First Cluster Low: 5840
    File Size (Bytes): 170252
    ```

## Script Details

### Functions

- **`hex_to_bin_str(hex_value, length)`**: Converts a hexadecimal string to a binary string of a specified length.
  
- **`decode_time(hex_time)`**: Decodes the creation/modification time from a hex string, adjusting for little-endian format.
  
- **`decode_date(hex_date)`**: Decodes the creation/modification date from a hex string, adjusting for little-endian format.
  
- **`decode_attributes(hex_value)`**: Converts a hex attribute byte into its corresponding file attribute descriptions.
  
- **`parse_hex_input(hex_input)`**: Parses the full hex string and decodes each component (SFN Name, Extension, Attributes, Times, Dates, File Size, etc.).

### Little-Endian Handling

The script accounts for little-endian format in decoding times, dates, and file size. Little-endian means the least significant byte is stored first, so the script reverses the byte order before converting to the correct values.

### Example Hex String

The hex string `544558542D4F7E314A5047200000436B714B714B0100EB4EFA4A58400C990200` is parsed as:

- **SFN Name**: `TEXT-O~1`
- **Extension**: `JPG`
- **Attributes**: `Archive`
- **Creation Time**: `13:26:06`
- **Creation Date**: `2017-11-17`
- **Last Date Accessed**: `2017-11-17`
- **Last Modification Time**: `09:55:22`
- **Last Modification Date**: `2017-07-26`
- **File Size**: `170252` bytes

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
