from gc import disable

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


if __name__ == '__main__':
    main()
