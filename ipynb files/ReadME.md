This folder contains the files for EDA and Final score calculation. Please note here absolute path for the files was set. You may need to change the path of the files according to your local system's path. All the generated files while doing experiments are stored in `dataFiles` Folder. Description of almost all useful files are provided in the table below.

## Description of the files for which scores are calculated

| File Name                        | Number of Instances | Number of Relations | Description                                      |
|----------------------------------|---------------------|---------------------|--------------------------------------------------|
| Golden_Truth_triples.json        | 288                 | 5                   | Full Golden Truth dataset with 5 relation types  |
| Golden_Truth_triple_nostring_gemma.json | 187             | 5                   | Subset of Golden Truth for Gemma                 |
| Golden_Truth_triple_nostring_mistral.json | 262           | 5                   | Subset of Golden truth for Gemma                 |
| Pred_rebel.json                  | 288                 | 5                   | Predictions extracted from Rebel                 |
| Pred_mistral.json                | 268                 | 5                   | Predictions from Mistral                         |
| Pred_gemma.json                  | 187                 | 5                   | Predictions from Gemma                           |
| Pred_rebel_nostring_mistral.json | 262                 | 5                   | For comparison with Mistral                      |
| Pred_rebel_nostring_gemma.json   | 187                 | 5                   | For comparison with Gemma                        |
| Pred_mistral_nostring.json       | 262                 | 5                   | Predictions from Mistral without hallucination   |
| Pred_gemma_nostring.json         | 187                 | 5                   | Predictions from Gemma without hallucination     |
| Pred_rebel_nostring_mistral_5rel.json | 262             | 5                   | For comparison of REBEL with same subset as Mistral, clustered |
| Pred_rebel_nostring_gemma_5rel.json | 187               | 5                   | For comparison of REBEL with same subset as Gemma, clustered |
| Pred_mistral_nostring_5rel.json  | 262                 | 5                   | Mistral predictions, clustered                   |
| Pred_gemma_nostring_5rel.json    | 187                 | 5                   | Gemma predictions, clustered                     |
| Pred_rebel_5rel.json             | 288                 | 5                   | Rebel predictions, clustered                     |