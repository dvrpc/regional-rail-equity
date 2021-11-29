def print_title(message: str):
    """
    This decorator will print out a header
    row of dashes, and then the message.

    It then runs the function, and prints
    out a closing row of dots to visually
    group any printed output from the function.
    """

    def decorator(function):
        def wrapper(*args, **kwargs):
            print("-" * len(message))
            print(message)

            result = function(*args, **kwargs)

            print("." * len(message))
            return result

        return wrapper

    return decorator


def print_msg(message: str, tabs: int = 1, bullet: str = "->"):
    """
    Print a message that is tabbed in and uses a bullet-style prefix

    User may tweak number of tabs and the bullet style
    """
    print("\t" * tabs, bullet, message)
