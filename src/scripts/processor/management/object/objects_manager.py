class ObjectsManager:

    __objects = {}

    @classmethod
    def create_object(cls, _object, *args, **kwargs):

        try:
            object_name = _object.__name__
            repr_name = f"'{object_name}'"

        except AttributeError:
            print(f"{_object} is not a class!")
            return None

        try:
            cls.__objects[object_name] = _object(*args, **kwargs)
            print(f"Successfully created {repr_name}")
            return cls.__objects[object_name]

        except Exception as E:
            print(f"Failed to create {repr_name}\n{E}")
            return None

    @classmethod
    def delete_object(cls, object_name):

        if object_name not in cls.__objects:
            print(f"'{object_name}' doesn't exist!")
            return

        del cls.__objects[object_name]

    @classmethod
    def detect_clear_memory_leaks(cls):
        leaks_found = False
        print("Looking for memory leaks!")
        for object_name in cls.__objects:
            leaks_found = True
            print(f"Found a memory leak! {object_name}")
            del cls.__objects[object_name]

        if leaks_found:
            print("Found but cleared memory leaks!")
