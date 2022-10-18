from asyncio import Task
from locust import TaskSet, constant, task


class MyHttpCat(TaskSet):

    @task
    def get_status(self):
        self.client.get("/200")
        print("Get Status of 200")