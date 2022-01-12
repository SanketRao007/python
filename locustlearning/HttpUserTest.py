from locust import User, task, constant, HttpUser

class ReqRes(HttpUser):

    host= "https://reqres.in" # or you can supply this host into CLI --host=abc 
    wait_time = constant(1)

    @task
    def get_users(self):
        response = self.client.get("/api/users?page=2")
        print(response.text)
        print(response.status_code)
        print(response.headers)

    @task
    def create_user(self):
        response= self.client.post("/api/users", data="{'name':'abc', 'job':'leader'}")
        print(response.text)
        print(response.status_code)
        print(response.headers)