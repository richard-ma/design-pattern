from abstractlogger import AbstractLogger


class ConsoleLogger(AbstractLogger):
    def __init__(self, level: int):
        super().__init__()
        self._level = level

    def write(self, message: str):
        print("Standard Console::Logger:", message)


if __name__ == "__main__":
    logger = ConsoleLogger(AbstractLogger.INFO)
    logger.log_message(AbstractLogger.INFO, "test console logger")