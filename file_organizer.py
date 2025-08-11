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

def get_category(file_path):
    # extract file extension
    ext = os.path.splitext(file_path)[1].lower()

    # loop over items and check for matches
    for category, exts in categories.items(): 
        if ext in exts: 
            return category

    # If no category matched, return "Others"
    return "Others"

def print_summary(summary):
    print("\nSummary:")
    for category, count in summary.items():
        print(f"{category}: {count} files")


def organize_files(folder_path, sim = False):
    summary = defaultdict(int)

    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)
        if os.path.isfile(item_path):
            category = get_category(item_path)
            target_folder = os.path.join(folder_path, category)
            if not os.path.exists(target_folder):
                os.makedirs(target_folder)

            summary[category] += 1

            if sim:
                print(f"Simulating move: {item_path} -> {target_folder}")
            else:
                shutil.move(item_path, target_folder)
    
    print_summary(summary)

