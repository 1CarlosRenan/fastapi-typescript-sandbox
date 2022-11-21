import os


class Config:
    def __init__(self):
        self.PORT = int(os.getenv("SERVER_PORT", 3000))
        self.ENVIRONMENT = os.getenv("ENVIRONMENT")
        self.DEFAULT_REDIRECT = os.getenv("DEFAULT_REDIRECT", "http://localhost:3000/docs")


config = Config()
