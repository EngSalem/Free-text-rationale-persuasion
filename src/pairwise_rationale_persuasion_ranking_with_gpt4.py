import pandas as pd
from openai import OpenAI, AzureOpenAI
import os
import json
import ast
import argparse

# Default prompt template
prompt = open("./prompts/pairwise_persuasion_ranking.md",'r').read()

def gpt4_ranker(prompt_text, client, max_tokens=256, temperature=0, stop=None):
    """Function to interact with GPT-4 API and return the evaluated response."""
    response = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": """
                  You will be presented with a topic and two arguments, labeled as "ARG1" and "ARG2." One of these arguments, either "ARG1" or "ARG2," is identified as the winner argument ("WINNER_ARG"). Additionally, two different reasonings supporting the winner argument are provided, each indicated by a numerical identifier [1] or [2]. Your task is to determine which reasoning is more persuasive in supporting the "WINNER_ARG".
                  """
            },
            {
                "role": "user",
                "content": prompt_text
            }
        ],
        model="gpt-4-turbo",
        temperature=temperature,
        max_tokens=max_tokens
    )
    
    try:
        return ast.literal_eval(response.choices[0].message.content)
    except Exception as e:
        return {"reasoning": "rationales are equally bad", "decision": "EQUAL"}

def main(args):
    """Main function to load the dataset, process it, and save the results."""
    # Initialize the Azure OpenAI client
    client = AzureOpenAI(
        api_key=args.api_key,
        azure_endpoint=args.azure_endpoint,
        api_version=args.api_version
    )
    
    # Load the dataset
    data = pd.read_csv(args.input_file)
    ## expecting the data in format "topic", "arg_1", "arg_2", "model_decision", "combination_1 (rationale 1)", and "combination_2 (rationale 2)"
    # First run of the model
    data["first_run"] = data.apply(lambda row: gpt4_ranker(
        prompt_text=prompt.format(row['topic'], row['arg_1'], row['arg_2'], row['model_decision'], row['combination_1'], row['combination_2']), 
        client=client), axis=1)
    
    # Second run of the model with reversed combinations
    data["second_run"] = data.apply(lambda row: gpt4_ranker(
        prompt_text=prompt.format(row['topic'], row['arg_1'], row['arg_2'], row['model_decision'], row['combination_2'], row['combination_1']), 
        client=client), axis=1)
    
    # Save the results to a CSV file
    data.to_csv(args.output_file, index=False)
    print(f"Results saved to {args.output_file}")

if __name__ == "__main__":
    # Set up argument parser for configurable input/output and API settings
    parser = argparse.ArgumentParser(description="Run GPT-4 ranking on argument pairs.")
    
    parser.add_argument('--input_file', type=str, required=True, help="Path to the input CSV file")
    parser.add_argument('--output_file', type=str, required=True, help="Path to the output CSV file")
    parser.add_argument('--api_key', type=str, required=True, help="Azure OpenAI API key")
    parser.add_argument('--azure_endpoint', type=str, required=True, help="Azure OpenAI endpoint URL")
    parser.add_argument('--api_version', type=str, default='2024-02-15-preview', help="Azure OpenAI API version")
    parser.add_argument('--max_tokens', type=int, default=256, help="Maximum tokens for the GPT-4 completion")
    parser.add_argument('--temperature', type=float, default=0, help="Temperature for the GPT-4 completion")

    args = parser.parse_args()
    main(args)
