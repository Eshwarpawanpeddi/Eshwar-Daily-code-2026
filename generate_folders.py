#!/usr/bin/env python3
"""
Script to generate folder structure with dates from today to Dec 31, 2026.
Each folder is named with the date in YYYY-MM-DD format.
"""

from datetime import datetime, timedelta
import os

def generate_date_folders(start_date, end_date):
    """
    Generate folders for each date between start_date and end_date (inclusive).
    Each folder contains a .gitkeep file to ensure it's tracked by Git.
    
    Args:
        start_date: Starting date (datetime object)
        end_date: Ending date (datetime object)
    """
    current_date = start_date
    folders_created = 0
    
    while current_date <= end_date:
        # Format date as YYYY-MM-DD
        folder_name = current_date.strftime("%Y-%m-%d")
        
        # Create folder (exist_ok=True avoids race conditions)
        folder_existed = os.path.exists(folder_name)
        os.makedirs(folder_name, exist_ok=True)
        
        # Create .gitkeep file to ensure Git tracks the folder
        gitkeep_path = os.path.join(folder_name, ".gitkeep")
        if not os.path.exists(gitkeep_path):
            open(gitkeep_path, 'a').close()
        
        if not folder_existed:
            folders_created += 1
            print(f"Created folder: {folder_name}")
        else:
            print(f"Folder already exists: {folder_name}")
        
        # Move to next day
        current_date += timedelta(days=1)
    
    print(f"\nTotal folders created: {folders_created}")
    return folders_created

if __name__ == "__main__":
    # Start date: January 17, 2026 (today)
    start_date = datetime(2026, 1, 17)
    
    # End date: December 31, 2026
    end_date = datetime(2026, 12, 31)
    
    print(f"Generating folders from {start_date.strftime('%Y-%m-%d')} to {end_date.strftime('%Y-%m-%d')}")
    print(f"Total days: {(end_date - start_date).days + 1}\n")
    
    generate_date_folders(start_date, end_date)
    
    print("\nFolder structure generation complete!")
