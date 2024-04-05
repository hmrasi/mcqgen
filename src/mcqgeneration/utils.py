import os
import PyPDF2
import json
import traceback

def read_file(file):
    if file.name.endswith(".pdf"):
        try:
            pdf_reader = PyPDF2.PdfFileReader(file)
            text=""
            for page in pdf_reader.pages:
                text+=page.extract_text()
            return text
        except Exception as E:
            raise Exception("Invalid pdf file")
        
    elif file.name.endswith(".txt"):
        return file.read().decode("utf-8")
    
    else:
        raise Exception("Unsupported file extension")
    

def get_table_data(quiz):
    try:
        quiz_dict = json.loads(quiz)
        quiz_table_data = []

        for key,val in quiz_dict.items():
            mcq= val["mcq"]
            options="|| ".join(
                [
                    f"{option} -> {option_value}" for option, option_value in val["options"].items()
                ]
            )

            correct_value = val["correct"]
            quiz_table_data.append({"MCQ": mcq, "Choices": options, "Correct": correct_value})

        return quiz_table_data
    
    except Exception as E:
        traceback.print_exception(type(E), E, E.__traceback__)
        return False
