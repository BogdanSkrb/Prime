import os
import sys

resources_path = r'resources'

class ResourcesService:
    def __init__(self, image_name):
        module = sys.modules['__main__']
        path, _ = os.path.split(module.__file__)
        self._path = os.path.join(path, resources_path, image_name)

    @property
    def path(self):
        return self._path
