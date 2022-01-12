from locust import User, task, constant


class  MyFirstTest(User):
    weight = 2
    wait_time = constant(1)
    @task
    def launch(self):
        print("launching url")

    @task
    def searching(self):
        print("searching")

class  MySecondTest(User):
    weight = 2
    wait_time = constant(1)
    @task
    def launch2(self):
        print("launching 2 url")

    @task
    def searching2(self):
        print("searching 2")