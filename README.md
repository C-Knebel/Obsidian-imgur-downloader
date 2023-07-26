# Obsidian Imgur Downloader

This Python script is designed to download images from Imgur links referenced within your Obsidian.md files and save them locally. Additionally, it updates the markdown files to reference the downloaded images locally.

The script may be useful for those who use the "obsidian-imgur-plugin" and wish to back up their files in the eventuality of Imgur going offline or deleting the images unexpectedly.

## Requirements

- Python 3.x
- Requests library (can be installed using `pip install requests`)

## Usage

1. Place the `imgur_downloader.py` script in the same folder as your Obsidian.md files or in any parent directory of your Obsidian vault.

2. Make sure you have Python 3.x installed on your system.

3. Install the required library by running the following command in your terminal or command prompt:

   ```
   pip install requests
   ```

4. Run the script by executing the following command in your terminal or command prompt:

   ```
   python imgur_downloader.py
   ```

   The script will automatically find all the .md files within the folder and its subfolders, download the images referenced in them, and update the links to point to the locally downloaded images.

## Folder Structure

```
/your_obsidian_vault
   ├── imgur_downloader.py
   └── your_obsidian_files/
       ├── @imgur_photos/
       ├── note1.md
       ├── note2.md
       └── ...
   └── other_obsidian_files/
       ├── @imgur_photos/
       ├── note3.md
       ├── note4.md
       └── ...
```

- `imgur_downloader.py`: The Python script to download and update the images.
- `@imgur_photos/`: The folder where the downloaded images will be stored.
- `your_obsidian_files/`, `other_obsidian_files/` : Folders containing your Obsidian.md files. The script will process all .md files within folders and subfolders.

## Important Notes

- The script assumes that the image links in your Obsidian.md files are in the format `![alt text](https://i.imgur.com/...)`. It will download images from Imgur links only.

- The downloaded images will be saved in the `@imgur_photos/` folder within the same directory as the md files.

- The script will overwrite any existing files in the `@imgur_photos/` folder with the same name. Please ensure that there are no conflicting image names.

## Disclaimer

**ATTENTION: PLEASE BACKUP YOUR VAULT BEFORE USING THIS SCRIPT. IT WILL REPLACE THE REFERENCES TO IMGUR LINKS IN ALL YOUR MD FILES WITH LOCAL FILES.**
