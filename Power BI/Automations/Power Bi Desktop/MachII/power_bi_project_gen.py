import os

PROJECT_NAME = "pbi_report_gen"

FOLDER_STRUCTURE = [
    PROJECT_NAME,
    f"{PROJECT_NAME}/src/pbi_automation",
    f"{PROJECT_NAME}/src/pbi_automation/io",
    f"{PROJECT_NAME}/src/pbi_automation/layout",
    f"{PROJECT_NAME}/src/pbi_automation/core",
    f"{PROJECT_NAME}/src/pbi_automation/config",
    f"{PROJECT_NAME}/tests",
]

FILES_TO_CREATE = [
    f"{PROJECT_NAME}/pyproject.toml",
    f"{PROJECT_NAME}/README.md",
    f"{PROJECT_NAME}/LICENSE",
    f"{PROJECT_NAME}/.gitignore",

    f"{PROJECT_NAME}/src/pbi_automation/__init__.py",
    f"{PROJECT_NAME}/src/pbi_automation/cli.py",

    f"{PROJECT_NAME}/src/pbi_automation/io/__init__.py",
    f"{PROJECT_NAME}/src/pbi_automation/io/file_ops.py",

    f"{PROJECT_NAME}/src/pbi_automation/layout/__init__.py",
    f"{PROJECT_NAME}/src/pbi_automation/layout/layout_v1.py",

    f"{PROJECT_NAME}/src/pbi_automation/core/__init__.py",
    f"{PROJECT_NAME}/src/pbi_automation/core/registry.py",
    f"{PROJECT_NAME}/src/pbi_automation/core/visuals.py",
    f"{PROJECT_NAME}/src/pbi_automation/core/page.py",
    f"{PROJECT_NAME}/src/pbi_automation/core/report.py",
    f"{PROJECT_NAME}/src/pbi_automation/core/bookmark.py",

    f"{PROJECT_NAME}/src/pbi_automation/config/__init__.py",
    f"{PROJECT_NAME}/src/pbi_automation/config/paths.py",

    f"{PROJECT_NAME}/tests/test_basic.py",
]

def create_structure():
    for folder in FOLDER_STRUCTURE:
        os.makedirs(folder, exist_ok=True)

    for file_path in FILES_TO_CREATE:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        if not os.path.exists(file_path):
            with open(file_path, "w", encoding="utf-8") as f:
                f.write("")

    print(f"Created project structure: {PROJECT_NAME}")

if __name__ == "__main__":
    create_structure()
