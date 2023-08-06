from locust import HttpUser, task
            
class User(HttpUser):
    host= HttpUser.host
    @task
    def mainPage(self):
        self.client.get("{}".format(self.host))
        
