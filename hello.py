def new_decorator(func):

    def process():

        print("First line")

        func()

        print("Last line")

    return process

@new_decorator
def needs_dec():
    print("Middle line")

needs_dec()
