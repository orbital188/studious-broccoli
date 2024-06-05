import pandas as pd
import os
import shutil
import re

# Load the CSV file
file_path = './final_consistent_sorted_content.csv'
df = pd.read_csv(file_path)

# Define the base output directory
base_output_dir = 'problems_md'

# Delete the base output directory if it exists
if os.path.exists(base_output_dir):
    shutil.rmtree(base_output_dir)

# Ensure the base output directory exists
os.makedirs(base_output_dir)

# Iterate through each row in the DataFrame
for index, row in df.iterrows():
    # Extract problem number from the title
    title = row['title_english']
    match = re.search(r'\bProblem (\d+)\b', title)
    if match:
        problem_number = match.group(1)
    else:
        # Skip if problem number is not found
        continue
    
    # Calculate the folder number
    folder_number = (int(problem_number) - 1) // 100 + 1
    folder_name = f'folder_{folder_number}'
    folder_path = os.path.join(base_output_dir, folder_name)
    
    # Ensure the folder exists
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    
    # Extract content and link
    content = row['content_english']
    link = row['link']
    
    # Create the markdown content
    md_content = f"# {title}\n\n{content}\n\n[Problem Source]({link})"
    
    # Define the file name
    file_name = f'problem_{problem_number}.md'
    
    # Write the markdown content to a file
    with open(os.path.join(folder_path, file_name), 'w', encoding='utf-8') as file:
        file.write(md_content)
