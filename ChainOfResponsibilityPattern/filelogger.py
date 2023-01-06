from abstractlogger import AbstractLogger


class FileLogger(AbstractLogger):
    def __init__(self, level: int):
        super().__init__()
        self._level = level

    def write(self, message: str):
        print("File::Logger:", message)


if __name__ == "__main__":
    logger = FileLogger(AbstractLogger.INFO)
    logger.log_message(AbstractLogger.INFO, "test file logger")