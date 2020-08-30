# funciones : Retenciones Mensuales
Enero = [ 1200,5000,2800,9100,7800,9870,7895,2000]
Febrero = [8790,5200,3500,4800,9870,57800,2580]
Marzo= [5692,9780,2589,4593,2583,2001]

def retenciones_totales (variable):
	retencion total= 0
	for factura in variable:
		if factura >= 1500 :
			retencion_mensual = retencion_mensual + (factura * 0.03)
   return retencion_mensual


   print (retenciones_totales(Enero))



