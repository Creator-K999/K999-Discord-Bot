from inspect import stack
from threading import Lock, Thread
from logging import config, getLogger


class Log:

    config.fileConfig(fname="log.config")
    __logger = getLogger(__name__)

    __threads_count = 0

    __lock = Lock()

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
                target=lambda: cls.__logger.debug(
                    f"\n\tFILE: {caller_info.filename}"
                    f"\n\tFUNC: {caller_info.function}"
                    f"\n\tLINE: {caller_info.lineno}"
                    f"\n\tMESSAGE: {message}"
                ),
                args=()
            ).start()

    @classmethod
    def info(cls, message):
        with cls.__lock:
            caller_info = stack()[1]
            cls.__threads_count += 1

            Thread(
                daemon=True,
                name=f"Thread No. {cls.__threads_count}",
                target=lambda: cls.__logger.info(
                    f"\n\tFILE: {caller_info.filename}"
                    f"\n\tFUNC: {caller_info.function}"
                    f"\n\tLINE: {caller_info.lineno}"
                    f"\n\tMESSAGE: {message}"
                ),
                args=()
            ).start()

    @classmethod
    def warning(cls, message):
        with cls.__lock:
            caller_info = stack()[1]
            cls.__threads_count += 1

            Thread(
                daemon=True,
                name=f"Thread No. {cls.__threads_count}",
                target=lambda: cls.__logger.warning(
                    f"\n\tFILE: {caller_info.filename}"
                    f"\n\tFUNC: {caller_info.function}"
                    f"\n\tLINE: {caller_info.lineno}"
                    f"\n\tMESSAGE: {message}"
                ),
                args=()
            ).start()

    @classmethod
    def error(cls, message):
        with cls.__lock:
            caller_info = stack()[1]
            cls.__threads_count += 1

            Thread(
                daemon=True,
                name=f"Thread No. {cls.__threads_count}",
                target=lambda: cls.__logger.error(
                    f"\n\tFILE: {caller_info.filename}"
                    f"\n\tFUNC: {caller_info.function}"
                    f"\n\tLINE: {caller_info.lineno}"
                    f"\n\tMESSAGE: {message}"
                ),
                args=()
            ).start()

    @classmethod
    def exception(cls, message):
        with cls.__lock:
            caller_info = stack()[1]
            cls.__threads_count += 1

            Thread(
                daemon=True,
                name=f"Thread No. {cls.__threads_count}",
                target=lambda: cls.__logger.exception(
                    f"\n\tFILE: {caller_info.filename}"
                    f"\n\tFUNC: {caller_info.function}"
                    f"\n\tLINE: {caller_info.lineno}"
                    f"\n\tMESSAGE: {message}"
                ),
                args=()
            ).start()

    @classmethod
    def critical(cls, message):
        with cls.__lock:
            caller_info = stack()[1]
            cls.__threads_count += 1

            Thread(
                daemon=True,
                name=f"Thread No. {cls.__threads_count}",
                target=lambda: cls.__logger.critical(
                    f"\n\tFILE: {caller_info.filename}"
                    f"\n\tFUNC: {caller_info.function}"
                    f"\n\tLINE: {caller_info.lineno}"
                    f"\n\tMESSAGE: {message}"
                ),
                args=()
            ).start()
