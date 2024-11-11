import os
import glob
import re

def natural_sort_key(s):
    return [int(c) if c.isdigit() else c.lower() for c in re.split(r'(\d+)', s)]

def get_existing_images(markdown_content):
    return set(re.findall(r'<img src="(.*?)"', markdown_content))

def create_markdown_with_screenshots(folder_path, img_width=800):
    markdown_file = os.path.join(folder_path, 'exam_notes.md')
    
    # Read existing markdown content if file exists
    if os.path.exists(markdown_file):
        with open(markdown_file, 'r') as f:
            existing_content = f.read()
        existing_images = get_existing_images(existing_content)
    else:
        existing_content = ""
        existing_images = set()

    # Get all PNG and JPEG files in the folder
    image_files = glob.glob(os.path.join(folder_path, '*.png')) + \
                  glob.glob(os.path.join(folder_path, '*.jpg')) + \
                  glob.glob(os.path.join(folder_path, '*.jpeg'))
    
    # Sort the files using natural sorting
    image_files.sort(key=natural_sort_key)
    
    # Create or update the markdown content
    updated_content = "# Exam Prepper Questions\n\n"
    for image_file in image_files:
        file_name = os.path.basename(image_file)
        if file_name in existing_images:
            # Find and add the existing content for this image
            pattern = f"## Question: {file_name}.*?(?=\n## Question: |\Z)"
            match = re.search(pattern, existing_content, re.DOTALL)
            if match:
                updated_content += match.group(0) + "\n\n"
        else:
            # Add new content for this image
            updated_content += f"## Question: {file_name}\n\n"
            updated_content += f'<img src="{file_name}" alt="Question" width="{img_width}">\n\n'
            updated_content += "<details>\n"
            updated_content += "<summary>Click to reveal the correct answer</summary>\n\n"
            updated_content += "- [Insert correct answer here]\n\n"
            updated_content += "Notes:\n\n"
            updated_content += "- \n\n"
            updated_content += "</details>\n\n"
    
    # Write the updated markdown content to the file
    with open(markdown_file, 'w') as f:
        f.write(updated_content)

# Use the current directory as the folder path
folder_path = 'exam_prepper_questions/SA-associate'
create_markdown_with_screenshots(folder_path)