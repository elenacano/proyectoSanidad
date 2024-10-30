query_carga_hospitales = """
INSERT INTO hospitales (ncodi) VALUES (%s)""" # insertar valores %s es como un formato. como un argumento

query_carga_tipo_hospi = """INSERT INTO tipo_hospitalizacion (tipo_id, nombre)
VALUES (%s, %s)""" # insertar valores %s es como un formato. como un argumento

query_carga_gastos = """INSERT INTO gastos 
                        (anio, 
                        totalcompra, 
                        producfarma, 
                        materialsani, 
                        implantes, 
                        restomateriasani, 
                        servcontratado, 
                        trabajocontratado, 
                        xrestocompras, 
                        variaexistencias, 
                        servexteriores, 
                        sumistro, 
                        xrestoserviexter, 
                        gastopersonal, 
                        sueldos, 
                        indemnizacion, 
                        segsocempresa, 
                        otrgassocial, 
                        dotaamortizacion, 
                        perdidadeterioro, 
                        xrestogasto, 
                        totcompragasto, 
                        ncodi) 
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""" 
                        # insertar valores %s es como un formato. como un argumento

query_carga_ingresos = """INSERT INTO ingresos 
(anio, particulares, aseguradoras, aseguradoras_enfermedad, aseguradoras_trafico, mutuas, ncodi, tipo_id) 
VALUES (%s, %s, %s, %s, %s, %s, %s, %s)""" 

# insertar valores %s es como un formato. como un argumento