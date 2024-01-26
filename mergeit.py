import PyPDF2
from PyPDF2 import Transformation,PdfWriter
from PyPDF2.generic import RectangleObject

import sys
pdf_file = sys.argv[1]
watermark = sys.argv[2]
merged_pdf = sys.argv[3]
with open(pdf_file,'rb') as input_file:
    input_pdf = PyPDF2.PdfReader(input_file)
    pdf_page = input_pdf.pages[0]
    with open(watermark,'rb') as watermark_file:
        watermark_pdf = PyPDF2.PdfReader(watermark_file)
        watermark_page = watermark_pdf.pages[0]


        # Scale and translate
        op = Transformation().scale(sx=1.5, sy=1.5).translate(-155,-85)
        pdf_page.add_transformation(op)

        # add watermark
        pdf_page.merge_page(watermark_page)
        rot = Transformation().rotate(90.0)
        pdf_page.add_transformation(rot)
        # pdf_page.mediabox.upper_right = (pdf_page.mediabox.right*2,pdf_page.mediabox.top*2)

        pdf_page.cropbox = RectangleObject([-290, 40, 0,470])
        pdf_page.mediabox = RectangleObject([-290, 40, 0,470])

        output = PyPDF2.PdfWriter()
        output.add_page(pdf_page)

        with open(merged_pdf,'wb') as output_file:
            output.write(output_file)
