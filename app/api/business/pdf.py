from fpdf import FPDF
from datetime import datetime
import os
from .toEmail import Email


class PDF:

    def __init__(self):
        pass

    def fecha(self, tipo):
        now = datetime.now()
        months = ("Enero", "Febrero", "Marzo", "Abri", "Mayo",
                "Junio", "Julio", "Agosto", "Septiembre",
                "Octubre", "Noviembre", "Diciembre")
        if tipo == "inicio":
            #return 'el día {} de {} del {}'.format(now.day, months[now.month - 1], now.year)
            return 'el día 10 de diciembre 2020'
        if tipo == "final":
            #return 'el día {} de {} del {}'.format(now.day, months[now.month - 1], now.year + 1)
            return 'el 10 de diciembre del 2021'

    def text(self, data):

        textoContrato = """"""
        with open(os.path.join(os.path.dirname(os.path.dirname(__file__)),
                'business/contrato.txt')) as file_in:
            # lines = []
            for line in file_in:
                textoContrato = textoContrato + line

        # NOMBRE_ARRENDADOR_REMPLAZO
        NRR = \
            textoContrato.replace('${NOMBRE_ARRENDADOR}',
                                data['NOMBRE_ARRENDADOR'].upper())
        # NOMBRE_ARRENDATARIO_REMPLAZO
        NAR = \
            NRR.replace('${NOMBRE_ARRENDATARIO}',
                        data['NOMBRE_ARRENDATARIO'].upper())
        # NUMERO_ESCRITURA_REMPLAZO
        NER = \
            NAR.replace('${NUMERO_ESCRITURA}',
                        '')
        # TIPO_INMUEBLE_REMPLAZO
        TIR = \
            NER.replace('${TIPO_INMUEBLE}',
                        data['TIPO_INMUEBLE'])
        # DIRECCION_INMUEBLE_REMPLAZO
        DIR = \
            TIR.replace('${DIRECCION_INMUEBLE}',
                        data['DIRECCION_INMUEBLE'])
        # SERVICIO_A_OFRECER_REMPLAZO
        SAOR = \
            DIR.replace('${SERVICIO_A_OFRECER}',
                        data['SERVICIO_A_OFRECER'])
        # FECHA_INICIO_REMPLAZO
        FIR = \
            SAOR.replace('${FECHA_INICIO}',
                        PDF.fecha(self, "inicio"))
        # FECHA_FINAL_REMPLAZO
        FFR = \
            FIR.replace('${FECHA_FINAL}',
                        PDF.fecha(self, "final"))
        # PRECIO_INMUEBLE_REMPLAZO
        PIR = \
            FFR.replace('${PRECIO_INMUEBLE}',
                        str(data['PRECIO_INMUEBLE']))
        # PRECIO_DEPOSITO_REMPLAZO
        PDR = \
            PIR.replace('${PRECIO_DEPOSITO}',
                        str(data['PRECIO_DEPOSITO']))
        # PLAZO_GRACIA_REMPLAZO
        PGR = \
            PDR.replace('${PLAZO_GRACIA}',
                        data['PLAZO_GRACIA'])
        # PORCENTAJE_AUMENTO_REMPLAZO
        PAR = \
            PGR.replace('${PORCENTAJE_AUMENTO}',
                        str(data['PORCENTAJE_AUMENTO'])+"%")
        # DIRRECCION_ARRENDADOR_REMPLAZO
        DAR = \
            PAR.replace('${DIRRECCION_ARRENDADOR}',
                        data['DIRRECCION_ARRENDADOR'])
        return DAR

    def buildContract(self, data, *args, **kw):
        try:
            pdf = FPDF(format='letter', unit='in')
            pdf.l_margin = pdf.l_margin*2.8
            pdf.r_margin = pdf.r_margin*2.8
            pdf.t_margin = pdf.t_margin*1.5
            pdf.b_margin = pdf.b_margin*1.5
            pdf.add_page()
            # eph = pdf.h - pdf.t_margin - pdf.b_margin
            pdf.set_font('Times', '', 14)
            th = 0.20
            pdf.ln(2*th)
            epw = pdf.w - pdf.l_margin - pdf.r_margin
            pdf.multi_cell(epw, th, PDF.text(self, data))
            pdf.output('api/business/contrato_arrendamiento.pdf', 'F')
            #Email.sendEmail(self, data)
            return True
        except Exception as error:
            print(error)
            return False
