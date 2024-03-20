#!/bin/bash

# Define common paths

EVAL_FILE_PATH="data/datasets/conll04/conll04_eval.json"
GOLDEN_FILE="data/datasets/conll04/test.json"

#GENERATED
PROCESS_GOLDEN="GeneratedData/Processingforeval/golden_multi.json"
PROCESS_PRED="GeneratedData/Processingforeval/pred_multi.json"
SCORES_MTRE="GeneratedData/Score/Score_multi_tool.txt"

# Multi-tool usage
echo "Starting multi-tool usage..."
PRED_FILE_PATH_MULTI="GeneratedData/Prediction/pred_multi.json"

# Prediction Step
python src/Prediction/generatePredictionLLMMultitool.py $EVAL_FILE_PATH $PRED_FILE_PATH_MULTI

# Processing Step
python src/Processing/Processingforeval.py $PRED_FILE_PATH_MULTI $GOLDEN_FILE $PROCESS_GOLDEN $PROCESS_PRED

# Evaluation Step
python src/Evaluation/evalRE.py $PROCESS_GOLDEN $PROCESS_PRED > $SCORES_MTRE

echo "Multi-tool usage completed."

