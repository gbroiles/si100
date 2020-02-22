#! /usr/bin/env python3
import datetime
import os
import sys

import PySimpleGUI as sg

def main():
    """ main event loop """

    tab1_layout = [
        [sg.T("Corporation name:"), sg.In(key="corpname")],
        [sg.T("SOS File No:"), sg.In(key="SOS_file_num")],
        [sg.Frame('Physical address', phy_addr_layout, font="Any 12", title_color='blue')],
        [sg.Frame('Mailing address', mail_addr_layout, font="Any 12", title_color='blue')],
        ]


    phy_addr_layout = [
        [sg.T("Street address:"), sg.In(key="3aAddress")],
        [sg.T("City:"), sg.In(key="3aCity")],
        [sg.T("State: CA")],
        [sg.T("ZIP:"), sg.In(key="3aZIP")],
        ]

    mail_addr_layout = [
        [sg.T("Street address:"), sg.In(key="3bAddress"), sg.Button('Copy', key='Copy_Addr')],
        [sg.T("City:"), sg.In(key="3bCity")],
        [sg.T("State:"), sg.In(key="3bState")],
        [sg.T("ZIP:"), sg.In(key="3bZIP")],
        ]

    tab2_layout = [
        [sg.Text("Corporation name:"), sg.In(key="corpname")],
        [sg.Text("Entity number:"), sg.In(key="entity_num")],
        [sg.Text("Submission comments:"), sg.Multiline(key="submission_comments", size=(45,5))]
    ]

    layout = [[sg.TabGroup([sg.Tab('Corp Info', tab1_layout), sg.Tab('Mail info', tab2_layout)])]]

    window = sg.Window(
        "California Secretary of State Form SI-100",
        layout,
        return_keyboard_events=True,
        grab_anywhere=False,
        size=(650, 200),
    )
    while True:             
        event, values = window.read()
        if event in (None, 'Cancel'):
            break

    window.close()


if __name__ == "__main__":
    main()
