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

