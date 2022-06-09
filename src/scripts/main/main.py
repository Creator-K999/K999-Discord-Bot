from gc import disable

from main_class import MainClass
from processor.management.object.objects_manager import ObjectsManager


def main():
    disable()

    main_object = ObjectsManager.create_object(MainClass)

    if main_object is None:
        print("main_class is None!")
        return 1

    main_object.run()

    ObjectsManager.delete_object("MainClass")
    ObjectsManager.detect_clear_memory_leaks()
    ...


if __name__ == '__main__':
    main()
