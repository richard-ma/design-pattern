from abstractlogger import AbstractLogger


class ErrorLogger(AbstractLogger):
    def __init__(self, level: int):
        super().__init__()
        self._level = level

    def write(self, message: str):
        print("Error Console::Logger:", message)


if __name__ == "__main__":
    logger = ErrorLogger(AbstractLogger.INFO)
    logger.log_message(AbstractLogger.INFO, "test error logger")