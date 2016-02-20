import hashlib

import requests


def str2hex(string):
    string = hashlib.sha512(string.encode('utf-8')).hexdigest()
    for i in range(ord('c'), ord('z')):
        string = string.replace(chr(i), '')
    return string[10:16]


class GithubApi:
    url = 'https://api.github.com'
    headers = {'user-agent': 'babab.nl/0.1.0'}

    def __init__(self, username, ignore=[], throttle=True):
        self.repos = []
        self.username = username
        self.ignore = ignore
        self.throttle = throttle

    def makeRequest(self, path, media=None):
        if media:
            self.headers.update({'Accept': media})
        return requests.get(path, headers=self.headers)

    def getRepos(self, sort=True):
        request = self.makeRequest('{}/users/{}/repos'
                                   .format(self.url, self.username))
        repos = []
        for item in request.json():
            if not item['fork'] and item['name'] not in self.ignore:
                repos.append([item['updated_at'], item])
        if sort:
            repos.sort(reverse=True)

        result = []
        for item in repos:
            result.append(item[1])
        self.repos = result
        return result

    def printRepos(self):
        if not self.repos:
            self.getRepos()
        for item in self.repos:
            print('{:30} {} {}'.format(item['name'], item['updated_at'],
                                       item['homepage'] or '-'))
        return self

    def getReadmeContent(self, repo):
        request = self.makeRequest('{}/repos/{}/{}/readme'
                                   .format(self.url, self.username, repo),
                                   media='application/vnd.github.VERSION.html')
        return request.text
