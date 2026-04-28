from pbi_automation.io.file_ops import read_json
from pbi_automation.core.registry import obj_reg


class Bookmark:
    def __init__(self, name, page, paths, display_name=None):
        self.paths = paths
        self.name = name
        self.page = page
        self.display_name = display_name if display_name else name

        self.file_path = str(self.paths.base_bookmark_template)
        self.json = read_json(self.file_path)

        self.json["name"] = f"'{self.name}'"
        self.json["displayName"] = f"'{self.display_name}'"
        self.json["selector"]["id"] = f"'{self.name}'"
        self.json["explorationState"]["activeSection"] = f"'{self.page.name}'"

        self.visuals = []
        obj_reg.register_object(self)

    def add_visual(self, visual):
        self.visuals.append(visual)

        self.json["options"]["targetVisualNames"].append(f"'{visual.name}'")
        self.json["explorationState"]["sections"][self.page.name]["visualContainers"][visual.name]["singleVisual"][
            "visualType"
        ] = visual.type

        self.json["explorationState"]["sections"][self.page.name]["visualContainers"][visual.name]["singleVisual"][
            "objects"
        ] = {}
