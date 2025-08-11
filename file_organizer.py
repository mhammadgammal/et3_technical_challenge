import os
import shutil
import argparse
from collections import defaultdict

categories = {
    "Images": [
        ".jpg",
        ".jpeg",
        ".png",
        ".gif",
        ".bmp",
        ".tiff",
        ".svg",
        ".webp",
    ],
    "Videos": [
        ".mp4",
        ".mkv",
        ".mov",
        ".avi",
        ".flv",
        ".wmv"
    ],
    "Documents": [
        ".pdf",
        ".doc",
        ".docx",
        ".xls",
        ".xlsx",
        ".ppt",
        ".pptx",
        ".txt"
    ]
}

def organize_files(file_path):
    # extract file extension
    ext = os.path.splitext(file_path)[1].lower()

    # loop over items and check for matches
    for category, exts in categories.items(): 
        if ext in exts: 
            return category

    # If no category matched, return "Others"
    return "Others"

