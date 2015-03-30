CFDiVigencia
==========

:Autores:
    Mr-E

:Fecha:
    2015/03/20

:Versión:
    0.0.20150320


Descripción
-----------
Aplicación en Python para comprobar la vigencia de comprobantes CFDi en la ruta especificada usando el web service del SAT.

Objetivos y alcances
-----------

    + Para aprendizaje en Python (xml, webservice, qrcode, pdf, gui/tk/qt)
    + Integrar un visor (CFDView) que genere la representación impresa un formato simple "sin moños"
    + Que detecte correctamente el tipo de comprobante (factura, nomina, etc.)
    + Que soporte "drag & drop" ¿será posible en Python + GUI: tk/Qt?
    + Básicamente he integrado las ideas de otros trantando con ello de aprender Python y crear algo útil. (seguro ya existe)
    + Si con esto sale algo útil para la comunidad y que algo aprendamos.

Lectura recomendada:
-------------------
    + http://eli.thegreenplace.net/2012/03/15/processing-xml-in-python-with-elementtree

Problemas iniciales
-----------
PySimpleSOAP v1.16 me esta dando problemas en python +3.2.3
Se ha comprobado que funciona en python 2.7.3

Fallas detectadas:
-----------
Esta falla se puede corregir con el siguiente parche:
    https://github.com/pysimplesoap/pysimplesoap/pull/52

pySimpleSoap falla en version 3.4.3 (windows) y 3.2.3 (ubuntu), con este error:

::

      File "H:\Devel\python\XMLviewBeta\ParseXML-2.py", line 146, in <module>

        servicio.verificaArchivos()

      File "H:\Devel\python\XMLviewBeta\ParseXML-2.py", line 124, in verificaArchivos

        sat.get_estatus(self.__data)

      File "H:\Devel\python\XMLviewBeta\ParseXML-2.py", line 36, in get_estatus

        client = SoapClient(wsdl=self._webservice)

      File "C:\Python34\lib\site-packages\pysimplesoap\client.py", line 173, in __init__

        self.services = wsdl and self.wsdl_parse(wsdl, cache=cache)

      File "C:\Python34\lib\site-packages\pysimplesoap\client.py", line 836, in wsdl_parse

        services = self._xml_tree_to_services(wsdl, cache, force_download)

      File "C:\Python34\lib\site-packages\pysimplesoap\client.py", line 757, in _xml_tree_to_services

        for name, msg in op['fault_msgs'].iteritems():

    AttributeError: 'dict' object has no attribute 'iteritems'

Créditos
--------
Este proyecto está basado en código de

:descargar-cfdi:
    jjlopez
:admin-cfdi:
    Mauricio Baez y PythonCabal
:Otros:
    Con información de otras páginas en la WEB.


Ligas
-----
Mr-E
  https://github.com/Mr-E

jjlopez:
  https://github.com/jjlopez/descargar-cfdi

Mauricio Baeza
    https://github.com/mauriciobaeza

PythonCabal
    http://wiki.cabal.mx/wiki/PythonCabal

.. Links
.. _Mr-E: https://github.com/Mr-E
.. _jjlopez: https://github.com/jjlopez/descargar-cfdi
.. _PythonCabal: http://wiki.cabal.mx/wiki/PythonCabal
