import json
import os

def read_json(file_path):
    try:
         with open(file_path,"r") as file:
            data = json.load(file)
         return data
    except Exception as e:
         print(f"error reading json {file_path}")

def create_folder(folder_path):
   
    try:
        os.makedirs(folder_path, exist_ok=True)  # Create the directory if it doesn't exist
        # print(GREEN + f"Folder creation successful: {folder_path.split('\\')[-1]}"+RESET)
    except Exception as e:
        print(f" Couldn't create the Folder{folder_path} due to the following error: {e}")

def create_or_replace_file(file_path,data):
    if not os.path.exists(os.path.dirname(file_path)):
        create_folder(os.path.dirname(file_path))
    try:
         with open(file_path ,"w") as file :
            json.dump(data,file,indent=2)
        #  print(GREEN+fr"successfully updated file {file_path.split('\\')[-1]}"+RESET)
    except Exception as e:
        print(f"An error occured while updating the file {file_path} due to the following error: {e}")


def create_object(self, cls, *args, **kwargs):
    obj = cls(*args, **kwargs)   # instantiate the class
    return obj

def generate_layout_v1(canvas_w=1600, canvas_h=900, visual_pad=2):
    # ------------------------------
    # Header allocation
    # ------------------------------
    hdr_h = 0.15 * canvas_h
    body_h = canvas_h - hdr_h

    # Header partitions
    hdr_main_h = 0.45 * hdr_h
    hdr_sub_h = 0.45 * hdr_h
    hdr_minor_h = 0.10 * hdr_h

    # ------------------------------
    # Main header width partitions
    # ------------------------------
    hdr_main_left_w = 0.10 * canvas_w
    hdr_main_right_w = 0.90 * canvas_w

    # ------------------------------
    # org_logo visual (left block)
    # ------------------------------
    org_logo_x = visual_pad
    org_logo_y = visual_pad
    org_logo_z = 0
    org_logo_w = hdr_main_left_w - (2 * visual_pad)
    org_logo_h = hdr_main_h - (2 * visual_pad)

    # ------------------------------
    # header_background_shape (right block)
    # ------------------------------
    hdr_bg_x = org_logo_x + org_logo_w + visual_pad
    hdr_bg_y = visual_pad
    hdr_bg_z = 0
    hdr_bg_w = hdr_main_right_w - (2 * visual_pad)
    hdr_bg_h = hdr_main_h - (2 * visual_pad)

    # ------------------------------
    # report_title (20% width of header_background)
    # ------------------------------
    report_title_w = 0.20 * hdr_bg_w
    report_title_x = hdr_bg_x + visual_pad
    report_title_y = hdr_bg_y + (0.20 * hdr_bg_h)
    report_title_z = hdr_bg_z + 1
    report_title_h = hdr_bg_h - (2 * 0.20 * hdr_bg_h)

    # ------------------------------
    # chapter_buttons (remaining 80% width)
    # ------------------------------
    chapter_btn_x = report_title_x + report_title_w + visual_pad
    chapter_btn_y = hdr_bg_y + (0.20 * hdr_bg_h)
    chapter_btn_z = hdr_bg_z + 1
    chapter_btn_w = 0.80 * hdr_bg_w - (2 * visual_pad)
    chapter_btn_h = hdr_bg_h - (2 * 0.20 * hdr_bg_h)

    # ------------------------------
    # home_button (square; width = height of report_title)
    # ------------------------------
    home_btn_size = report_title_h

    home_btn_x = chapter_btn_x + visual_pad
    home_btn_y = chapter_btn_y
    home_btn_z = chapter_btn_z + 1
    home_btn_w = home_btn_size
    home_btn_h = chapter_btn_h

    # ------------------------------
    # remaining space for chapter buttons
    # ------------------------------
    chapter_btn_space_x = home_btn_x + home_btn_w + visual_pad
    chapter_btn_space_y = chapter_btn_y
    chapter_btn_space_z = chapter_btn_z
    chapter_btn_space_w = chapter_btn_w - (home_btn_w + 2 * visual_pad)
    chapter_btn_space_h = chapter_btn_h

    # ------------------------------
    # sub_header_outline (second header row)
    # ------------------------------
    sub_hdr_outline_x = visual_pad
    sub_hdr_outline_y = hdr_main_h + visual_pad
    sub_hdr_outline_z = 0
    sub_hdr_outline_w = canvas_w - (2 * visual_pad)
    sub_hdr_outline_h = hdr_sub_h - (2 * visual_pad)

    # ------------------------------
    # page_navigator (inside sub_header_outline)
    # ------------------------------
    page_nav_x = sub_hdr_outline_x + visual_pad
    page_nav_y = sub_hdr_outline_y + visual_pad
    page_nav_z = sub_hdr_outline_z + 1
    page_nav_w = sub_hdr_outline_w - (2 * visual_pad)
    page_nav_h = sub_hdr_outline_h - (2 * visual_pad)

    # ------------------------------
    # divider_line (third header row)
    # ------------------------------
    divider_line_x = visual_pad
    divider_line_y = hdr_main_h + hdr_sub_h + visual_pad
    divider_line_z = 0
    divider_line_w = canvas_w - (2 * visual_pad)
    divider_line_h = hdr_minor_h - (2 * visual_pad)

    # ------------------------------
    # Return visual-centric layout
    # ------------------------------
    return {
        "meta": {
            "layout_version": "1.0",
            "description": "Visual-centric layout for Power BI style page header."
        },
        "canvas": {
            "width": canvas_w,
            "height": canvas_h,
            "padding": visual_pad
        },
        "visuals": [
            {
                "id": "org_logo",
                "type": "image",
                "section": "header_main_left",
                "x": org_logo_x, "y": org_logo_y, "z": org_logo_z,
                "w": org_logo_w, "h": org_logo_h
            },
            {
                "id": "header_background_shape",
                "type": "shape",
                "section": "header_main_right",
                "x": hdr_bg_x, "y": hdr_bg_y, "z": hdr_bg_z,
                "w": hdr_bg_w, "h": hdr_bg_h
            },
            {
                "id": "report_title",
                "type": "text",
                "section": "header_main_right",
                "base_visual": "header_background_shape",
                "x": report_title_x, "y": report_title_y, "z": report_title_z,
                "w": report_title_w, "h": report_title_h
            },
            {
                "id": "chapter_buttons",
                "type": "container",
                "section": "header_main_right",
                "base_visual": "header_background_shape",
                "x": chapter_btn_x, "y": chapter_btn_y, "z": chapter_btn_z,
                "w": chapter_btn_w, "h": chapter_btn_h
            },
            {
                "id": "home_button",
                "type": "button",
                "section": "header_main_right",
                "parent": "chapter_buttons",
                "x": home_btn_x, "y": home_btn_y, "z": home_btn_z,
                "w": home_btn_w, "h": home_btn_h
            },
            {
                "id": "chapter_button_space",
                "type": "container",
                "section": "header_main_right",
                "parent": "chapter_buttons",
                "x": chapter_btn_space_x, "y": chapter_btn_space_y, "z": chapter_btn_space_z,
                "w": chapter_btn_space_w, "h": chapter_btn_space_h
            },
            {
                "id": "sub_header_outline",
                "type": "shape",
                "section": "header_sub",
                "x": sub_hdr_outline_x, "y": sub_hdr_outline_y, "z": sub_hdr_outline_z,
                "w": sub_hdr_outline_w, "h": sub_hdr_outline_h
            },
            {
                "id": "page_navigator",
                "type": "navigation",
                "section": "header_sub",
                "base_visual": "sub_header_outline",
                "x": page_nav_x, "y": page_nav_y, "z": page_nav_z,
                "w": page_nav_w, "h": page_nav_h
            },
            {
                "id": "divider_line",
                "type": "line",
                "section": "header_minor",
                "x": divider_line_x, "y": divider_line_y, "z": divider_line_z,
                "w": divider_line_w, "h": divider_line_h
            }
        ]
    }


