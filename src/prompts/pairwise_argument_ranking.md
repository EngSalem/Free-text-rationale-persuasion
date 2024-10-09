# Task
You possess the art of argumentation. You will receive two arguments, each identified by a numerical identifier [] and a Topic. Disregarding your own opinion on the topic, given the arguments, the model decision, and the model reasoning, decide which argument you would recommend.
Choose argument [1] if you recommend argument [1] over argument [2].
Choose argument [2] if you recommend argument [2] over argument [1].
Format your output in a JSON format with "decision" and "reasoning" keys.: 

# Formatting Examples

## Example 1:
- Input:
{
"topic": "topic 1",
"1": "argument 1",
"2": "argument 2"
}

- Output:
{
"decision": 1,
"reasoning": "reason for choosing argument 1"
}


## Example 2:
- Input:
{
"topic": "topic 2",
"1": "argument 1",
"2": "argument 2"
}

- Output:
{
"decision": 2,
"reasoning": "reason for choosing argument 2"
}


# Reminder
make sure to choose only one argument and provide a convincing reasoning why you choose this argument over the other one.
Generate only the json output with decision and reasoning, do not generate any additional thought process or discussion.

# Annotation Example:
- Input:

{
"topic": "{}",
"1": "{}",
"2": "{}",
"model_decision": "argument {}",
"model_reasoning": "{}",
}

- Output:

