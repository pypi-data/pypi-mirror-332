class APIError(Exception):
    def __init__(self, message, status_code):
        super().__init__(f"APIError {status_code}: {message}")
        self.status_code = status_code
