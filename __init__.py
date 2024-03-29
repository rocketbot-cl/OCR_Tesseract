# coding: utf-8
"""
Base para desarrollo de modulos externos.
Para obtener el modulo/Funcion que se esta llamando:
     GetParams("module")

Para obtener las variables enviadas desde formulario/comando Rocketbot:
    var = GetParams(variable)
    Las "variable" se define en forms del archivo package.json

Para modificar la variable de Rocketbot:
    SetVar(Variable_Rocketbot, "dato")

Para obtener una variable de Rocketbot:
    var = GetVar(Variable_Rocketbot)

Para obtener la Opcion seleccionada:
    opcion = GetParams("option")


Para instalar librerias se debe ingresar por terminal a la carpeta "libs"
    
    pip install <package> -t .

"""

import os
from PIL import Image

base_path = tmp_global_obj["basepath"]
cur_path = os.path.join(base_path, 'modules', 'OCR_Tesseract', 'libs')
sys.path.append(cur_path)
cur_path = os.path.join(base_path, 'modules', 'OCR_Tesseract', 'tesseract')
sys.path.append(cur_path)

import pyocr
import pyocr.tesseract
from pyocr.builders import TextBuilder
from pyocr.error import TesseractError

"""
    Obtengo el modulo que fueron invocados
"""

class Builder(TextBuilder):
    def __init__(self, **kwargs):
        psm = "3"
        if "psm" in kwargs:
            if kwargs["psm"] is not None: psm = kwargs["psm"]
            del kwargs["psm"]
        super().__init__(**kwargs)
        self.tesseract_configs = ['--oem', '3', '--psm', psm]
          
          
module = GetParams("module")

if module == "gettext":

    image = GetParams("image")
    result = GetParams("result")
    psm = GetParams("psm")

    try:
        pyocr.tesseract.TESSERACT_CMD = os.path.join(base_path,  'modules', 'OCR_Tesseract', 'Tesseract-OCR', 'tesseract.exe')
        img = Image.open(image)
        w,h = img.size
        if w<= 200 or h <= 50:
            print("Scaling...")
            factor = min(1, float(1024.0 / w))
            size = int(factor * w), int(factor * h)
            img = img.resize(size)
        # img = improve_image(image)
        tool = pyocr.get_available_tools()[0]
        lang = tool.get_available_languages()[0]
    
        text = tool.image_to_string(img,lang=lang, builder=Builder(psm=psm))

        if result:
            SetVar(result, text)

    except Exception as e:
        PrintException()
        raise e

    


