#!/usr/bin/env python
#coding:utf-8
import xlsxwriter

datos = [{'item1':1, 'item2':2, 'item3':3 }, {'item1':1, 'item2':3, 'item3':5 }]

# Seteo las filay columna inicial
row = 0
col = 0

# Creo el libro y le agrego una hoja
workbook = xlsxwriter.Workbook('tablaConFormulas.xlsx')
worksheet = workbook.add_worksheet()

# Creo los formatos
encabezado = workbook.add_format({'bold': True, 'bg_color':'blue'})
filaGris = workbook.add_format({'bg_color':'gray'})
filaBlanca = workbook.add_format({})

# Escribo el encabezado de la tabla
worksheet.write(row, col, 'item1', encabezado)
worksheet.write(row, col + 1, 'item2', encabezado)
worksheet.write(row, col + 2, 'item3', encabezado)
worksheet.write(row, col + 3, 'suma', encabezado)
row += 1

# Lleno la tabla de datos
for elem in datos:
    if row%2==0:
      tipoFila = filaGris
    else:
      tipoFila = filaBlanca
  
    worksheet.write(row, col, elem['item1'], tipoFila)
    worksheet.write(row, col + 1, elem['item2'], tipoFila)
    worksheet.write(row, col + 2, elem['item3'], tipoFila)

    rangoSuma = 'A' + str(row+1) +':C'+str(row+1) # Para formulas se comienza a indexar por 1
    worksheet.write_formula(row, col + 3, '=+SUM(' + rangoSuma + ')', tipoFila)
    row += 1

workbook.close()

