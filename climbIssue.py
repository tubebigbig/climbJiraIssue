from jira import JIRA
import configparser
import re
p1 = re.compile('[0-9]')
config = configparser.ConfigParser()
try:
    config.read('climbIssue.ini')
    user = config.get('DEFAULT', 'user_name')
    apikey = config.get('DEFAULT', 'api_key')
    server = config.get('DEFAULT', 'server')
    finish_text = config.get('DEFAULT', 'finish_text')
except:
    print("[Error] no such .ini file Or ini cfg is wrong")
    input("Press Enter to continue...")
options = {'server': server}
try:
    jira = JIRA(options, basic_auth=(user, apikey))
except:
    print("[Error]fail to connect jira server")
    input("Press Enter to continue...")
project = input("Please enter project(ZRSH):")
sprint = input("Please enter Sprint(openSprints()):")
assignee = input("Please enter assignee people(self):")
if not project:
    project = 'ZRSH'
if not sprint:
    sprint = ' in openSprints()'
else:
    sprint = '= ' + sprint
if not assignee:
    assignee = 'currentUser()'
jira_search_str = "project="\
        + project\
        + " and Sprint"\
        + sprint

if 'all' != assignee.lower():
    jira_search_str += " and assignee = " + assignee
issues = jira.search_issues(jira_search_str)

### search single issue
# issue = input("issue:")
# issue = jira.issue(issue)
# for field_name in issue.raw['fields']:
#     print("Field:", field_name, "Value:", issue.raw['fields'][field_name])
# print(issue.fields.project.key)            # 'JRA'
# print(issue.fields.issuetype.name)         # 'New Feature'
# print(issue.fields.reporter.displayName)   # 'Mike Cannon-Brookes [Atlassian]'

### output jira issue
outfile = open("output.txt", "w")
for issue in issues:
    issue_status =  issue.fields.status.name
    is_done = 'x' if issue_status == finish_text else ' '
#     print("issue No:", issue, ",issue name:", issue.fields.summary)
    outstr = '- ['\
            + is_done \
            +'] | ['\
            + str(issue) \
            + '](https://info360.atlassian.net/browse/' \
            + str(issue) \
            + ') |' \
            + issue.fields.summary \
            + '| ' \
            + issue.fields.assignee.displayName \
            + ' | <font color="red">' \
            + issue.fields.priority.name \
            + '</font> |\n'
    csvstr = issue.fields.summary \
            + '\t\t' \
            + 'https://info360.atlassian.net/browse/'\
            + str(issue) \
            + '\t' \
            + issue.fields.priority.name \
            + '\t' \
            + issue.fields.status.name \
            + '\n'
    outfile.write(outstr)
print('Pick up jira issue to output.txt success')
