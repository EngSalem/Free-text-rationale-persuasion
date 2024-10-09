 Task 
  You will be presented with a topic and two arguments, labeled as "ARG1" and "ARG2." One of these arguments, either "ARG1" or "ARG2," is identified as the winner argument ("WINNER_ARG"). Additionally, two different reasonings supporting the winner argument are provided, each indicated by a numerical identifier [1] or [2]. Your task is to determine which reasoning is more PERSUASIVE or if they are equally persuasive in supporting the "WINNER_ARG".

#   
# Formatting Examples

## Example 1:
- Input:

{{
"TOPIC": "topic 1",
"ARG1": "text of argument 1",
"ARG2": "text of argument 2",
"WINNER_ARG": "ARG1",
"[1]" : "REASONING 1 for choosing argument 1",
"[2]" : "REASONING 2 for choosing argument 2"
}}
Think step by step then decide.
<|im_end|>
- Output:

{{
"reasoning": "Your reasoning for choosing rationale [1]"
"decision": "[1]"
}}
<|im_end|>

## Example 2:
- Input:

{{
"TOPIC": "topic 1",
"ARG1": "text of argument 1",
"ARG2": "text of argument 2",
"WINNER_ARG": "ARG1",
"[1]" : "REASONING 1 for choosing argument 1",
"[2]" : "REASONING 2 for choosing argument 2"
}}



Think step by step then decide.
<|im_end|>
- Output:

{{
"reasoning": "Your reasoning for choosing rationale [2]"
"decision": "[2]",
}}
<|im_end|>

## Example 3:
- Input:

{{
"TOPIC": "topic 1",
"ARG1": "text of argument 1",
"ARG2": "text of argument 2",
"WINNER_ARG": "ARG1",
"[1]" : "REASONING 1 for choosing argument 1",
"[2]" : "REASONING 2 for choosing argument 2"
}}


Think step by step then decide.
<|im_end|>
- Output:

{{
"reasoning": "Your reasoning for deciding that they are equally persuasive"
"decision": "EQUAL",
}}
<|im_end|>


# Reminder
make sure to include your "reasoning" and decision in a json format of {{"reasoning":"..",
                                                                 "decision":".."}}.
Don't include anything else in the process.
Keep your reasoning short in a maximum of 2 sentences.
# Annotation Example:
- Input:

{{
"TOPIC": "{}",
"ARG1": "{}",
"ARG2": "{}",
"WINNER_ARG": "ARG{}",
"[1]": "{}",
"[2]": "{}"
}}
Think step by step then decide.
<|im_end|>
- Output:
