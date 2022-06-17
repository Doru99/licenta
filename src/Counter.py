class Counter:
    val = 0

    @staticmethod
    def reset_counter():
        Counter.val = 0
        return Counter.val

    @staticmethod
    def get_counter():
        return Counter.val

    @staticmethod
    def count_up():
        Counter.val += 1

    @staticmethod
    def count_down():
        Counter.val -= 1
