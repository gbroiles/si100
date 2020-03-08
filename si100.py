#! /usr/bin/env python3
# import datetime
# import os
# import sys

import pprint
from resource import statelist
import PySimpleGUI as sg

# from uszipcode import SearchEngine, SimpleZipcode, Zipcode
import pdfrw

INPUT_PDF_PATH = "corp_si100.pdf"


def main():
    """ main event loop """
    global OUTPUT_PDF_PATH
    global INPUT_PDF_PATH

    ANNOT_KEY = "/Annots"
    ANNOT_FIELD_KEY = "/T"
    #    ANNOT_VAL_KEY = "/V"
    #    ANNOT_RECT_KEY = "/Rect"
    SUBTYPE_KEY = "/Subtype"
    WIDGET_SUBTYPE_KEY = "/Widget"

    def fill_dict(values):
        data = {}
        for key in values.keys():
            #            print(key)
            #        pprint.pprint(values)
            #        data["2EntityName"] = values["2EntityName"]
            #        data["2EntityNumber"] = values["2EntityNumber"]
            if values[key]:
                data[key] = values[key]
                print(key, "=", data[key])
        return data

    def fill_form(data_dict):
        template_pdf = pdfrw.PdfReader(INPUT_PDF_PATH)
        for page in range(len(template_pdf.pages)):
            annotations = template_pdf.pages[page][ANNOT_KEY]
            for annotation in annotations:
                if annotation[SUBTYPE_KEY] == WIDGET_SUBTYPE_KEY:
                    if annotation[ANNOT_FIELD_KEY]:
                        key = annotation[ANNOT_FIELD_KEY][1:-1]
                        if key in data_dict.keys():
                            annotation.update(
                                pdfrw.PdfDict(V="{}".format(data_dict[key]))
                            )
                            annotation.update(pdfrw.PdfDict(Ff=1))
        return template_pdf

    phy_addr_layout = [
        [sg.T("Street address:"), sg.In(key="3aAddress")],
        [
            sg.T("ZIP:"),
            sg.In(key="3aZIP", size=(11, 1), enable_events=True),
            sg.T("City:"),
            sg.In(key="3aCity"),
            sg.T("State: CA*"),
            sg.In("CA", key="3aState", visible=False),
        ],
        [sg.T("* State must be California")],
    ]

    mail_addr_layout = [
        [sg.Button("Copy from physical address", key="Copy_mail_Addr"),],
        [sg.T("Street address:"), sg.In(key="3bAddress"),],
        [
            sg.T("ZIP:"),
            sg.In(key="3bZIP", size=(11, 1)),
            sg.T("City:"),
            sg.In(key="3bCity"),
            sg.T("State:"),
            sg.Combo(statelist, key="3bState", size=(3, 1)),
        ],
    ]

    tab1_layout = [
        [sg.T("Corporation name:"), sg.In(key="corpname")],
        [sg.T("SOS File No:"), sg.In(key="SOS_file_num")],
        [sg.Frame("Physical address", phy_addr_layout)],
        [sg.Frame("Mailing address", mail_addr_layout)],
    ]

    ceo_layout = [
        [sg.Button("Copy from corporation mailing address", key="Copy_ceo_Addr")],
        [
            sg.T("First name:"),
            sg.In(key="ceo_firstname", size=(15, 1)),
            sg.T("Middle name:"),
            sg.In(key="ceo_middlename", size=(15, 1)),
        ],
        [
            sg.T("Last name:"),
            sg.In(key="ceo_lastname", size=(15, 1)),
            sg.T("Suffix:"),
            sg.In(key="ceo_suffix", size=(5, 1)),
        ],
        [sg.T("Street address:"), sg.In(key="ceo_street", size=(40, 1)),],
        [
            sg.T("City:"),
            sg.In(key="ceo_City", size=(15, 1)),
            sg.T("State:"),
            sg.Combo(statelist, key="ceo_State", size=(3, 1)),
            sg.T("ZIP:"),
            sg.In(key="ceo_ZIP", size=(10, 1)),
        ],
    ]

    secretary_layout = [
        [sg.Button("Copy from corporation mailing address", key="Copy_sec_Addr")],
        [
            sg.T("First name:"),
            sg.In(key="sec_firstname", size=(15, 1)),
            sg.T("Middle name:"),
            sg.In(key="sec_middlename", size=(15, 1)),
        ],
        [
            sg.T("Last name:"),
            sg.In(key="sec_lastname", size=(15, 1)),
            sg.T("Suffix:"),
            sg.In(key="sec_suffix", size=(5, 1)),
        ],
        [sg.T("Street address:"), sg.In(key="sec_street", size=(40, 1)),],
        [
            sg.T("City:"),
            sg.In(key="sec_City", size=(15, 1)),
            sg.T("State:"),
            sg.Combo(statelist, key="sec_State", size=(3, 1)),
            sg.T("ZIP:"),
            sg.In(key="sec_ZIP", size=(10, 1)),
        ],
    ]

    cfo_layout = [
        [sg.Button("Copy from corporation mailing address", key="Copy_cfo_Addr")],
        [
            sg.T("First name:"),
            sg.In(key="cfo_firstname", size=(15, 1)),
            sg.T("Middle name:"),
            sg.In(key="cfo_middlename", size=(15, 1)),
        ],
        [
            sg.T("Last name:"),
            sg.In(key="cfo_lastname", size=(15, 1)),
            sg.T("Suffix:"),
            sg.In(key="cfo_suffix", size=(5, 1)),
        ],
        [sg.T("Street address:"), sg.In(key="cfo_street", size=(40, 1)),],
        [
            sg.T("City:"),
            sg.In(key="cfo_City", size=(15, 1)),
            sg.T("State:"),
            sg.Combo(statelist, key="cfo_State", size=(3, 1)),
            sg.T("ZIP:"),
            sg.In(key="cfo_ZIP", size=(10, 1)),
        ],
    ]

    tab2_layout = [
        [sg.Frame("Chief Executive Officer", ceo_layout)],
        [sg.Frame("Secretary", secretary_layout)],
        [sg.Frame("Chief Financial Officer", cfo_layout)],
    ]

    tab3_layout = [
        [
            sg.Radio(
                "Agent is an individual",
                "agent1",
                key="ind_agent",
                default=True,
                enable_events=True,
            )
        ],
        [
            sg.Radio(
                "Agent is a corporation", "agent1", key="corp_agent", enable_events=True
            )
        ],
        [
            sg.T("Agent corporate name:", key="agent_corp_name_label", visible=False),
            sg.In(key="agent_corpname", visible=False),
        ],
        [
            sg.T("Agent first name:", key="ind_agent_1"),
            sg.In(key="agent_given", size=(15, 1)),
            sg.T("Agent middle name:", key="ind_agent_3"),
            sg.In(key="agent_middle", size=(15, 1)),
        ],
        [
            sg.T("Agent last name:", key="ind_agent_5"),
            sg.In(key="agent_last"),
            sg.T("Agent suffix:", key="ind_agent_7"),
            sg.In(key="agent_suffix", size=(5, 1)),
        ],
        [sg.Button("Copy from corporation physical address", key="Copy_agent_Addr")],
        [sg.T("Agent street address:"), sg.In(key="agent_Street", size=(40, 1))],
        [
            sg.T("Agent city:"),
            sg.In(key="agent_City", size=(15, 1)),
            sg.T("Agent state: CA"),
            sg.In("CA", key="agent_State", visible=False),
            sg.T("Agent ZIP:"),
            sg.In(key="agent_ZIP", size=(10, 1)),
        ],
    ]
    tab4_layout = [
        [sg.Text("Corporation name:"), sg.In(key="2EntityName")],
        [sg.Text("Entity number:"), sg.In(key="2EntityNumber", size=(12, 1))],
        [
            sg.Text("Submission comments:"),
            sg.Multiline(key="submission_comments", size=(45, 6), autoscroll=False),
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
        pprint.pprint(event)
        pprint.pprint(values)
        if event == "ind_agent":
            window.FindElement("agent_corp_name_label").update(visible=False)
            window.FindElement("agent_corpname").update(visible=False)
            window.FindElement("ind_agent_1").update(visible=True)
            window.FindElement("agent_given").update(visible=True)
            window.FindElement("ind_agent_3").update(visible=True)
            window.FindElement("agent_middle").update(visible=True)
            window.FindElement("ind_agent_5").update(visible=True)
            window.FindElement("agent_last").update(visible=True)
            window.FindElement("ind_agent_7").update(visible=True)
            window.FindElement("agent_suffix").update(visible=True)
            window.FindElement("agent_City").update(visible=True)
            window.FindElement("agent_State").update(visible=True)
            window.FindElement("agent_ZIP").update(visible=True)
        if event == "corp_agent":
            window.FindElement("agent_corp_name_label").update(visible=True)
            window.FindElement("agent_corpname").update(visible=True)
            window.FindElement("ind_agent_1").update(visible=False)
            window.FindElement("agent_given").update(visible=False)
            window.FindElement("ind_agent_3").update(visible=False)
            window.FindElement("agent_middle").update(visible=False)
            window.FindElement("ind_agent_5").update(visible=False)
            window.FindElement("agent_last").update(visible=False)
            window.FindElement("ind_agent_7").update(visible=False)
            window.FindElement("agent_suffix").update(visible=False)
            window.FindElement("agent_City").update(visible=False)
            window.FindElement("agent_State").update(visible=False)
            window.FindElement("agent_ZIP").update(visible=False)

        if event in (None, "Cancel"):
            break
        if event == "Print":
            formdata = fill_dict(values)
            fill_form(formdata)
        if event == "Save":
            formdata = fill_dict(values)
            finished_pdf = fill_form(formdata)
            output_path = sg.PopupGetFile(
                "Save as", save_as=True, file_types=(("PDF", "*.pdf"),),
            )
            #            output_path = sg.FileSaveAs()
            #            pprint.pprint(output_path)
            if output_path:
                pdfrw.PdfWriter().write(output_path, finished_pdf)
        if event == "3aZIP":
            continue
        #            potential = values['3aZIP']
        #            print(event, potential)
        #            if len(potential) == 5:
        #                with SearchEngine() as search:
        #                    zipcode = search.by_zipcode(values['3aZIP'], zipcode_type=None)
        #                window.FindElement("3aCity").update(zipcode.major_city)
        if event == "Copy_mail_Addr":
            window.FindElement("3bCity").update(values["3aCity"])
            window.FindElement("3bState").update(values["3aState"])
            window.FindElement("3bAddress").update(values["3aAddress"])
            window.FindElement("3bZIP").update(values["3aZIP"])
        if event == "Copy_ceo_Addr":
            window.FindElement("ceo_City").update(values["3bCity"])
            window.FindElement("ceo_State").update(values["3bState"])
            window.FindElement("ceo_street").update(values["3bAddress"])
            window.FindElement("ceo_ZIP").update(values["3bZIP"])
        if event == "Copy_sec_Addr":
            window.FindElement("sec_City").update(values["3bCity"])
            window.FindElement("sec_State").update(values["3bState"])
            window.FindElement("sec_street").update(values["3bAddress"])
            window.FindElement("sec_ZIP").update(values["3bZIP"])
        if event == "Copy_cfo_Addr":
            window.FindElement("cfo_City").update(values["3bCity"])
            window.FindElement("cfo_State").update(values["3bState"])
            window.FindElement("cfo_street").update(values["3bAddress"])
            window.FindElement("cfo_ZIP").update(values["3bZIP"])
        if event == "Copy_agent_Addr":
            window.FindElement("agent_City").update(values["3aCity"])
            window.FindElement("agent_State").update(values["3aState"])
            window.FindElement("agent_Street").update(values["3aAddress"])
            window.FindElement("agent_ZIP").update(values["3aZIP"])

    window.close()


if __name__ == "__main__":
    main()
