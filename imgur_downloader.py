import os
import re
import requests

# Create a folder (if it doesn't exist) at the given path
def create_folder(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

# Find the part inside parentheses (link) of the regular expression in the file
def find_links(file):
    links = re.findall(r'!\[.*?\]\((https://i.imgur.com/.*?)\)', file)
    return links

# Download an image, given a link, name, and location
def download_image(link, image_name, output_folder):
        # Path for the downloaded image
        image_path = os.path.join(output_folder, image_name)

        # Perform a request to the Imgur link
        response = requests.get(link)

        if response.status_code == 200:
            # Save the image
            with open(image_path, 'wb') as image_file:
                image_file.write(response.content)
            print(f"Image downloaded: {image_name}")
        else:
            print(f"Failed to download the image: {image_name}")

# Update the markdown file to reference the downloaded image locally
def md_substitute(image_name, content):
    image_tag = f"![[{image_name}]]"
    new_content = re.sub(r'!\[.*?\]\((https://i.imgur.com/.*?)\)', image_tag, content)
    return new_content

def imgur_downloader(md_file):
    # Open the file
    with open(md_file, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Folder in which the file is located
    base_folder = os.path.dirname(md_file)  

    # List of links within the "content" file
    imgur_links = find_links(content)

    # Use the folder "@imgur_photos" to save the images
    output_folder = os.path.join(base_folder, "@imgur_photos")
    # Create the folder
    create_folder(output_folder)  

    new_content = content

    for idx, link in enumerate(imgur_links, start=1):
        # Naming the files based on the name and position in the links list
        image_name = f"{os.path.basename(md_file)[:-3]}-{idx}.jpg"
        
        # Download the image
        download_image(link, image_name, output_folder)

        # Update: the content of the markdown file
        new_content = md_substitute(image_name, new_content)
    
    with open(md_file, 'w', encoding='utf-8') as file:
        file.write(new_content)

# Function that calls the image downloader for each markdown file within folders/subfolders
def folder_tree_call(folder_path):
    # In each iteration, we have a new root, dirs, and files
    for root, _, files in os.walk(folder_path):
        # root is the address of the current folder, dirs are the subfolders inside, and files are the files
        for file in files:
            if file.endswith(".md"):
                # Path to the md file
                md_file_path = os.path.join(root, file)
                imgur_downloader(md_file_path)

if __name__ == "__main__":
    # Get the directory path where the script is located
    script_dir = os.path.dirname(__file__)
    # Call the function for the directory
    folder_tree_call(script_dir)
