# Jira Issue Cloner

## Project Overview

This project is a Python-based automation tool designed to clone a specific Jira ticket and assign copies of it to multiple users. It is particularly useful for assigning the same task to a group of people, such as a class of students or a team.

## Prerequisites

*   **Python 3**: The project requires a Python 3 environment.
*   **Jira Library**: This project depends on the `jira` Python library.
    ```bash
    pip install jira
    ```

## Setup

### Credentials

The project requires a `credentials.py` file in the `jira_python/` directory to authenticate with your Jira instance. This file is git-ignored for security. You must create it manually with the following structure:

**File:** `jira_python/credentials.py`

```python
server = "https://your-domain.atlassian.net"
basic_auth = "your-email@example.com"
super_secret = "your-api-token"
```

*   `server`: The URL of your Jira instance.
*   `basic_auth`: Your Jira email address.
*   `super_secret`: Your Jira API token (not your password).

## Usage

The main script is `jira_python/create_issue.py`. It accepts command-line arguments to specify the source ticket, the target project, and the file containing the list of assignees.

### Command Format

```bash
python3 jira_python/create_issue.py --ticket=<TICKET_ID> --project=<PROJECT_KEY> --filename=<PATH_TO_CSV>
```

### Arguments

*   `--ticket`: The ID of the Jira ticket you want to clone (e.g., `PROJ-123`).
*   `--project`: The key of the project where the new tickets should be created (e.g., `PROJ`).
*   `--filename`: Path to a file containing the names of the assignees.

### Example

```bash
python3 jira_python/create_issue.py --ticket=Test-1 --project=TEST --filename=jira_python/helpers/class_names.csv
```

### Assignee File Format

The assignee file (e.g., `helpers/class_names.csv`) should be a plain text or CSV file with one name per line.

```text
Admas Kinfu
Victoria Moore
```

## Key Files

*   `jira_python/create_issue.py`: The main script that handles connecting to Jira, fetching the issue, and creating clones.
*   `jira_python/helpers/class_names.csv`: An example file containing a list of names to assign tickets to.
*   `jira_python/.gitignore`: Specifies files to be ignored by Git, including sensitive credentials.

## Development Notes

*   **Issue Type**: The script currently hardcodes the new issue type to `'Story'` in the `get_issue` function.
*   **Modifications**: To change the issue type or other fields, modify the `new_issue` dictionary in `jira_python/create_issue.py`.
