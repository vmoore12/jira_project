"""
This project clones a ticket from jira and assigns it to multiple users.
You will need to first create a ticket in Jira, and csv file with names of people you want to assign.

CLI example:

 $ python3 create_issue.py --ticket=Test-1 --project=TEST --filename=helpers/class_names.csv
"""

import argparse
from jira import JIRA
from credentials import server, super_secret, basic_auth




# connected to Jira account:
jira = JIRA(
    server= server, # Url to your jira account
    basic_auth=(basic_auth,super_secret)) # username and secret key for authentication


parser = argparse.ArgumentParser(description='Copy a ticket from jira')
parser.add_argument('--ticket', metavar='ticket', type=str, help='enter your jira ticket name')
parser.add_argument('--project', metavar='project', type=str, help='project name')
parser.add_argument('--filename', metavar='filepath', type=str, help='Enter the file path')
args = parser.parse_args()

jira_ticket = args.ticket
jira_project = args.project
assignee = args.filename

# get issue from Jira website:
def get_issue():

    """ Gets the issue from Jira website

    Returns:
        issue information from Jira.
    """
    issue = jira.issue(jira_ticket, fields='summary, description, issuetype',)
    print(issue)

    new_issue = {
            'project':{'key':jira_project},
            'summary': issue.fields.summary,
            'description': issue.fields.description,
            'issuetype': {'name': 'Story'},
        
        }

    return new_issue


# clone issue 
def cloned_issue(issue_details):
    """_summary_
    copies issue created from Jira website and assigns them to other students.
    Args:
        issue_details (bool): issue details from get_issue().

    Returns:
        copied issue with assigned student.
    """
    
    with open(assignee, 'r') as f:
        names = f.readlines()
        new_names =[i.strip('\n').strip(',') for i in names]    
        print(new_names)
    for name in new_names:
        copy = jira.create_issue(issue_details)
        copies = jira.assign_issue(copy, name)
        print(copies)

    return issue_details

ticket_details = get_issue()
cloned_issue(ticket_details)
