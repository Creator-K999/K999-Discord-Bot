from processor.logger.log import Log


class ObjectsManager:

    __objects = {}

    def __init__(self):\
        raise NotImplementedError("Cannot create instance of ObjectsManager!")

    @classmethod
    def create_object(cls, _object, *args, **kwargs):

        try:
            object_name = _object.__name__
            repr_name = f"'{object_name}'"

        except AttributeError as E:
            Log.exception(f"{_object} is not a class! {E}")
            return None

        try:
            cls.__objects[object_name] = _object(*args, **kwargs)
            Log.info(f"Successfully created {repr_name}")
            return cls.__objects[object_name]

        except Exception as E:
            Log.exception(f"Failed to create {repr_name}! {E}")
            return None

    @classmethod
    def delete_object(cls, object_name):

        if object_name not in cls.__objects:
            Log.warning(f"'{object_name}' doesn't exist!")
            return

        del cls.__objects[object_name]
        Log.info(f"Successfully deleted {object_name}")

    @classmethod
    def detect_clear_memory_leaks(cls):
        leaks_found = False
        Log.debug("Looking for memory leaks...")
        for object_name in cls.__objects:
            leaks_found = True
            Log.warning(f"Found a memory leak! {object_name}")
            del cls.__objects[object_name]

        if leaks_found:
            Log.warning("Found but cleared memory leaks!")
