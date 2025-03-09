import requests


class ReleaseAPIClient:

    def __init__(self, server_address, username=None, password=None, personal_access_token=None):
        if not server_address:
            raise ValueError("server_address must not be empty.")
        self.server_address = server_address.rstrip('/')  # Ensure no trailing slash
        self.session = requests.Session()
        self.session.headers.update({"Accept": "application/json"})

        if username and password:
            self.session.auth = (username, password)
        elif personal_access_token:
            self.session.headers.update({"x-release-personal-token": personal_access_token})
        else:
            raise ValueError("Either username and password or a personal access token must be provided.")

    def _request(self, method, endpoint, params=None, json=None, data=None, **kwargs):
        url = f"{self.server_address}/{endpoint.lstrip('/')}"
        response = self.session.request(
            method, url, params=params, data=data, json=json, **kwargs
        )
        return response

    def get(self, endpoint, params=None, **kwargs):
        return self._request("GET", endpoint, params=params, **kwargs)

    def post(self, endpoint, json=None, data=None, **kwargs):
        return self._request("POST", endpoint, data=data, json=json, **kwargs)

    def put(self, endpoint, json=None, data=None, **kwargs):
        return self._request("PUT", endpoint, data=data, json=json, **kwargs)

    def delete(self, endpoint, params=None, **kwargs):
        return self._request("DELETE", endpoint, params=params, **kwargs)

    def patch(self, endpoint, json=None, data=None, **kwargs):
        return self._request("PATCH", endpoint, data=data, json=json, **kwargs)

    def close(self):
        self.session.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()
