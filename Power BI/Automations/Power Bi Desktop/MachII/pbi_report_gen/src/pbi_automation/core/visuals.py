from pbi_automation.io.file_ops import read_json
from pbi_automation.core.registry import obj_reg


class Visual:
    def __init__(self, name, vtype, paths):
        self.name = name
        self.type = vtype
        self.paths = paths

        self.file_path = str(self.paths.resolve_visual_template(self.type))

        self.position = {
            "x": None,
            "y": None,
            "z": None,
            "tabOrder": None,
            "width": None,
            "height": None,
        }

        self.groups = []
        self.bookmark = []
        self.background = "#FFFFFF"
        self.border_color = "#000000"
        self.font_color = "#000000"
        self.page = ""

        self.json = read_json(self.file_path)
        self.json["name"] = self.name
        self.json["position"] = self.position

        obj_reg.register_object(self)

    def add_to_group(self, grp_name):
        self.groups.append(grp_name)

    def add_to_bookmark(self, bookmark_name):
        self.bookmark.append(bookmark_name)

    def add_to_page(self, page_name):
        self.page = page_name

    def set_position(self, x, y, z, tabOrder, width, height):
        self.position["x"] = x
        self.position["y"] = y
        self.position["z"] = z
        self.position["tabOrder"] = tabOrder
        self.position["width"] = width
        self.position["height"] = height
        self.json["position"] = self.position


class Image(Visual):
    def __init__(self, name, paths, image_url="logo_mini5418441097720991.png"):
        super().__init__(name, "image", paths)
        self.image_url = image_url

        self.json["name"] = f"{self.name}"
        self.json["visual"]["objects"]["general"][0]["properties"]["imageUrl"]["expr"]["ResourcePackageItem"][
            "ItemName"
        ] = self.image_url
        self.json["visual"]["visualContainerObjects"]["visualLink"][0]["properties"]["show"]["expr"]["Literal"][
            "Value"
        ] = "false"


class HomeIcon(Visual):
    def __init__(self, name, paths):
        super().__init__(name, "image", paths)
        self.icon = "Home_button_logo.png"
        self.destination = "Homepage"

        self.json["name"] = f"{self.name}"
        self.json["visual"]["objects"]["general"][0]["properties"]["imageUrl"]["expr"]["ResourcePackageItem"][
            "ItemName"
        ] = self.icon

        self.json["visual"]["visualContainerObjects"]["visualLink"][0]["properties"]["type"]["expr"]["Literal"][
            "Value"
        ] = "'PageNavigation'"
        self.json["visual"]["visualContainerObjects"]["visualLink"][0]["properties"]["tooltip"]["expr"]["Literal"][
            "Value"
        ] = "'Go to Home Page'"
        self.json["visual"]["visualContainerObjects"]["title"][0]["properties"]["text"]["expr"]["Literal"][
            "Value"
        ] = "'Home'"
        self.json["visual"]["visualContainerObjects"]["visualLink"][0]["properties"]["navigationSection"]["expr"][
            "Literal"
        ]["Value"] = self.destination


class ClearFilterIcon(Visual):
    def __init__(self, name, paths):
        super().__init__(name, "image", paths)
        self.icon = "Clear_all_slicers14676744101821415.png"

        self.json["name"] = f"{self.name}"
        self.json["visual"]["objects"]["general"][0]["properties"]["imageUrl"]["expr"]["ResourcePackageItem"][
            "ItemName"
        ] = self.icon

        self.json["visual"]["visualContainerObjects"]["visualLink"][0]["properties"]["tooltip"]["expr"]["Literal"][
            "Value"
        ] = "'Clear All Slicers'"
        self.json["visual"]["visualContainerObjects"]["visualLink"][0]["properties"]["type"]["expr"]["Literal"][
            "Value"
        ] = "'ClearAllSlicers'"
        self.json["visual"]["visualContainerObjects"]["title"][0]["properties"]["text"]["expr"]["Literal"][
            "Value"
        ] = "'Filter Clear'"

        self.json["visual"]["visualContainerObjects"]["visualLink"][0]["properties"].pop("navigationSection", None)


class ReportName(Visual):
    def __init__(self, name, paths, report_title):
        super().__init__(name, "textbox", paths)
        self.report_title = report_title

        self.json["name"] = f"{self.name}"
        self.json["visual"]["objects"]["general"][0]["properties"]["paragraphs"][0]["textRuns"][0]["value"] = (
            f"'{self.report_title}'"
        )
        self.json["visual"]["objects"]["general"][0]["properties"]["paragraphs"][0]["textRuns"][0]["textStyle"][
            "color"
        ] = f"'{self.font_color}'"


class Shape(Visual):
    def __init__(self, name, paths, shape_type="rectangleRounded"):
        super().__init__(name, "shape", paths)
        self.shape_type = shape_type

        self.json["name"] = f"{self.name}"
        self.json["visual"]["objects"]["shape"][0]["properties"]["tileShape"]["expr"]["Literal"]["Value"] = (
            f"'{self.shape_type}'"
        )

        self.json["visual"]["objects"]["fill"][0]["properties"]["fillColor"]["solid"]["color"]["expr"]["Literal"][
            "Value"
        ] = f"'{self.background}'"
        self.json["visual"]["objects"]["outline"][0]["properties"]["lineColor"]["solid"]["color"]["expr"]["Literal"][
            "Value"
        ] = f"'{self.border_color}'"


class PageNavigator(Visual):
    def __init__(self, name, paths, page=None):
        super().__init__(name, "pageNavigator", paths)
        self.json["name"] = f"{self.name}"

        self.page_schema = {
            "properties": {"showPage": {"expr": {"Literal": {"Value": "true"}}}},
            "selector": {"id": ""},
        }
        self.page_schema["selector"]["id"] = f"'{self.name}'"


class ChapterButton(Visual):
    def __init__(self, name, paths, chapter_name):
        super().__init__(name, "actionButton", paths)

        self.destination = "destination_page"
        self.chapter_name = chapter_name

        self.json["name"] = f"{self.name}"
        self.json["visual"]["objects"]["text"][1]["properties"]["text"]["expr"]["Literal"]["Value"] = (
            f"'{self.chapter_name}'"
        )

        self.json["visual"]["visualContainerObjects"]["visualLink"][0]["properties"]["type"]["expr"]["Literal"][
            "Value"
        ] = "'PageNavigation'"

        self.json["visual"]["visualContainerObjects"]["visualLink"][0]["properties"]["navigationSection"]["expr"][
            "Literal"
        ]["Value"] = f"'{self.chapter_name}'"
