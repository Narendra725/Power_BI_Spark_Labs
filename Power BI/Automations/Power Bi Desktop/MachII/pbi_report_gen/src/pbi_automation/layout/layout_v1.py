def generate_layout_v1(canvas_w=1600, canvas_h=900, visual_pad=2):
    hdr_h = 0.15 * canvas_h
    body_h = canvas_h - hdr_h

    hdr_main_h = 0.45 * hdr_h
    hdr_sub_h = 0.45 * hdr_h
    hdr_minor_h = 0.10 * hdr_h

    hdr_main_left_w = 0.10 * canvas_w
    hdr_main_right_w = 0.90 * canvas_w

    org_logo_x = visual_pad
    org_logo_y = visual_pad
    org_logo_z = 0
    org_logo_w = hdr_main_left_w - (2 * visual_pad)
    org_logo_h = hdr_main_h - (2 * visual_pad)

    hdr_bg_x = org_logo_x + org_logo_w + visual_pad
    hdr_bg_y = visual_pad
    hdr_bg_z = 0
    hdr_bg_w = hdr_main_right_w - (2 * visual_pad)
    hdr_bg_h = hdr_main_h - (2 * visual_pad)

    report_title_w = 0.20 * hdr_bg_w
    report_title_x = hdr_bg_x + visual_pad
    report_title_y = hdr_bg_y + (0.20 * hdr_bg_h)
    report_title_z = hdr_bg_z + 1
    report_title_h = hdr_bg_h - (2 * 0.20 * hdr_bg_h)

    chapter_btn_x = report_title_x + report_title_w + visual_pad
    chapter_btn_y = hdr_bg_y + (0.20 * hdr_bg_h)
    chapter_btn_z = hdr_bg_z + 1
    chapter_btn_w = 0.80 * hdr_bg_w - (2 * visual_pad)
    chapter_btn_h = hdr_bg_h - (2 * 0.20 * hdr_bg_h)

    home_btn_size = report_title_h

    home_btn_x = chapter_btn_x + visual_pad
    home_btn_y = chapter_btn_y
    home_btn_z = chapter_btn_z + 1
    home_btn_w = home_btn_size
    home_btn_h = chapter_btn_h

    chapter_btn_space_x = home_btn_x + home_btn_w + visual_pad
    chapter_btn_space_y = chapter_btn_y
    chapter_btn_space_z = chapter_btn_z
    chapter_btn_space_w = chapter_btn_w - (home_btn_w + 2 * visual_pad)
    chapter_btn_space_h = chapter_btn_h

    sub_hdr_outline_x = visual_pad
    sub_hdr_outline_y = hdr_main_h + visual_pad
    sub_hdr_outline_z = 0
    sub_hdr_outline_w = canvas_w - (2 * visual_pad)
    sub_hdr_outline_h = hdr_sub_h - (2 * visual_pad)

    page_nav_x = sub_hdr_outline_x + visual_pad
    page_nav_y = sub_hdr_outline_y + visual_pad
    page_nav_z = sub_hdr_outline_z + 1
    page_nav_w = sub_hdr_outline_w - (2 * visual_pad)
    page_nav_h = sub_hdr_outline_h - (2 * visual_pad)

    divider_line_x = visual_pad
    divider_line_y = hdr_main_h + hdr_sub_h + visual_pad
    divider_line_z = 0
    divider_line_w = canvas_w - (2 * visual_pad)
    divider_line_h = hdr_minor_h - (2 * visual_pad)

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
