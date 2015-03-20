#!/usr/bin/env python
# -*- coding: utf-8 -*-
# version 0.0.20150320
# con apoyo de proyectos GIT: ".." ".." ".."
#
import os
import moment
from xml.dom import minidom

from pysimplesoap.client import SoapClient, SoapFault
try:
    from subprocess import DEVNULL
except ImportError:
    DEVNULL = open(os.devnull, 'wb')


class SAT(object):
    '''
    Gracias! mauriciobaeza https://github.com/mauriciobaeza
    '''

    _webservice = 'https://consultaqr.facturaelectronica.sat.gob.mx/' \
        'consultacfdiservice.svc?wsdl'

    def __init__(self):
        self.error = ''
        self.msg = ''

    def get_estatus(self, data):
        try:
            args = '?re={emisor_rfc}&rr={receptor_rfc}&tt={total}&id={uuid}'
            # data = {'emisor_rfc': 'ABC010101000', 'receptor_rfc': 'XAXX010101000', 'total': '1.23', 'uuid': 'xxxx-xxx-xxx-xxx'}
            fac = args.format(**data)
            client = SoapClient(wsdl=self._webservice)
            fac = args.format(**data)
            res = client.Consulta(fac)
            if 'ConsultaResult' in res:
                self.msg = res['ConsultaResult']['Estado']
                return True
            return False
        except SoapFault as sf:
            self.error = sf.faultstring
            return False


class ParseXML:
    '''
    Gracias! jjlopez https://github.com/jjlopez
    '''
    def __init__(self, direccionOrigen, boolVerifica):  # , direccionDestino):
        self.__direccionOrigen = direccionOrigen
        #self.__direccionDestino=direccionDestino
        self.__data = {'emisor_rfc': '', 'receptor_rfc': '', 'total': '', 'uuid': ''}
        self.__boolVerifica = boolVerifica

    def __getFiles(self, directory):
        file_paths = []
        for root, directories, files in os.walk(directory):
            for filename in files:
                fnm, fex = os.path.splitext(filename)
                # hagamos la comparacion en minuscula sin afectar el nombre de archivo
                if fex.lower() == '.xml':
                    filepath = os.path.join(root, filename)
                    file_paths.append(filepath)
        return file_paths

    def verificaArchivos(self):
        sat = SAT()  # probemos el servicio

        archivosOrigen = self.__getFiles(self.__direccionOrigen)
        for filename in archivosOrigen:
            xmldoc = minidom.parse(filename)
            cfdiComprobante = xmldoc.getElementsByTagName('cfdi:Comprobante')
            tfdTimbreFiscal = xmldoc.getElementsByTagName('tfd:TimbreFiscalDigital')
            cfdiEmisor = xmldoc.getElementsByTagName('cfdi:Emisor')
            cfdiReceptor = xmldoc.getElementsByTagName('cfdi:Receptor')
            cfdiTotal = cfdiComprobante[0].attributes['total'].value

            # Valores para el webservice y para mostrar en pantalla
            UUID = tfdTimbreFiscal[0].attributes['UUID'].value.upper()
            emisorRFC = cfdiEmisor[0].attributes['rfc'].value.upper()
            emisorNombre = cfdiEmisor[0].attributes['nombre'].value.upper()
            receptorRFC = cfdiReceptor[0].attributes['rfc'].value.upper()
            receptorNombre = cfdiReceptor[0].attributes['nombre'].value.upper()

            self.__data['emisor_rfc'] = emisorRFC
            self.__data['receptor_rfc'] = receptorRFC
            self.__data['total'] = cfdiTotal
            self.__data['uuid'] = UUID
            if self.__boolVerifica:
                sat.get_estatus(self.__data)
            else:
                sat.msg = u'(No se verificó)'
            #print(('\n%s, %s, %s, %s, %s, %s, %s' % (sat.msg, emisorRFC, emisorNombre, receptorRFC, receptorNombre, cfdiTotal, UUID)))
            print(('\n%s, %s, %s' % (sat.msg, emisorRFC, emisorNombre)))
            print(('%s, %s' % (receptorRFC, receptorNombre)))
            print(('%s, %s' % (cfdiTotal, UUID)))

# Cambiar "False" a "True" para probar el webservice del SAT
servicio = ParseXML(os.curdir, False)
#servicio = ParseXML(os.curdir, True)
# Para probar colocar algunos XMLs en la carpeta donde esta este programa o indicar una ruta:
# servicio = ParseXML('c:\CarpetaConXML', False)
# servicio = ParseXML('/home/mr-E/CarpetaConXML', False)

servicio.verificaArchivos()
