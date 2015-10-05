#!/usr/bin/env python
#coding:utf-8
import xlsxwriter

datos = [{'item1':'foo', 'item2':'baz', 'item3':'bar' }, {'item1':'1', 'item2':'2', 'item3':'3' }]

# Seteo las filay columna inicial
row = 0
col = 0

# Creo el libro y le agrego una hoja
workbook = xlsxwriter.Workbook('tablaSimple.xlsx')
worksheet = workbook.add_worksheet()

# Escribo el encabezado de la tabla
worksheet.write(row, col, 'item1')
worksheet.write(row, col + 1, 'item2')
worksheet.write(row, col + 2, 'item3')
row += 1

# Lleno la tabla de datos
for elem in datos:
    worksheet.write(row, col, elem['item1'])
    worksheet.write(row, col + 1, elem['item2'])
    worksheet.write(row, col + 2, elem['item3'])
    row += 1

workbook.close()

