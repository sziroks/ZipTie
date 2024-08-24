class SingletonMeta(type):
    _instances: dict = {}

    def __call__(cls, *args, **kwargs):
        """
        This method overrides the default behavior of creating an instance of a class.
        It ensures that only one instance of a class is created, and subsequent calls to the class
        will return the same instance.

        Parameters:
        *args: Variable length argument list. These arguments are passed to the class's __init__ method.
        **kwargs: Arbitrary keyword arguments. These arguments are passed to the class's __init__ method.

        Returns:
        The singleton instance of the class.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]
