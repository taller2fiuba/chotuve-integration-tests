class ChotuveAppError(Exception):
    def __init__(self, response, *args, **kwargs):
        self.response = response
        self.status_code = response.status_code

    def __str__(self):
        return f'{self.response.url} respondió {self.response.status_code}\n' + \
               f'{self.response.text}'
