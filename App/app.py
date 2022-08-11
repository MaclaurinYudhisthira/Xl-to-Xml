# Set-ExecutionPolicy Unrestricted -Scope Process
# env\Scripts\activate
# python app.py

# Importing the modules required
import pandas as pd
import eel

eel.init('web')

@eel.expose
def convert(input_file_path,output_file_path,operation_name):
    print(f"Converting {input_file_path} ...")
    # Reading the file 
    df=pd.read_excel(input_file_path)
    fields=df.columns

    # Convrsion to xml
    output_string='<?xml version="1.0" encoding="UTF-8"?>\n<data>'
    for index, operation in df.iterrows():
        output_string+=f'\n\t<operation name="{operation_name+str(index)}">'
        for field in fields:
            output_string+=f'\n\t\t<fields>\n\t\t\t<label>{field}</label>\n\t\t\t<value>{operation[field]}</value>\n\t\t</fields>'
        output_string+='\n\t</operation>'
    output_string+='\n</data>\n'

    # Exporting to file
    f = open(output_file_path, "w")
    f.write(output_string)
    f.close()

    print("Done!!!")
    return 0

eel.start('index.html',size=(1000,600))