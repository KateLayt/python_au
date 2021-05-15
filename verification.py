import requests
import json

TOKEN = '06fc997b5ae8c70e3ffdf2573a33407f2579cc5f' 
PREFIXES = ['GENERATOR', 'LEETCODE', 'HEXNUMBER','ITERATOR', 'TRIANGLE', 'REQUESTS']
GROUPS = ['1011','1012','1021','1022']
ACTIONS = ['Added','Deleted','Refactored','Fixed']

def prepare_headers():
  return{'Authorization': 'Token {}'.format(TOKEN),
      'Content-Type': "application/json",
      'Accept': "application/vnd.github.v3+json"
  }


def send_pr_comment(pr, errors):
  data = {'body': errors,
          'path': requests.get(pr['url']+'/files', headers=prepare_headers()).json()[0]['filename'],
          'position': 1,
          'commit_id': pr['head']['sha']}
  r = requests.post(pr['url']+'/comments', headers=prepare_headers(), json=data)
  print(r.json())
  print(r.status_code)


def get_all_pr_commits(pr):
  result = []
  commitpage = requests.get(pr["commits_url"], headers = prepare_headers())
  for pc in commitpage.json():
    commit = pc["commit"]
    result.append(commit)
  return result


def check_prefixes(title): 
  errors = ''
  parts_of_title = title.split('-')[:2]
  if len(parts_of_title) == 2:
    parts_of_title += parts_of_title[1].split()
    print(parts_of_title)
    if len(parts_of_title) != 5:
      parts_of_title = [1, 2, 3, 4]
  else:
    parts_of_title = [1, 2, 3, 4]
  if not(parts_of_title[0] in PREFIXES):
    errors += 'Pull Request prefix must contain prefix in {}. '.format(PREFIXES)
  if not(parts_of_title[2] in GROUPS):
    errors += 'Pull Request title must contain group number in {}. '.format(GROUPS)
  if not(parts_of_title[3] in ACTIONS):
    errors += 'Pull Request action must contain action in {}. '.format(ACTIONS)
  return errors
    

def get_all_user_pr(user_login, repo_name, pr_state): 
  r = requests.get('https://api.github.com/repos/{}/{}/pulls?state={}'.format(user_login, repo_name, pr_state), headers = prepare_headers())
  return r


def main():
  prs = get_all_user_pr('KateLayt', 'python_au', 'open')
  for pr in prs.json():
    errors = ''
    comms = get_all_pr_commits(pr)
    commit_date = get_last_commit_date(pr)
    comment_date = get_last_comment_date(pr)
    if comment_date != "0000-00-00T00:00:00Z" and commit_date > comment_date:
      for commit in comms:
        errors += check_prefixes(commit['message'])
      if len(errors) > 0:
        send_pr_comment(pr, errors)  


def get_last_commit_date(pull):
    commitpage = requests.get(pull["commits_url"], headers = prepare_headers())  
    return commitpage.json()[-1]["commit"]["author"]["date"]


def get_last_comment_date(pull):
  commentpg = requests.get(pull["review_comments_url"], headers = prepare_headers())
  if len(commentpg.json()) > 0:
    return commentpg.json()[-1]["created_at"]
  return "0000-00-00T00:00:00Z"

