class Settings:
    """
    Settings: 
    model for wasy adding handlers to http
    """
    def __init__(self, get_func, post_func) -> None:
        """
        Initialize 
        get two functions: for handle get requests and for handle post requests
        get function get 0 positional arguments
        post function get 1 positional argument - dictionary (json from request)
        """
        self.get_func = get_func
        self.post_func = post_func
    
    def get(self) -> tuple:
        return self.get_func()
    
    def post(self, data: dict) -> tuple:
        return self.post_func(data)