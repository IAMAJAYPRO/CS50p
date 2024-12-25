from fpdf import FPDF


def main():
    name = input("Name: ").strip()
    pdf = make_shirtificate(name)
    pdf.output("shirtificate.pdf")


def make_shirtificate(name):
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    # pdf.add_font("MonteCarlo",fname="fonts/MonteCarlo-Regular.ttf")
    pdf.set_font("Helvetica", size=48)
    pdf.set_margins(10, 10, 10)
    pdf.add_page()
    pdf.ln(20)

    pdf.cell(text="CS50 Shirtificate", center=True)
    pdf.ln(40)
    pdf.image("shirtificate.png", w=190, keep_aspect_ratio=True)
    pdf.set_font("", size=26)
    pdf.set_text_color(255, 255, 255)
    # Write text on top of the image
    pdf.cell(0, -250, f"{name} took CS50", align="C")
    pdf.rect(pdf.l_margin, pdf.t_margin, pdf.w -
             2*pdf.l_margin, pdf.h - 2*pdf.t_margin)
    return pdf

if __name__=="__main__":
    main()