class Obj_Register :
    def __init__(self):
        self.objects = []
        self.obj_names = []
    
    def register_object(self,obj):
        self.objects.append(obj)
        self.obj_names.append(obj.name)

obj_reg = Obj_Register()

        
class Visual:
    def __init__(self, name, vtype):
        
        self.name = name 
        self.type = vtype
        self.file_path = f"C:\\Nahdi-articrafts\\REPORT_AUTOMATION\\base_articrafts\\report_page_jsons\\visuals\\{self.type}\\visual.json"

        self.position = {
            "x": None,
            "y": None,
            "z": None,
            "tabOrder": None,
            "width": None,
            "height": None
        }
        
        self.groups = []
        self.bookmark = []
        self.background = "#FFFFFF"
        self.border_color = "#000000"
        self.font_color = "#000000"
        self.page = ""
        self.json = read_json(self.file_path)
        self.json['name'] = self.name
        self.json['position'] = self.position
        obj_reg.register_object(self)
        
    def add_to_group(self,grp_name):
        self.groups.append(grp_name)
    
    def add_to_bookmark(self,bookmark_name):
        self.bookmark.append(bookmark_name)
    
    def add_to_page(self,page_name):
        self.page = page_name
    
    def set_position(self, x, y, z, tabOrder, width, height):
        self.position['x'] = x
        self.position['y'] = y
        self.position['z'] = z
        self.position['tabOrder'] = tabOrder
        self.position['width'] = width
        self.position['height'] = height
        self.json['position'] = self.position
        
