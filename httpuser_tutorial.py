from locust import HttpUser, task, constant

# HttpUser class
## represents a HTTP user which spawns and attacks the system
## it creates a 'client' instance of HttpSession
## get, post, delete, patch, head, put, headers, text, status_code etc.


class FirstLoadTest(HttpUser):
    wait_time = constant(1)
    host = 'https://reqres.in'

    @task
    def get_users(self):
        self.client.get('/api/users?page=2')

    @task 
    def create_user(self):
        self.client.post('/api/users',
         data="""
        {
            "name": "morpheus",
            "job": "leader",
        }
        """)
