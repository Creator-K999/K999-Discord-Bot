from gc import disable
from threading import enumerate as threads_enumerate

from main_class import MainClass
from processor.logger.log import Log
from processor.management.object.objects_manager import ObjectsManager


def main():
    disable()

    Log.debug("Application Started!")
    Log.debug("Creating 'MainClass'")
    main_object = ObjectsManager.create_object(MainClass)

    if main_object is None:
        Log.critical("main_class is None!")
        return 1

    main_object.run()

    ObjectsManager.delete_object("MainClass")
    ObjectsManager.detect_clear_memory_leaks()

    for thread in threads_enumerate():
        if thread.name != "MainThread":
            print(f"Warning! {thread.name} is still running!")
            thread.join()

    print("Waited for all threads!")


if __name__ == '__main__':
    main()
