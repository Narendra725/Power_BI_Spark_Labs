def create_object(cls, *args, **kwargs):
    return cls(*args, **kwargs)


class ObjRegister:
    def __init__(self):
        self.objects = []
        self.obj_names = []

    def register_object(self, obj):
        self.objects.append(obj)
        self.obj_names.append(getattr(obj, "name", obj.__class__.__name__))


obj_reg = ObjRegister()
