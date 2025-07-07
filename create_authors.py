import os
import bibtexparser
from unidecode import unidecode
import subprocess

# Function to install a package if it's not already installed
def install_package(package):
    try:
        __import__(package)
    except ImportError:
        subprocess.check_call(["pip", "install", package])

# Install required packages
install_package("bibtexparser")
install_package("unidecode")

# --- Configuration ---
BIB_FILE = 'publications.bib'
AUTHORS_DIR = 'content/authors'
# --- End Configuration ---

def normalize_author_name(name):
    """
    Normalizes an author's name to a standard format.
    Handles 'Last, First' and 'First Last' formats.
    """
    name = name.strip()
    if ',' in name:
        parts = [p.strip() for p in name.split(',')]
        return f"{parts[1]} {parts[0]}"
    return name

def get_unique_authors(bib_file):
    """
    Parses a .bib file and returns a set of unique, normalized author names.
    """
    try:
        with open(bib_file, 'r', encoding='utf-8') as bibtex_file:
            bib_database = bibtexparser.load(bibtex_file)
    except FileNotFoundError:
        print(f"Error: The file '{bib_file}' was not found.")
        return set()

    authors = set()
    for entry in bib_database.entries:
        if 'author' in entry:
            author_list = entry['author'].split(' and ')
            for author_name in author_list:
                normalized_name = normalize_author_name(author_name)
                # Use unidecode to handle accents and special characters
                cleaned_name = unidecode(normalized_name).lower()
                authors.add(cleaned_name.title()) # Keep it title-cased for display
    return authors

def create_author_profiles(authors, authors_dir):
    """
    Creates a directory and an _index.md file for each author.
    """
    if not os.path.exists(authors_dir):
        os.makedirs(authors_dir)

    for author_name in authors:
        # Create a unique, URL-friendly ID for the author
        author_id = author_name.lower().replace(' ', '-')

        # Path for the author's directory
        author_path = os.path.join(authors_dir, author_id)

        # Create the directory if it doesn't exist
        if not os.path.exists(author_path):
            os.makedirs(author_path)

        # Path for the _index.md file
        index_file_path = os.path.join(author_path, '_index.md')

        # Create the content for the _index.md file
        content = f"""---
# Display name
title: {author_name}

# Is this the primary user of the site?
superuser: false

# Role/position
role: Co-author

# Organizations/Affiliations
# organizations:
# - name: Stanford University
#   url: ""

# Short bio (displayed in user profile at the top of the page)
bio: ""

# Social/Academic Networking
# For available icons, see: https://docs.hugoblox.com/getting-started/page-builder/#icons
#   For an email link, use "fas" icon pack, "envelope" icon, and a link in the
#   form "mailto:your-email@example.com" or "#contact" for contact widget.
social:
- icon: envelope
  icon_pack: fas
  link: '#contact'  # For a direct email link, use "mailto:test@example.org".

# Link to a PDF of your resume/CV from the About widget.
# To enable, copy your resume/CV to `static/uploads/resume.pdf` and uncomment the lines below.
# - icon: cv
#   icon_pack: ai
#   link: uploads/resume.pdf

# Enter email to display Gravatar (if Gravatar enabled in Config)
email: ""

# Highlight the author in author lists? (true/false)
highlight_name: false
---
"""

        # Write the content to the _index.md file
        with open(index_file_path, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"Created profile for {author_name} at {author_path}")

if __name__ == "__main__":
    unique_authors = get_unique_authors(BIB_FILE)
    if unique_authors:
        create_author_profiles(unique_authors, AUTHORS_DIR)
        print("\nSuccessfully created author profiles.")
