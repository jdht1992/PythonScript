class MyCustomeError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        print("calling str")
        if self.message:
            #return f"MyCustomError {self.message}"
            return "MyCustomError {0}".format(self.message)
        else:
            return "MyCustomError has been raised"

raise MyCustomeError("we have a problem")

# #########################################

class MyCustomeError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            response = {
                "code": 1000,
                "message": "Validation Failed",
                "errors": [
                    {
                        "code": 2031,
                        "field": self.message,
                        "message": "Este campo no puede estar en blanco."
                    }]
            }
            return "{0}".format(response)
        else:
            return "MyCustomError has been raised"

raise MyCustomeError("image")