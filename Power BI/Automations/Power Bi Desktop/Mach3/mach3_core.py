import os
import json
import re
import pandas as pd
from fabric_models import Report, Page, VisualContainer, Bookmark

class FabricPage:
    def __init__(self, model, visuals):
        self.model = model
        self.visuals = visuals
    def __getattr__(self, name): return getattr(self.model, name)
    def __repr__(self): return f"<FabricPage: {self.displayName} ({len(self.visuals)} visuals)>"

class FabricReport:
    def __init__(self, report_metadata, pages_with_visuals, bookmarks):
        self.metadata = report_metadata
        self.pages = [FabricPage(p, v) for p, v in pages_with_visuals]
        self.bookmarks = bookmarks
    def get_summary(self):
        print(f"--- Fabric Report Master Summary ---")
        print(f"Pages: {len(self.pages)} | Bookmarks: {len(self.bookmarks)}")
        for page in self.pages:
            print(f"- {page.displayName} ({len(page.visuals)} visuals)")

def save_fabric_definition(report_obj, pages_list, bookmarks_list, extra_metadata, base_output_path):
    os.makedirs(base_output_path, exist_ok=True)
    with open(os.path.join(base_output_path, 'report.json'), 'w') as f:
        f.write(report_obj.model_dump_json(by_alias=True, exclude_none=True, indent=2))
    pages_base = os.path.join(base_output_path, 'pages')
    os.makedirs(pages_base, exist_ok=True)
    if 'pages.json' in extra_metadata:
        with open(os.path.join(pages_base, 'pages.json'), 'w') as f:
            json.dump(extra_metadata['pages.json'], f, indent=2)
    for page, visuals in pages_list:
        page_folder = os.path.join(pages_base, page.name)
        os.makedirs(page_folder, exist_ok=True)
        with open(os.path.join(page_folder, 'page.json'), 'w') as f:
            f.write(page.model_dump_json(by_alias=True, exclude_none=True, indent=2))
        if visuals:
            v_base = os.path.join(page_folder, 'visuals')
            for v in visuals:
                v_data = v.root
                v_folder = os.path.join(v_base, v_data.name)
                os.makedirs(v_folder, exist_ok=True)
                with open(os.path.join(v_folder, 'visual.json'), 'w') as f: f.write(v.model_dump_json(by_alias=True, exclude_none=True, indent=2))

def create_pages_from_template(template_page, chapter_names):
    new_pages_list = []
    for i, chapter in enumerate(chapter_names, start=1):
        page_data = template_page.model.model_dump(by_alias=True)
        page_suffix = f"{i:03d}"
        page_data['name'] = f"Chapter_Page_{page_suffix}"
        page_data['displayName'] = chapter
        new_page_model = Page.model_validate(page_data)
        cloned_visuals = []
        v_counter = 1
        for v in template_page.visuals:
            v_data = v.model_dump(by_alias=True)
            visual_inner = v_data.get('visual', {})
            if visual_inner and 'query' in visual_inner:
                continue
            v_data['name'] = f"Visual_{v_counter:03d}_Chp_{page_suffix}"
            cloned_visuals.append(VisualContainer.model_validate(v_data))
            v_counter += 1
        new_pages_list.append((new_page_model, cloned_visuals))
    return new_pages_list

def validate_visual_consistency(template_page, generated_page):
    print(f"--- Consistency Audit: {template_page.displayName} vs {generated_page.displayName} ---")
    expected_template_visuals = [v for v in template_page.visuals if 'query' not in (v.root.visual or {})]
    if len(expected_template_visuals) != len(generated_page.visuals):
        print(f"❌ Count Mismatch: Template expected {len(expected_template_visuals)} vs Generated {len(generated_page.visuals)}")
        return
    matches = 0
    for i, (t_v, g_v) in enumerate(zip(expected_template_visuals, generated_page.visuals)):
        t_root, g_root = t_v.root, g_v.root
        t_visual, g_visual = t_root.visual or {}, g_root.visual or {}
        pos_match = t_root.position == g_root.position
        type_match = t_visual.get('visualType') == g_visual.get('visualType')
        name_changed = t_root.name != g_root.name
        if pos_match and type_match and name_changed: matches += 1
    print(f"✅ {matches}/{len(expected_template_visuals)} visuals verified.")

class FabricBPARules:
    def __init__(self, report_instance, extra_metadata):
        self.report = report_instance
        self.metadata = extra_metadata
    def run_all_checks(self):
        results = []
        for page in self.report.pages:
            if not page.displayName[0].isupper():
                results.append(f"❌ [RULE_001]: Page '{page.displayName}' naming error.")
        print("--- BPA Audit Complete ---")
        for res in results: print(res)