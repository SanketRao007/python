from locust import constant, task,  HttpUser, SequentialTaskSet

class SeqTask(SequentialTaskSet):
    @task
    def get_status(self):
        self.client.get("/200")
        print("get status for 200 ")


    @task
    def get_500_status(self):
        self.client.get("/500")
        print("get status for 500 ")



class MyloadTest(HttpUser):
    host = "https://http.cat"
    wait_time = constant(1)
    tasks = [SeqTask]