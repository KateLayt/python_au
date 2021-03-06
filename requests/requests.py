import requests
import json

TOKEN = '7646b28b57b06bf46eec36dc67c1547f70972250'
PREFIXES = ['GENERATOR', 'LEETCODE', 'HEXNUMBER', 'ITERATOR', 'TRIANGLE']
GROUPS = ['1011', '1012', '1021', '1022']
ACTIONS = ['Added', 'Deleted', 'Refactored', 'Fixed']


def prepare_headers():
    return {'Authorization': 'Token {}'.format(TOKEN),
            'Content-Type': "application/json",
            'Accept': "application/vnd.github.v3+json"
            }


def send_pr_comment(pr, errors):
    data = {'body': errors,
            'path': requests.get(pr['url'] + '/files', headers=prepare_headers()).json()[0]['filename'],
            'position': 1,
            'commit_id': pr['head']['sha']}
    r = requests.post(pr['url'] + '/comments', headers=prepare_headers(), json=data)
    print(r.json())
    print(r.status_code)


def get_all_pr_commits(pr):
    result = []
    commitpage = requests.get(pr["commits_url"], headers=prepare_headers())
    for pc in commitpage.json():
        commit = pc["commit"]
        result.append(commit)
    return result


def check_prefixes(title):
    errors = ''
    parts_of_title = title.split('-')[:2]
    parts_of_title += parts_of_title[1].split()
    if not (parts_of_title[0] in PREFIXES):
        errors += 'Pull Request prefix must contain prefix in {}. '.format(PREFIXES)
    if not (parts_of_title[2] in GROUPS):
        errors += 'Pull Request title must contain group number in {}. '.format(GROUPS)
    if not (parts_of_title[3] in ACTIONS):
        errors += 'Pull Request action must contain action in {}. '.format(ACTIONS)
    return errors


def get_all_user_pr(user_login, repo_name, pr_state):
    r = requests.get('https://api.github.com/repos/{}/{}/pulls?state={}'.format(user_login, repo_name, pr_state),
                     headers=prepare_headers())
    return r


def main():
    prs = get_all_user_pr('KateLayt', 'python_au', 'open')
    for pr in prs.json():
        errors = ''
        comms = get_all_pr_commits(pr)
        for commit in comms:
            errors += check_prefixes(commit['message'])
        if len(errors) > 0:
            send_pr_comment(pr, errors)


main()