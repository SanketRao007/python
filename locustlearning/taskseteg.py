import random

from locust import constant, task, TaskSet, HttpUser


class HttpCat(TaskSet):
    @task
    def get_status(self):
        self.client.get("/200")
        print("get status for 200 ")

    @task
    def get_random_status(self):
        status_codes = [404,503,100,102,103,500]
        random_url = "/" + str(random.choice(status_codes))
        res = self.client.get(random_url)

        print("random http status")

class MyloadTest(HttpUser):
    host = "https://http.cat"
    wait_time = constant(1)
    tasks = [HttpCat]