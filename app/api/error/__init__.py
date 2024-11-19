from werkzeug.exceptions import HTTPException

class ResponseError(HTTPException):
    def __init__(self, code: int, description: str):
        super().__init__(description)
        
        self.code = code
        self.description = description

    def __str__(self):
        return f"[{self.code}] {self.description}"