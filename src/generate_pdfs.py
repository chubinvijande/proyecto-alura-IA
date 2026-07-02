from pathlib import Path 
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

KNOWLEDGE_PATH = Path("knowledge_base")
DATA_PATH = Path("data")
OUTPUT_PATH = Path("data")


def generate_pdfs():
    styles = getSampleStyleSheet()
    title_style = styles["Heading1"]
    normal_style = styles["BodyText"]

    for md_file in KNOWLEDGE_PATH.rglob("*.md"):

        with open(md_file, "r", encoding="utf-8") as file :
            content = file.readlines()
        story = []
    
        for line in content:


                line = line.strip()

                if not line:
                        continue
                    

                if line.startswith("# "):

                    title = line.replace("# ", "")
                    story.append(
                          Paragraph(title, title_style)
                )

                else:

                    story.append(
                    Paragraph(line, normal_style)
                )
                

        relative_path = md_file.relative_to(KNOWLEDGE_PATH)

        pdf_path = OUTPUT_PATH / relative_path.with_suffix(".pdf")

        pdf_path.parent.mkdir(parents=True, exist_ok=True)
        doc = SimpleDocTemplate(str(pdf_path))

        for elemento in story:
            print(type(elemento))

            doc.build(story)

            print(f"PDF generado: {pdf_path}")


if __name__ == "__main__":

    generate_pdfs()

