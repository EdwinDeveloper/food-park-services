from fpdf import FPDF
from datetime import datetime
import os

def buildContract():

    pdf=FPDF(format='letter',unit='in')
    pdf.l_margin = pdf.l_margin*2.8
    pdf.r_margin = pdf.r_margin*2.8
    pdf.t_margin = pdf.t_margin*1.5
    pdf.b_margin = pdf.b_margin*1.5
    pdf.add_page()

    epw = pdf.w - pdf.l_margin - pdf.r_margin
    eph = pdf.h - pdf.t_margin - pdf.b_margin

    pdf.set_font('Times','',14)
    th = 0.20

    pdf.ln(2*th)

    textoContrato = """"""

    with open( os.path.join(os.path.dirname(os.path.dirname(__file__)), 'api/contrato.txt') ) as file_in:
        lines = []
        for line in file_in:
            textoContrato = textoContrato + line

    now = datetime.now()
    months = ("Enero", "Febrero", "Marzo", "Abri", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")

    NOMBRE_ARRENDADOR_REMPLAZO = textoContrato.replace('${NOMBRE_ARRENDADOR}', 'Santiago Pérez Ontiveros'.upper())
    NOMBRE_ARRENDATARIO_REMPLAZO = NOMBRE_ARRENDADOR_REMPLAZO.replace('${NOMBRE_ARRENDATARIO}', 'Roberto Israel Perez Ochoa'.upper())
    NUMERO_ESCRITURA_REMPLAZO = NOMBRE_ARRENDATARIO_REMPLAZO.replace('${NUMERO_ESCRITURA}', '')
    TIPO_INMUEBLE_REMPLAZO = NUMERO_ESCRITURA_REMPLAZO.replace('${TIPO_INMUEBLE}', 'LOCAL')
    DIRECCION_INMUEBLE_REMPLAZO = TIPO_INMUEBLE_REMPLAZO.replace('${DIRECCION_INMUEBLE}', 'AV. Tepic Vallarta #32')
    SERVICIO_A_OFRECER_REMPLAZO = DIRECCION_INMUEBLE_REMPLAZO.replace('${SERVICIO_A_OFRECER}', 'RENTA LOCAL')
    FECHA_INICIO_REMPLAZO = SERVICIO_A_OFRECER_REMPLAZO.replace('${FECHA_INICIO}', 'el día {} de {} del {}'.format( now.day , months[ now.month - 1 ] , now.year ))
    FECHA_FINAL_REMPLAZO = FECHA_INICIO_REMPLAZO.replace('${FECHA_FINAL}', 'el día {} de {} del {}'.format( now.day , months[ now.month - 1 ] , now.year + 1 ))
    PRECIO_INMUEBLE_REMPLAZO = FECHA_FINAL_REMPLAZO.replace('${PRECIO_INMUEBLE}', '6,000')
    PRECIO_DEPOSITO_REMPLAZO = PRECIO_INMUEBLE_REMPLAZO.replace('${PRECIO_DEPOSITO}', '6,500')
    PLAZO_GRACIA_REMPLAZO = PRECIO_DEPOSITO_REMPLAZO.replace('${PLAZO_GRACIA}', '2')
    PORCENTAJE_AUMENTO_REMPLAZO = PLAZO_GRACIA_REMPLAZO.replace('${PORCENTAJE_AUMENTO}', '10%')
    DIRRECCION_ARRENDADOR_REMPLAZO = PORCENTAJE_AUMENTO_REMPLAZO.replace('${DIRRECCION_ARRENDADOR}', 'Federalismo sur 341 cp: 44100')

    pdf.multi_cell(epw,th, DIRRECCION_ARRENDADOR_REMPLAZO)
    pdf.output('contrato_arrendamiento.pdf','F')