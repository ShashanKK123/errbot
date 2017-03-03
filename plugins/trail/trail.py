import requests
import ast
import jenkins
from jenkins import Jenkins
from errbot import botcmd, BotPlugin
from config import JENKINS_URL, JENKINS_USERNAME, JENKINS_PASSWORD
from jenkinsapi.jenkins import Jenkins

class Trail(BotPlugin):
    @botcmd
    def getjobs(self, msg, args):
        #server = self.get_server_instance()
        server= Jenkins(JENKINS_URL, username=JENKINS_USERNAME, password=JENKINS_PASSWORD)
        for j in server.get_jobs():
            jobs = server.get_job(j[0])
            return jobs.name
    @botcmd
    def getjenkinsviews(self, msg, args):
        server= Jenkins(JENKINS_URL, username=JENKINS_USERNAME, password=JENKINS_PASSWORD)
        #server = Jenkins(JENKINS_URL, username=JENKINS_USERNAME, password=JENKINS_PASSWORD)
        views = server.get_views()
        return views.json()    