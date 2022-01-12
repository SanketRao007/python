from locust import constant, task, TaskSet, HttpUser



class HttpCat(TaskSet):
    @task
    def get_status(self):
        self.client.get("/200")
        print("get status for 200 ")

    @task
    class HttpCat2(TaskSet):
        @task
        def get_500_status(self):
            self.client.get("/500")
            print("get status for 500 ")
            self.interrupt(reschedule=False)


class MyloadTest(HttpUser):
    host = "https://http.cat"
    wait_time = constant(1)
    tasks = [HttpCat]