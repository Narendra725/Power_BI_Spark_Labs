from pbi_automation.io.file_ops import read_json, create_folder, create_or_replace_file
from pbi_automation.core.registry import obj_reg
from pbi_automation.core.page import Page


class Report:
    def __init__(self, name, paths, height=720, width=1024):
        self.paths = paths
        self.name = name
        self.height = height
        self.width = width

        self.folder = str(self.paths.output_definition)

        self.pages = []

        self.bookmarks_json = read_json(str(self.paths.base_bookmarks_json))
        self.version_json = read_json(str(self.paths.base_version_json))
        self.pages_json = read_json(str(self.paths.base_pages_json))
        self.file_path = str(self.paths.base_report_json)
        self.json = read_json(self.file_path)

        self.bookmarks = []
        obj_reg.register_object(self)

    def add_page(self, page_name, dis_name=None, chapter=None, is_home=False):
        page_obj = Page(
            name=page_name,
            paths=self.paths,
            display_name=dis_name,
            chapter=chapter,
            is_home=is_home,
            width=self.width,
            height=self.height,
        )

        self.pages.append(page_obj)

        self.pages_json["activePageName"] = self.pages[0].name
        page_obj.report = self
        self.pages_json["pageOrder"].extend([page_obj.name])

        if page_obj.is_home:
            self.pages_json["activePageName"] = page_obj.name

        return page_obj

    def save_report(self):
        create_folder(self.folder)
        create_folder(f"{self.folder}/pages")

        create_or_replace_file(f"{self.folder}/version.json", self.version_json)
        create_or_replace_file(f"{self.folder}/report.json", self.json)
        create_or_replace_file(f"{self.folder}/pages/pages.json", self.pages_json)

        for page in self.pages:
            create_or_replace_file(f"{self.folder}/pages/{page.name}/page.json", page.json)
            for visual in page.visuals:
                create_or_replace_file(
                    f"{self.folder}/pages/{page.name}/visuals/{visual.name}/visual.json",
                    visual.json,
                )
