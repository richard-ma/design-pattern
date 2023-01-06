from abstractlogger import AbstractLogger
from consolelogger import ConsoleLogger
from errorlogger import ErrorLogger
from filelogger import FileLogger


if __name__ == "__main__":
    def get_chain_of_loggers():
        errorLogger = ErrorLogger(AbstractLogger.ERROR)
        fileLogger = FileLogger(AbstractLogger.DEBUG)
        consoleLogger = ConsoleLogger(AbstractLogger.INFO)

        errorLogger.set_next_logger(fileLogger)
        fileLogger.set_next_logger(consoleLogger)

        return errorLogger

    logger_chain = get_chain_of_loggers()

    logger_chain.log_message(AbstractLogger.INFO, "This is an information")
    logger_chain.log_message(AbstractLogger.DEBUG, "This is a debug level information")
    logger_chain.log_message(AbstractLogger.ERROR, "This is an error information")