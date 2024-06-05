import pandas as pd
import os

# Load the CSV file
file_path = './final_consistent_sorted_content.csv'
df = pd.read_csv(file_path)

# Ensure the output directory exists
output_dir = 'problems_md'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Iterate through each row in the DataFrame
for index, row in df.iterrows():
    # Extract title, content, and link
    title = row['title_english']
    content = row['content_english']
    link = row['link']
    
    # Create the markdown content
    md_content = f"# {title}\n\n{content}\n\n({link})"
    
    # Define the file name
    file_name = f'problem_{index + 1}.md'
    
    # Write the markdown content to a file
    with open(os.path.join(output_dir, file_name), 'w') as file:
        file.write(md_content)

