from fpdf import FPDF

def main():
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    name = input("Name: ")
    pdf.add_page()
    pdf.image("shirtificate.png", y=70,w=pdf.epw)
    pdf.set_font("helvetica", "", 48)
    pdf.text(42, 43.5,"CS50 Shirtificate")
    pdf.set_text_color(255, 255, 255)
    pdf.set_font("helvetica", "", 25)
    pdf.text(55.5, 140, f"{name} took CS50")
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()