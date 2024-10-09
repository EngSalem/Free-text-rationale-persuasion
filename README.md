

# Free-text Rationale Persuasiveness (EMNLP 2024 Findings)

This repository contains the code and data for the paper **"Free-text Rationale Persuasiveness"** published in the EMNLP 2024 Findings.

## Annotated Dataset

### Accessing the Dataset
The annotated dataset can be found [here](./data/annotated_data).

### Dataset Structure
The dataset is constructed to include pairs of arguments and corresponding rationales from different models. The file `annotated_rationale_pairs.json` contains the following fields:

- `topic`: The subject of the argument.
- `argument 1`: Text of the first argument.
- `argument 2`: Text of the second argument.
- `model decision`: Indicates which argument the model deemed more persuasive.
- `rationale 1`: Free-text rationale supporting the model’s decision from one model.
- `rationale 2`: Free-text rationale supporting the model’s decision from another model.
- `persuasive rationale`: The rationale considered more persuasive between rationale 1 and rationale 2.

#### Example:

```json
{
    "topic": "Flu vaccination should not be mandatory",
    "argument 1": "The state ought not intervene in individuals' right of bodily autonomy regardless of societal harms. Forcing vaccinations is a crude invasion of someone's body and should therefore not be done.",
    "argument 2": "Forcing people to participate in a system they do not trust, often with passion and for irrational reasons, might lead them to distrust conventional medicine as a whole, increasing the risk to their health.",
    "model decision": "argument 1",
    "rationale 1": "Argument 1 is more persuasive because it appeals to the principle of bodily autonomy, which is a fundamental human right. It also provides clear and logical reasoning for why mandatory vaccination is not justified. Argument 2, while valid, may not be as convincing to those who do not share the same distrust in conventional medicine.",
    "rationale 2": "Argument 1 is more compelling as it appeals to the universal principle of bodily autonomy and individual rights. It also addresses the potential societal harms, making it a more comprehensive argument.",
    "persuasive rationale": "rationale 1"
}
```

## Sampled Pairs
The pairs of arguments sampled and used for analysis can be accessed [here](./data/argument_pairs).

## Prompting LLMs
The prompts used for interacting with language models (LLMs) can be found [here](./src/prompts).

## Ranking Rationales for Persuasion
The script for ranking rationales based on persuasiveness using GPT-4 can be found [here](./src/prompts/pairwise_rationale_persuasion_ranking_with_gpt4.py).

## Citation 
```
@article{elaraby2024persuasiveness,
  title={Persuasiveness of Generated Free-Text Rationales in Subjective Decisions: A Case Study on Pairwise Argument Ranking},
  author={Elaraby, Mohamed and Litman, Diane and Li, Xiang Lorraine and Magooda, Ahmed},
  journal={arXiv preprint arXiv:2406.13905},
  year={2024}
}
```