# ![Jira Logo](Jira_Logo.jpeg) Jira Issue Cloner

## Purpose
This project automates the process of cloning a specific Jira ticket and assigning copies to a list of multiple users. It is designed to streamline task distribution, such as assigning the same coursework to a class of students or a standard task to a team.

## Prerequisites

*   **Python 3**: Ensure you have Python 3 installed. You can download it from [python.org/downloads](https://www.python.org/downloads/).
*   **Jira Account**: Access to a Jira instance and an API token.
    *   **Sign up**: Get a free Jira account at [atlassian.com/software/jira](https://www.atlassian.com/software/jira/free).
    *   **API Token**: Generate an API token at [id.atlassian.com](https://id.atlassian.com/manage-profile/security/api-tokens).

## Dependencies

This project relies on the `jira` Python library. Install it using pip:

```bash
pip install jira
```

## Setup

1.  **Clone the repository** (if you haven't already).
2.  **Configure Credentials**:
    The script requires a `credentials.py` file to authenticate with Jira. This file is ignored by Git for security.
    
    Create a file named `credentials.py` inside the `jira_python/` directory with the following content:

    ```python
    # jira_python/credentials.py
    
    server = "https://your-domain.atlassian.net"
    basic_auth = "your-email@example.com"
    super_secret = "your-api-token"
    ```

    *   `server`: Your Jira instance URL.
    *   `basic_auth`: The email address associated with your Jira account.
    *   `super_secret`: Your Jira API token (generate one in your Atlassian account settings).

3.  **Prepare Assignee List**:
    Create a text or CSV file containing the names of the users you want to assign tickets to. See `jira_python/helpers/class_names.csv` for an example.

## How to Run

Navigate to the project root and run the script using the following command structure:

```bash
python3 jira_python/create_issue.py --ticket=<TICKET_ID> --project=<PROJECT_KEY> --filename=<PATH_TO_FILE>
```

### Arguments

* `--ticket`: The ID of the existing Jira ticket you want to clone (e.g., `TEST-1`).
* `--project`: The project key where the new tickets will be created (e.g., `TEST`).
* `--filename`: Relative path to the file containing the list of assignees.

### Example

```bash
python3 jira_python/create_issue.py --ticket=TEST-1 --project=TEST --filename=jira_python/helpers/class_names.csv
```

This command will:

1. Fetch the details of ticket `TEST-1`.
2. Read the list of names from `jira_python/helpers/class_names.csv`.
3. Create a new ticket in project `TEST` for each name in the file and assign it to them.
