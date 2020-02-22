#! /usr/bin/env python3
import datetime
import os
import sys

import PySimpleGUI as sg
import pdfrw

output_pdf_path = "test.pdf"


def main():
    """ main event loop """
    global output_pdf_path

    ANNOT_KEY = "/Annots"
    ANNOT_FIELD_KEY = "/T"
    ANNOT_VAL_KEY = "/V"
    ANNOT_RECT_KEY = "/Rect"
    SUBTYPE_KEY = "/Subtype"
    WIDGET_SUBTYPE_KEY = "/Widget"

    def fill_dict():
        data = {}
        data["2EntityName"] = window["corpname2"]
        data["2EntityNumber"] = window["entity_num"]
        return data

    def fill_form(data_dict):
        template_pdf = pdfrw.PdfReader("corp_so100.pdf")
        annotations = template_pdf.pages[0][ANNOT_KEY]
        for annotation in annotations:
            if annotation[SUBTYPE_KEY] == WIDGET_SUBTYPE_KEY:
                if annotation[ANNOT_FIELD_KEY]:
                    key = annotation[ANNOT_FIELD_KEY][1:-1]
                    if key in data_dict.keys():
                        annotation.update(pdfrw.PdfDict(V="{}".format(data_dict[key])))
        return template_pdf

    phy_addr_layout = [
        [sg.T("Street address:"), sg.In(key="3aAddress")],
        [sg.T("City:"), sg.In(key="3aCity")],
        [sg.T("State: CA")],
        [sg.T("ZIP:"), sg.In(key="3aZIP")],
    ]

    mail_addr_layout = [
        [
            sg.T("Street address:"),
            sg.In(key="3bAddress"),
            sg.Button("Copy", key="Copy_Addr"),
        ],
        [sg.T("City:"), sg.In(key="3bCity")],
        [sg.T("State:"), sg.In(key="3bState")],
        [sg.T("ZIP:"), sg.In(key="3bZIP")],
    ]

    tab1_layout = [
        [sg.T("Corporation name:"), sg.In(key="corpname")],
        [sg.T("SOS File No:"), sg.In(key="SOS_file_num")],
        [sg.Frame("Physical address", phy_addr_layout)],
        [sg.Frame("Mailing address", mail_addr_layout)],
    ]

    ceo_layout = []

    secretary_layout = []

    cfo_layout = []

    tab2_layout = [
        [sg.Frame("Chief Executive Officer", ceo_layout)],
        [sg.Frame("Secretary", secretary_layout)],
        [sg.Frame("Chief Financial Officer", cfo_layout)],
    ]

    tab3_layout = [
        [sg.Radio("Agent is an individual", "agent1", default=True)],
        [sg.Radio("Agent is a corporation", "agent1")],
        [sg.T("Agent first name:"), sg.In(key="agent_given")],
        [sg.T("Agent middle name:"), sg.In(key="agent_middle")],
        [sg.T("Agent last name:"), sg.In(key="agent_last")],
        [sg.T("Agent suffix:"), sg.In(key="agent_suffix")],
        [sg.T("Agent street address:"), sg.In(key="agent_street")],
        [sg.T("Agent city:"), sg.In(key="agent_city")],
        [sg.T("Agent state: CA")],
        [sg.T("Agent ZIP:"), sg.In(key="agent_zip")],
    ]
    tab4_layout = [
        [sg.Text("Corporation name:"), sg.In(key="corpname2")],
        [sg.Text("Entity number:"), sg.In(key="entity_num")],
        [
            sg.Text("Submission comments:"),
            sg.Multiline(key="submission_comments", size=(45, 5)),
        ],
    ]

    layout = [
        [
            sg.TabGroup(
                [
                    [
                        sg.Tab("Corp Info", tab1_layout),
                        sg.Tab("Officer info", tab2_layout),
                        sg.Tab("Service of Process", tab3_layout),
                        sg.Tab("Mail info", tab4_layout),
                    ]
                ]
            )
        ],
        [sg.Button("Clear"), sg.Button("Print"), sg.Button("Save")],
    ]

    window = sg.Window(
        "California Secretary of State Form SI-100",
        layout,
        return_keyboard_events=True,
        grab_anywhere=False,
        #        size=(650, 200),
    )

    while True:
        event, values = window.read()
        if event in (None, "Cancel"):
            break
        if event == "Print":
            formdata = fill_dict()
            fill_form(formdata)
        if event == "Save":
            formdata = fill_dict()
            finished_pdf = fill_form(formdata)
            pdfrw.PdfWriter().write(output_pdf_path, finished_pdf)

    window.close()


if __name__ == "__main__":
    main()
