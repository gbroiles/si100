#! /usr/bin/env python3
""" dumps name/value pairs for form fields in PDF """
import pdfrw

ANNOT_KEY = "/Annots"
ANNOT_FIELD_KEY = "/T"
ANNOT_VAL_KEY = "/V"
SUBTYPE_KEY = "/Subtype"
WIDGET_SUBTYPE_KEY = "/Widget"

PDF_NAME = "test.pdf"

template_pdf = pdfrw.PdfReader(PDF_NAME)
for page in range(0, len(template_pdf.pages)):
    annotations = template_pdf.pages[page][ANNOT_KEY]
    for annotation in annotations:
        if annotation[SUBTYPE_KEY] == WIDGET_SUBTYPE_KEY:
            if annotation[ANNOT_FIELD_KEY]:
                name = annotation[ANNOT_FIELD_KEY]
                print("{} ".format(name), end="")
                if annotation[ANNOT_VAL_KEY]:
                    value = annotation[ANNOT_VAL_KEY]
                    print("= {}".format(value))
                else:
                    print()
