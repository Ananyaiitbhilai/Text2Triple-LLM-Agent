#!/bin/bash

# Define common paths
# EVAL_FILE_PATH="data/datasets/conll04/conll04_eval.json"
# GOLDEN_FILE="data/datasets/conll04/test.json"

EVAL_FILE_PATH = "testing_eval.json"
GOLDEN_FILE = "testing_gold.json"

#GENERATED
PROCESS_GOLDEN="GeneratedData/Processingforeval/golden_stLLM.json"
PROCESS_PRED="GeneratedData/Processingforeval/pred_stLLM.json"
SCORES_R="GeneratedData/Score/Score_single_tool_noLLLM_rebel.txt"
SCORES_K="GeneratedData/Score/Score_single_tool_noLLLM_knowgl.txt"

# Single-tool usage
echo "Starting single-tool no LLM usage..."
PRED_FILE_PATH_SINGLE="GeneratedData/Prediction/pred_single_noLLM.json"

# Prediction Step for a single tool (uncomment the desired tool)
#python src/Prediction/generatePredictiononlyFramework.py extract_text_triplets_knowgl $EVAL_FILE_PATH $PRED_FILE_PATH_SINGLE
python src/Prediction/generatePredictiononlyFramework.py extract_text_triplets_rebel $EVAL_FILE_PATH $PRED_FILE_PATH_SINGLE

# Processing Step
python src/Processing/Processingforeval.py $PRED_FILE_PATH_SINGLE $GOLDEN_FILE $PROCESS_GOLDEN $PROCESS_PRED

# Evaluation Step
python src/Evaluation/evalRE.py $PROCESS_GOLDEN $PROCESS_PRED > $SCORES_R
#python src/Evaluation/evalRE.py $PROCESS_GOLDEN $PROCESS_PRED > $SCORES_K

echo "Single-tool no LLM usage completed."