class Image(Visual):
    def __init__(self, name, image_url ="logo_mini5418441097720991.png"):
        super().__init__(name, 'image')
        self.image_url = image_url
        self.json['name'] = ""+self.name
        self.json['visual']['objects']['general'][0]['properties']['imageUrl']['expr']['ResourcePackageItem']['ItemName'] = self.image_url
        self.json['visual']['visualContainerObjects']['visualLink'][0]['properties']['show']['expr']['Literal']['Value'] = "false"

        
        
            
class Home_Icon(Visual):
    ## validation done
    def __init__(self, name):
        super().__init__(name, 'image')
        self.icon = "Home_button_logo.png"
        self.destination = "Homepage"
        self.json['name'] = ""+self.name
        self.json['visual']['objects']['general'][0]['properties']['imageUrl']['expr']['ResourcePackageItem']['ItemName'] = self.icon
        self.json['visual']['visualContainerObjects']['visualLink'][0]['properties']['type']['expr']['Literal']['Value'] = f"'{str("PageNavigation")}'"
        self.json['visual']['visualContainerObjects']['visualLink'][0]['properties']['tooltip']['expr']['Literal']['Value'] = f"'{str("Go to Home Page")}'"
        self.json['visual']['visualContainerObjects']['title'][0]['properties']['text']['expr']['Literal']['Value'] = f"'{str("Home")}'"
        self.json['visual']['visualContainerObjects']['visualLink'][0]['properties']['navigationSection']['expr']['Literal']['Value'] = self.destination

class Clear_Filter_Icon(Visual):
    ## validation done
    def __init__(self, name):
        super().__init__(name, 'image')
        self.icon = "Clear_all_slicers14676744101821415.png"
        self.json['name'] = f"{self.name}"
        self.json['visual']['objects']['general'][0]['properties']['imageUrl']['expr']['ResourcePackageItem']['ItemName'] = f"'{self.icon}'"
        self.json['visual']['visualContainerObjects']['visualLink'][0]['properties']['tooltip']['expr']['Literal']['Value'] = f"'{str("Clear All Slicers")}'"
        self.json['visual']['visualContainerObjects']['visualLink'][0]['properties']['type']['expr']['Literal']['Value'] = f"'{str('ClearAllSlicers')}'"
        self.json['visual']['visualContainerObjects']['title'][0]['properties']['text']['expr']['Literal']['Value'] = f"'{str('Filter Clear')}'"
        self.json['visual']['visualContainerObjects']['visualLink'][0]['properties'].pop('navigationSection', None)

