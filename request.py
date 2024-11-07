import requests
from collections import deque


class RequestStack:
    """Stack to store requests in LIFO order."""

    def __init__(self):
        self.stack = deque()

    def push(self, request_info):
        """Pushes request information to the stack."""
        self.stack.append(request_info)

    def pop(self):
        """Pops the last request information from the stack."""
        if not self.is_empty():
            return self.stack.pop()
        raise IndexError("pop from an empty stack")

    def peek(self):
        """Peeks at the last request information in the stack."""
        if not self.is_empty():
            return self.stack[-1]
        raise IndexError("peek from an empty stack")

    def is_empty(self):
        """Checks if the stack is empty."""
        return len(self.stack) == 0

    def size(self):
        """Returns the size of the stack."""
        return len(self.stack)


class RequestHandler:
    def __init__(self, url):
        self.url = url
        self.request_stack = RequestStack()

    def delete_request(self, resource_id, headers=None):
        """Sends a DELETE request to delete a specific resource."""
        response = requests.delete(f"{self.url}/{resource_id}", headers=headers)
        self._handle_response(response, "DELETE", {"resource_id": resource_id, "headers": headers})
        return response.json() if response.content else None

    def get_request(self, params=None, headers=None):
        """Sends a GET request to retrieve data."""
        response = requests.get(self.url, params=params, headers=headers)
        self._handle_response(response, "GET", {"params": params, "headers": headers})
        return response.json() if response.content else None

    def head_request(self, headers=None):
        """Sends a HEAD request to retrieve headers only."""
        response = requests.head(self.url, headers=headers)
        self._handle_response(response, "HEAD", {"headers": headers})
        return response.headers

    def patch_request(self, resource_id, data=None, headers=None):
        """Sends a PATCH request to partially update a resource."""
        response = requests.patch(f"{self.url}/{resource_id}", json=data, headers=headers)
        self._handle_response(response, "PATCH", {"resource_id": resource_id, "data": data, "headers": headers})
        return response.json() if response.content else None

    def post_request(self, data=None, headers=None):
        """Sends a POST request to create a new resource."""
        response = requests.post(self.url, json=data, headers=headers)
        self._handle_response(response, "POST", {"data": data, "headers": headers})
        return response.json() if response.content else None

    def put_request(self, resource_id, data=None, headers=None):
        """Sends a PUT request to update or replace a resource."""
        response = requests.put(f"{self.url}/{resource_id}", json=data, headers=headers)
        self._handle_response(response, "PUT", {"resource_id": resource_id, "data": data, "headers": headers})
        return response.json() if response.content else None

    def custom_request(self, method, data=None, params=None, headers=None):
        """Sends a custom request of the specified method."""
        response = requests.request(method, self.url, json=data, params=params, headers=headers)
        self._handle_response(response, method.upper(), {"data": data, "params": params, "headers": headers})
        return response.json() if response.content else None

    def _handle_response(self, response, method, request_data):
        """Logs request data in LIFO stack and prints response details."""
        self.request_stack.push({"method": method, "response": response, "data": request_data})
        self._print_response(response, method)

    def _print_response(self, response, method):
        """Helper method to print response details."""
        if response.status_code in (200, 201):
            print(f"{method} request successful. Status Code: {response.status_code}")
            print("Response:", response.json() if response.content else "No Content")
        else:
            print(f"{method} request failed. Status Code: {response.status_code}")

    def pop_last_request(self):
        """Retrieves the last request made in LIFO order."""
        if not self.request_stack.is_empty():
            last_request = self.request_stack.pop()
            print(f"Last request - Method: {last_request['method']}, Data: {last_request['data']}")
            return last_request
        print("No requests in stack.")
        return None


# Usage examples:
url = "https://jsonplaceholder.typicode.com/posts"
handler = RequestHandler(url)

# DELETE request
handler.delete_request(1)


# GET request
handler.get_request(params={"userId": 1})

# HEAD request
handler.head_request()

# PATCH request
handler.patch_request(1, data={"title": "Updated Title"})

# POST request
handler.post_request(data={"title": "New Post", "body": "This is a new post", "userId": 1})

# PUT request
handler.put_request(1, data={"title": "Replaced Title", "body": "This is the updated content", "userId": 1})

# Custom request (e.g., POST)
handler.custom_request("POST", data={"title": "Custom Request Title", "body": "Custom request content", "userId": 1})

# Retrieve last request in LIFO order
handler.pop_last_request()
