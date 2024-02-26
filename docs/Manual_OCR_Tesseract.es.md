# OCR Offline Tesseract
  
Módulo para extraer texto de una imagen  

*Read this in other languages: [English](Manual_OCR_Tesseract.md), [Português](Manual_OCR_Tesseract.pr.md), [Español](Manual_OCR_Tesseract.es.md)*
  
![banner](imgs/Banner_OCR_Tesseract.png)
## Como instalar este módulo
  
Para instalar el módulo en Rocketbot Studio, se puede hacer de dos formas:
1. Manual: __Descargar__ el archivo .zip y descomprimirlo en la carpeta modules. El nombre de la carpeta debe ser el mismo al del módulo y dentro debe tener los siguientes archivos y carpetas: \__init__.py, package.json, docs, example y libs. Si tiene abierta la aplicación, refresca el navegador para poder utilizar el nuevo modulo.
2. Automática: Al ingresar a Rocketbot Studio sobre el margen derecho encontrara la sección de **Addons**, seleccionar **Install Mods**, buscar el modulo deseado y presionar install.  

## Modos de segmentación de página (psm)
  0    Orientation and script detection (OSD) only.
  1    Automatic page segmentation with OSD.
  2    Automatic page segmentation, but no OSD, or OCR. (not implemented)
  3    Fully automatic page segmentation, but no OSD. (Default)
  4    Assume a single column of text of variable sizes.
  5    Assume a single uniform block of vertically aligned text.
  6    Assume a single uniform block of text.
  7    Treat the image as a single text line.
  8    Treat the image as a single word.
  9    Treat the image as a single word in a circle.
 10    Treat the image as a single character.
 11    Sparse text. Find as much text as possible in no particular order.
 12    Sparse text with OSD.
 13    Raw line. Treat the image as a single text line,
       bypassing hacks that are Tesseract-specific.


## Descripción de los comandos

### Convertir imagen a texto
  
Extrae texto de una imagen
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Imagen ||Image.jpg|
|Modo de segmentación de página (psm)||3|
|Asignar rsultado a variable||Variable|

### Obtener cajas de caracteres
  
Obtiene las cajas de caracteres de una imagen
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Imagen ||Image.jpg|
|Asignar rsultado a variable||Variable|
