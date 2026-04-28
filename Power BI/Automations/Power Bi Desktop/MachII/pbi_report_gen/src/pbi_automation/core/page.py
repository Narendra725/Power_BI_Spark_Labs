from pbi_automation.io.file_ops import read_json
from pbi_automation.core.registry import obj_reg, create_object
from pbi_automation.core.visuals import PageNavigator


class Group:
    def __init__(self, name, page, paths, display_name=None):
        self.paths = paths
        self.name = name

        self.position = {
            "x": None,
            "y": None,
            "z": None,
            "height": None,
            "width": None,
        }

        self.display_name = display_name if display_name else name
        self.visuals = []

        self.file_path = str(self.paths.base_group_json)
        self.json = read_json(self.file_path)
        self.json["name"] = self.name
        self.json["visualGroup"]["displayName"] = self.display_name

        self.page = page
        obj_reg.register_object(self)

    def add_visual(self, visual_cls, *args, **kwargs):
        visual = create_object(visual_cls, *args, **kwargs)
        self.visuals.append(visual)

        self.page.add_visual(visual)
        visual.json["parentGroupName"] = self.name
        return visual


class Page:
    def __init__(self, name, paths, display_name=None, chapter=None, is_home=False, width=1024, height=720):
        self.paths = paths
        self.report = None

        self.is_home = is_home
        self.width = width
        self.height = height

        self.name = name
        self.display_name = display_name if display_name else name

        self.verticalAlignment = "Middle"
        self.background = {"Literal": {"Value": "#FFFFFF"}}

        self.file_path = str(self.paths.base_page_json)
        self.json = read_json(self.file_path)

        self.json["name"] = self.name
        self.json["displayName"] = self.display_name
        self.json["height"] = self.height
        self.json["width"] = self.width

        self.chapter = chapter
        self.visuals = []
        self.bookmarks = []

        obj_reg.register_object(self)

    def add_group(self, grp_name, display_name=None):
        group_obj = Group(grp_name, self, self.paths, display_name)
        self.visuals.append(group_obj)
        group_obj.page = self
        return group_obj

    def add_page_navigator(self, navigator_name):
        navigator = PageNavigator(navigator_name, self.paths, self.name)
        self.visuals.append(navigator)
        navigator.main_page = self.name
        return navigator

    def link_to_report(self, report):
        self.report = report

    def add_visual(self, visual):
        self.visuals.append(visual)
