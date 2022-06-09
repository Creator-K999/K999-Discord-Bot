from inspect import stack
from threading import Lock, Thread
from logging import config, getLogger


class Log:
    __lock = Lock()
    __threads_count = 0

    config.fileConfig(fname="log.config")
    __logger = getLogger(__name__)

    def __init__(self):
        raise NotImplementedError("Cannot create instance of Log!")

    @classmethod
    def debug(cls, message):
        with cls.__lock:
            caller_info = stack()[1]
            cls.__threads_count += 1

            Thread(
                daemon=True,
                name=f"Thread No. {cls.__threads_count}",
                target=cls.__logger.debug,
                args=(
                    f"\n\tFILE: {caller_info.filename}"
                    f"\n\tFUNC: {caller_info.function}"
                    f"\n\tLINE: {caller_info.lineno}"
                    f"\n\tMESSAGE: {message}\n"
                    ,)
            ).start()

    @classmethod
    def info(cls, message):
        with cls.__lock:
            caller_info = stack()[1]
            cls.__threads_count += 1

            Thread(
                daemon=True,
                name=f"Thread No. {cls.__threads_count}",
                target=cls.__logger.info,
                args=(
                    f"\n\tFILE: {caller_info.filename}"
                    f"\n\tFUNC: {caller_info.function}"
                    f"\n\tLINE: {caller_info.lineno}"
                    f"\n\tMESSAGE: {message}\n"
                    ,)
            ).start()

    @classmethod
    def warning(cls, message):
        with cls.__lock:
            caller_info = stack()[1]
            cls.__threads_count += 1

            Thread(
                daemon=True,
                name=f"Thread No. {cls.__threads_count}",
                target=cls.__logger.warning,
                args=(
                    f"\n\tFILE: {caller_info.filename}"
                    f"\n\tFUNC: {caller_info.function}"
                    f"\n\tLINE: {caller_info.lineno}"
                    f"\n\tMESSAGE: {message}\n"
                    ,)
            ).start()

    @classmethod
    def error(cls, message):
        with cls.__lock:
            caller_info = stack()[1]
            cls.__threads_count += 1

            Thread(
                daemon=True,
                name=f"Thread No. {cls.__threads_count}",
                target=cls.__logger.error,
                args=(
                    f"\n\tFILE: {caller_info.filename}"
                    f"\n\tFUNC: {caller_info.function}"
                    f"\n\tLINE: {caller_info.lineno}"
                    f"\n\tMESSAGE: {message}\n"
                    ,)
            ).start()

    @classmethod
    def exception(cls, message):
        with cls.__lock:
            caller_info = stack()[1]
            cls.__threads_count += 1

            Thread(
                daemon=True,
                name=f"Thread No. {cls.__threads_count}",
                target=cls.__logger.exception,
                args=(
                    f"\n\tFILE: {caller_info.filename}"
                    f"\n\tFUNC: {caller_info.function}"
                    f"\n\tLINE: {caller_info.lineno}"
                    f"\n\tMESSAGE: {message}\n"
                    ,)
            ).start()

    @classmethod
    def critical(cls, message):
        with cls.__lock:
            caller_info = stack()[1]
            cls.__threads_count += 1

            Thread(
                daemon=True,
                name=f"Thread No. {cls.__threads_count}",
                target=cls.__logger.critical,
                args=(
                    f"\n\tFILE: {caller_info.filename}"
                    f"\n\tFUNC: {caller_info.function}"
                    f"\n\tLINE: {caller_info.lineno}"
                    f"\n\tMESSAGE: {message}\n"
                    ,)
            ).start()
