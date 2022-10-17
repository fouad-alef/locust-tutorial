from locust import User, task, constant


class FirstTest(User):
    """class to test users (not http users)."""
    weight = 2
    wait_time = constant(1)
    @task
    def launch(self):
        print("Luanching the url")


    @task(3)
    def search(self):
        print("Searching")


class SecondTest(User):
    """class to test users (not http users)."""
    weight = 2
    wait_time = constant(1)
    @task
    def launch2(self):
        print("2 Luanching the url")


    @task
    def search(self):
        print("2 Searching")


# to run this file:
## locust -f user_class_tutorial.py
## when running this file, the web UI can be accessed to pass the number of users and spawn time (in seconds)
## the print statement will be displayed in terminal output with "Searching" being 3 times as likely to be printed