class Report_Name(Visual):
    ## Validation done
    def __init__(self, name, report_title):
        super().__init__(name, "textbox")
        self.report_title = report_title
        self.json['name'] = f"{self.name}"
        self.json['visual']['objects']['general'][0]['properties']['paragraphs'][0]['textRuns'][0]['value'] = f"'{self.report_title}'"
        self.json['visual']['objects']['general'][0]['properties']['paragraphs'][0]['textRuns'][0]['textStyle']['color'] = f"'{self.font_color}'"

class Shape(Visual):
    ## Validation done
    def __init__(self, name, shape_type = "rectangleRounded"):
        super().__init__(name, "shape")
        self.shape_type = shape_type
        # self.round_edges = "8L"
        self.json['name'] = f"{self.name}"
        self.json['visual']['objects']['shape'][0]['properties']['tileShape']['expr']['Literal']['Value'] = f"'{self.shape_type}'"
        # self.json['visual']['objects']['shape'][0]['properties']['rectangleRoundedCurve']['expr']['Literal']['Value'] = f"'{self.round_edges}'"
        self.json['visual']['objects']['fill'][0]['properties']['fillColor']['solid']['color']['expr']['Literal']['Value'] = f"'{self.background}'"
        self.json['visual']['objects']['outline'][0]['properties']['lineColor']['solid']['color']['expr']['Literal']['Value'] = f"'{self.border_color}'"


class Page_Navigator(Visual):
    ## Validation Done
    def __init__(self, name,page = None):
        super().__init__(name, "pageNavigator")
        self.json['name'] = f"{self.name}"
        self.page_schema = {
          "properties": {
            "showPage": {
              "expr": {
                "Literal": {
                  "Value": "true"
                }
              }
            }
          },
          "selector": {
            "id": ""
          }
        }
        self.page_schema["selector"]["id"]= f"'{self.name}'"
    
            

class Chapter_Button(Visual):
    def __init__(self, name, chapter_name):
        super().__init__(name, "actionButton")
        self.destination = 'destination_page'
        self.chapter_name = chapter_name
        self.json['name'] = f"'{self.name}'"
        self.json['visual']['objects']['text'][1]['properties']['text']['expr']['Literal']['Value'] = f"'{self.chapter_name}'"
        self.json['visual']['visualContainerObjects']['visualLink'][0]['properties']['type']['expr']['Literal']['Value'] = f"'{str("PageNavigation")}'"
        self.json['visual']['visualContainerObjects']['visualLink'][0]['properties']['navigationSection']['expr']['Literal']['Value'] = f"'{self.chapter_name}'"
    
class Report:
    def __init__(self, name,height = 720 , width = 1024):
        self.name = name
        self.height = height
        self.width = width
        self.folder = "C:\\Nahdi-articrafts\\REPORT_AUTOMATION\\NewReport.Report\\definition"
        self.pages = []
        self.bookmarks_json = read_json(f"C:\\Nahdi-articrafts\\REPORT_AUTOMATION\\base_articrafts\\report_page_jsons\\bookmarks\\bookmarks.json")
        self.version_json = read_json(f"C:\\Nahdi-articrafts\\REPORT_AUTOMATION\\base_articrafts\\version.json")
        self.pages_json = read_json(f"C:\\Nahdi-articrafts\\REPORT_AUTOMATION\\base_articrafts\\pages.json")
        self.file_path = f"C:\\Nahdi-articrafts\\REPORT_AUTOMATION\\base_articrafts\\report.json"
        self.json= read_json(self.file_path)
        self.bookmarks =[]
        obj_reg.register_object(self)
    
    def add_page(self, page_name,dis_name=None,chapter = None,is_home = False):
        page_obj = Page(name=page_name,display_name=dis_name,chapter=chapter,is_home=is_home)
        page_obj.width = self.width
        page_obj.height = self.height
        self.pages.append(page_obj)
        self.pages_json['activePageName'] = self.pages[0].name
        page_obj.report = self
        self.pages_json["pageOrder"].extend([page_obj.name])
        if page_obj.is_home == True:
            self.pages_json["activePageName"] = page_obj.name
    
    def save_report(self):
        create_folder(self.folder)
        # create_folder(f"{self.folder}\\bookmarks")
        create_folder(f"{self.folder}\\pages")
        create_or_replace_file(f"{self.folder}\\version.json", self.version_json)
        create_or_replace_file(f"{self.folder}\\report.json", self.json)
        create_or_replace_file(f"{self.folder}\\pages\\pages.json", self.pages_json)
        for page in self.pages:
            create_or_replace_file(f"{self.folder}\\pages\\{page.name}\\page.json", page.json)
            for visual in page.visuals:
                create_or_replace_file(f"{self.folder}\\pages\\{page.name}\\visuals\\{visual.name}\\visual.json", visual.json)
        

