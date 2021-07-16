from jira import JIRA
import configparser
config = configparser.ConfigParser()
try:
    config.read('climbIssue.ini')
    user = config.get('DEFAULT', 'user_name')
    apikey = config.get('DEFAULT', 'api_key')
    server = config.get('DEFAULT', 'server')
except:
    print("[Error] no such .ini file Or ini cfg is wrong")
    input("Press Enter to continue...")
options = {'server': server}
try:
    jira = JIRA(options, basic_auth=(user, apikey))
except:
    print("[Error]fail to connect jira server")
    input("Press Enter to continue...")
### search single issue
issue = input("issue:")
issue = jira.issue(issue)
# print(issue.fields.status.name)
for field_name in issue.raw['fields']:
    print("Field:", field_name, "Value:", issue.raw['fields'][field_name])
# print(issue.fields.project.key)            # 'JRA'
# print(issue.fields.issuetype.name)         # 'New Feature'
# print(issue.fields.reporter.displayName)   # 'Mike Cannon-Brookes [Atlassian]'
