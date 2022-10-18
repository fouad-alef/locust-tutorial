from asyncio import Task
from locust import HttpUser, TaskSet, constant, task
import random

class MyHttpCat(TaskSet):

    @task
    def get_status(self):
        self.client.get("/200")
        print("Get Status of 200")

    @task
    def get_random_status(self):
        status_codes = [100, 101, 102, 200, 201, 202, 203, 204, 300, 301, 302, 400, 401, 402, 403]
        random_url = f"/{random.choice(status_codes)}"
        res = self.client.get(random_url)
        print(f"Random Http status {random_url.strip('/')}")


class MyLoadTest(HttpUser):
    host = "https://http.cat"
    tasks = [MyHttpCat]
    wait_time = constant(1)