class Group:
    def __init__(self,name,page,display_name = None):
        
        self.name = name 
        self.position = {
            "x": None,
            "y": None,
            "z": None,
            "height": None,
            "width": None
        },
        if display_name is None:
            self.display_name = name
        else :
            self.display_name = display_name
        self.visuals = []
        self.file_path = f"C:\\Nahdi-articrafts\\REPORT_AUTOMATION\\base_articrafts\\report_page_jsons\\VisualGroup\\visual.json"
        self.json = read_json(self.file_path)    
        self.json['name'] = self.name
        self.json['visualGroup']['displayName'] = self.display_name   
        self.page = page
        obj_reg.register_object(self)

    def add_visual(self,visual, *args, **kwargs):
        visual = create_object(None,visual, *args, **kwargs)
        self.visuals.append(visual)
        self.page.add_visual(visual)
        self.visual.json['parentGroupName']= self.name

class Page:
    def __init__(self, name ,display_name = None,chapter = None,is_home = False,width =1024, height = 720):
        
        self.report = None
        self.is_home = is_home
        self.width = width
        self.height = height
        self.name = name
        if display_name is None:
            self.display_name = name
        else :
            self.display_name = display_name
        self.verticalAlignment = "Middle"
        self.background= {"Literal": {"Value": "#FFFFFF"} } ##or {"ThemeDataColor": {"ColorId": 0,"Percent": 0} } for theme color 
        self.file_path = f"C:\\Nahdi-articrafts\\REPORT_AUTOMATION\\base_articrafts\\report_page_jsons\\page.json"
        self.json = read_json(self.file_path)
        self.json['name'] = self.name
        self.json['displayName']= self.display_name
        self.json['height'] = self.height
        self.json['width'] = self.width
        self.chapter = chapter
        self.visuals =[]
        self.bookmarks = [] 
        obj_reg.register_object(self)
    
    def add_group(self,grp_name,display_name = None):
        group_obj = Group(grp_name,self,display_name)
        self.visuals.append(group_obj)
        group_obj.page = self
        
    def add_page_navigator(self,navigator_name):
        navigator = Page_Navigator(navigator_name,self.name)
        self.visuals.append(navigator)
        navigator.main_page = self.name
    
    def link_to_report(self,report):
        self.report = report
    
    def add_visual(self,visual):
        self.visuals.append(visual)

    def add_bookmark(self,bookmark):
        bookmark_obj = create_object(None,bookmark,bookmark)

class Bookmark:
    def __init__(self, name,page,display_name = None):
        
        self.name = name
        self.page = page
        if display_name is None:
            self.display_name = name
        else:
            self.display_name = display_name
        self.file_path = f"C:\\Nahdi-articrafts\\REPORT_AUTOMATION\\base_articrafts\\report_page_jsons\\bookmarks\\bookmarkname.bookmark.json"
        self.json = read_json(self.file_path)
        self.json['name'] = f"'{self.name}'"
        self.json['displayName'] = f"'{self.display_name}'"
        self.json['selector']['id']= f"'{self.name}'"
        self.json['explorationState']['activeSection'] = f"'{self.page.name}'"
        self.visuals=[]
        obj_reg.register_object(self)
    
    def add_visual(self,Visual):
        self.visuals.append(Visual)
        self.json['options']['targetVisualNames'].append(f"'{Visual.name}'")
        self.json['explorationState']['sections'][self.page.name]['visualContainers'][Visual.name]['singleVisual']['visualType'] = Visual.type
        self.json['explorationState']['sections'][self.page.name]['visualContainers'][Visual.name]['singleVisual']['objects'] = {}
    

