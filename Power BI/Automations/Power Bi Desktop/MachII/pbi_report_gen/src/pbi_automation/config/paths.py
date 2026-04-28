from dataclasses import dataclass
from pathlib import Path


@dataclass
class ProjectPaths:
    base_artifacts: Path
    output_definition: Path

    def resolve_visual_template(self, visual_type: str) -> Path:
        return self.base_artifacts / "report_page_jsons" / "visuals" / visual_type / "visual.json"

    @property
    def base_report_json(self) -> Path:
        return self.base_artifacts / "report.json"

    @property
    def base_pages_json(self) -> Path:
        return self.base_artifacts / "pages.json"

    @property
    def base_version_json(self) -> Path:
        return self.base_artifacts / "version.json"

    @property
    def base_bookmarks_json(self) -> Path:
        return self.base_artifacts / "report_page_jsons" / "bookmarks" / "bookmarks.json"

    @property
    def base_page_json(self) -> Path:
        return self.base_artifacts / "report_page_jsons" / "page.json"

    @property
    def base_group_json(self) -> Path:
        return self.base_artifacts / "report_page_jsons" / "VisualGroup" / "visual.json"

    @property
    def base_bookmark_template(self) -> Path:
        return self.base_artifacts / "report_page_jsons" / "bookmarks" / "bookmarkname.bookmark.json"
