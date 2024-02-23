# Character Frequency Analysis Tool

This tool analyzes the frequency of characters and pairs of characters in a text file. It supports multiple output formats and languages, with an option to focus only on ASCII characters for broader compatibility.

## Description

The Character Frequency Analysis Tool is designed to process text files to extract and report the frequency of individual characters and character pairs. This tool is versatile, supporting various languages and output formats, including YAML and JSON. It also features an ASCII-only mode, which converts non-ASCII characters to their closest ASCII equivalents, such as mapping "ö" to "o".

## Installation

Before using the tool, ensure you have Python installed on your system. You can then clone this repository to your local machine.

```bash
git clone https://github.com/predyy/letter-frequency.git
```

## Usage

To use the tool, navigate to the program's directory and run the following command in your terminal:

```python
python character_frequency_analysis.py <filepath> [options]
```

### Arguments

- `filepath`: The path to the text file you want to analyze.

### Options

- `--language`: Specify the language for character analysis. Default is "english".
- `--ascii`: Enable ASCII-only mode. Non-ASCII characters will be converted to their closest ASCII counterparts.
- `--yaml`: Output the analysis results in YAML format to file.
- `--json`: Output the analysis results in JSON format to file.

### Examples

Analyze a text file with default settings (English, no ASCII conversion, standard output):

```bash
python letter_frequency.py data/samples/english/shakespeare.txt
```

Analyze a text file in German in ASCII mode with JSON output:

```bash
python letter_frequency.py data/samples/german/combined.txt --language german --ascii --json
```

## Adding New Languages

To add support for a new language, create a YAML file in the `data/alphabets` directory. The file should also map each character in the alphabet to its ASCII equivalent if necessary.

## Samples

Sample text files for testing and examples of their analysis results are included in the data/samples and data/samples_results directories, respectively.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
