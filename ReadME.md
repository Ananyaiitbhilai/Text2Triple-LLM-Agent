
# Text2kg_LLM_KGAgent

This repository contains the code and resources for the research project "Towards Harnessing Large Language Models as Autonomous Agents for Semantic Triple Extraction from Unstructured Text". The project aims to develop a framework that integrates Large Language Models (LLMs) with existing tools like REBEL and KnowGL for the task of triple extraction from unstructured text to construct knowledge graphs.

## Overview

The proposed framework leverages the strengths of LLMs in understanding complex linguistic structures, handling modalities and negations, and mitigating biases inherent in training data. The experimental results on the CONLL04 dataset indicate that while multi-tool approaches face challenges such as hallucination, the integration of LLMs shows promising results in enhancing extraction accuracy.

## Repository Structure

- `data/`: Contains the dataset files used for evaluation (CONLL04).
- `CONLL04 pre-processing/`: Contains scripts for pre-processing and formatting the CONLL04 dataset.
- `src/`:
  - `Evaluation/`: Contains scripts for evaluating the performance of the triple extraction models.
  - `Prediction/`: Contains scripts for generating predictions using LLMs and various tools (REBEL, KnowGL).
  - `Processing/`: Contains scripts for processing the predictions and preparing them for evaluation.
  - `SystemLLM/`: Contains scripts related to the LLM component of the framework.
  - `Tools/`: Contains scripts for interfacing with external tools like REBEL and KnowGL.
- `GeneratedData/`: Directory for storing generated predictions and processed files during the evaluation process.
- `run_extraction.sh`: A bash script to automate the prediction, processing, and evaluation steps for both multi-tool and single-tool usage.

## Getting Started


1. Install the required dependencies:

```
pip install -r requirements.txt
```



3. Download the CONLL04 dataset and place it in the `data/` directory.

4. Run the pre-processing script to format the dataset:

```
python CONLL04preprocessing/conll04_formatting.py
python CONLL04preprocessing/evalFileGeneration.py
```

5. Run the evaluation script for multi-tool or single-tool usage:

```
# Multi-tool usage
./run_extraction.sh

# Single-tool usage (REBEL)
./run_extraction.sh
```

## Contributing

Contributions to this project are welcome. If you encounter any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

We would like to acknowledge the authors of the REBEL and KnowGL frameworks, as well as the researchers and developers of the Large Language Models used in this project.
```

This README provides an overview of the project, the repository structure, instructions for getting started, contributing guidelines, license information, and acknowledgments. Feel free to modify it according to your specific project requirements.

Based on the provided file structure, the README file should be updated to reflect the correct paths and filenames. Here is the revised section of the README that corresponds to the file structure in the image:

---

# Triple Extraction Automation README

This README provides instructions on how to use the `run_extraction.sh` bash script for automating the process of triple extraction using a Language Learning Model (LLM) as an autonomous agent. The script supports both multi-tool and single-tool usage.

## Prerequisites

Before running the script, ensure that you have:

- Python 3.x installed
- All necessary Python dependencies installed (as required by the scripts mentioned in `run_extraction.sh`)
- The project directory structure set up as expected by the script

## Getting Started

1. **Prepare Your Environment**: If you're using a Python virtual environment, activate it before running the script. Ensure all Python scripts referenced in `run_extraction.sh` are executable in your current environment.

2. **Check Paths and Filenames**: Verify that all paths and filenames in `run_extraction.sh` match those in your project. Adjust any paths or filenames as necessary.

3. **Make the Script Executable**: Run the following command in your terminal to make `run_extraction.sh` executable:

    ```bash
    chmod +x run_extraction.sh
    ```

4. **Run the Script**: Execute the script by running the following command in your terminal:

    ```bash
    ./run_extraction.sh
    ```

## Script Overview

The `run_extraction.sh` script automates the following steps for both multi-tool and single-tool usage:

- **Prediction**: Generates predictions using the specified tools located in the `src/Prediction` directory.
- **Processing**: Processes the predictions and formats them for evaluation using the script in the `src/Processing` directory.
- **Evaluation**: Evaluates the processed predictions against a golden file using the script in the `src/Evaluation` directory.

For single-tool usage, the script is set to use `REBEL.py` by default. To switch to `KnowGL.py`, edit the script to comment out the line with `REBEL.py` and uncomment the line with `KnowGL.py`.

## Troubleshooting

- If you encounter permission issues when running Python scripts, ensure they are marked as executable or adjust the script to include the path to your virtual environment's Python executable.
- For any path or filename mismatches, double-check the script and adjust the paths or filenames as needed.

## Support

For additional help or to report issues, please contact the project maintainers.

---


