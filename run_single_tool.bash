#!/bin/bash

# Define common paths
EVAL_FILE_PATH="data/datasets/conll04/conll04_eval.json"
GOLDEN_FILE="data/datasets/conll04/test.json"


#GENERATED
PROCESS_GOLDEN="GeneratedData/Processingforeval/golden_st.json"
PROCESS_PRED="GeneratedData/Processingforeval/pred_st.json"
SCORES="GeneratedData/Score/Score_single_tool_rebel.txt"


# Single-tool usage
echo "Starting single-tool usage..."
PRED_FILE_PATH_SINGLE="GeneratedData/Prediction/pred_single.json"

# Prediction Step for a single tool (uncomment the desired tool)

python src/Prediction/generatePredictionsLLMSingleTool.py $EVAL_FILE_PATH $PRED_FILE_PATH_SINGLE

# Processing Step
python src/Processing/Processingforeval.py $PRED_FILE_PATH_SINGLE $GOLDEN_FILE $PROCESS_GOLDEN $PROCESS_PRED

# Evaluation Step
python src/Evaluation/evalRE.py $PROCESS_GOLDEN $PROCESS_PRED > $SCORES


echo "Single-tool usage completed."



