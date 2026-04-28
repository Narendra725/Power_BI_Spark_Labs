from src.powerbi import PowerBIReport
import json 
import os
from utils.Read import Json


def main():
    definition_folder = "C:\\Users\\dasari.babu\\OneDrive - Tredence\\Documents\\Nahdi-articrafts\\PowerBI\\Automations\\MachII\\sample_report.Report\\definition"
    report_json_path = "C:\\Users\\dasari.babu\\OneDrive - Tredence\\Documents\\Nahdi-articrafts\\PowerBI\\Automations\\MachII\\sample_report.Report\\definition\\report.json"
    version_json_path = "C:\\Users\\dasari.babu\\OneDrive - Tredence\\Documents\\Nahdi-articrafts\\PowerBI\\Automations\\MachII\\sample_report.Report\\definition\\version.json"
    pages_folder = "C:\\Users\\dasari.babu\\OneDrive - Tredence\\Documents\\Nahdi-articrafts\\PowerBI\\Automations\\MachII\\sample_report.Report\\definition\\pages"
    bookmarks_folder = "C:\\Users\\dasari.babu\\OneDrive - Tredence\\Documents\\Nahdi-articrafts\\PowerBI\\Automations\\MachII\\sample_report.Report\\definition\\bookmarks"

# definition folder is the main folder which contains all the json files and subfolders for the report definition. We will read the report.json and version.json files and print their contents. We will also list all the pages in the pages folder.
# report.json contains the main definition of the report, including its name, dataset, and other properties. version.json contains the version information of the report. The pages folder contains individual page definitions for the report.
# pages are stored as separate json files in the pages folder, and we will list their names to see how many pages the report has.
# bookmarks are stored similar to pages, but in a separate bookmarks folder. We can also list the bookmarks if needed.
    

if __name__ == "__main__":
    main()