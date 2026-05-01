from pdf2docx import Converter
import tempfile
import os

def handler(request):
    try:
        # Get file
        file = request.files.get("file")

        if not file:
            return {
                "statusCode": 400,
                "body": "No file uploaded"
            }

        # Temporary paths
        pdf_path = tempfile.mktemp(suffix=".pdf")
        docx_path = tempfile.mktemp(suffix=".docx")

        # Save PDF
        with open(pdf_path, "wb") as f:
            f.write(file.read())

        # Convert PDF → DOCX
        cv = Converter(pdf_path)
        cv.convert(docx_path)
        cv.close()

        # Return file
        with open(docx_path, "rb") as f:
            file_data = f.read()

        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
            },
            "body": file_data
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": str(e)
        }
