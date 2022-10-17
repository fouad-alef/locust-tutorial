from locust import HttpUser, task, between
import time

class QuickstartUser(HttpUser):
    """A quickstart user for users that are to be simulated
    -  inherits from HttpUser which gives each user a  client attribute  (instance of HttpSession to make HTTP requests to the target system to load test
    -  when load testing starts, locust will create an instance of this class for each user.
    
    """
    # simulated wait between 1 and 5 seconds after each task is executed
    wait_time = between(1, 5)

    @task # the core of locust file
    # for each running user, Locust creates a greenlet that will call these methods
    def hello_world(self):
        # self.client makes it possible to make HTTP calls that will be logged by Locust
        self.client.get('/hello')
        self.client.get('/world')

    @task(3) # higher weight which makes locust picking this method three times more likely
    def view_items(self):
        for item_id in range(10):
            self.client.get(f'/item?id={item_id}', name='/item')
            time.sleep(1)

    def on_start(self):
        """will be called for each simulated user when they start (on_start, on_stop)"""
        self.client.post("/login", json={"username":"foo", "password":"bar"})

