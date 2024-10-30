


# Centro hospitalario identificador de hosñitales y nombres 
query_creation_hospitales = """
CREATE TABLE IF NOT EXISTS hospitales (
    ncodi INT PRIMARY KEY,
    name VARCHAR(300)
);
"""


# Tipos de hospityalizacion de los hospitales 
query_creation_tipo_hosp = """
CREATE TABLE IF NOT EXISTS tipo_hospitalizacion (
    tipo_id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) UNIQUE NOT NULL
);
"""


# Gastos
query_creation_gastos = """
CREATE TABLE IF NOT EXISTS gastos (
    gastos_id SERIAL PRIMARY KEY,
    ncodi INT NOT NULL,
    año INT NOT NULL,
    totalcompra NUMERIC,
    producfarma NUMERIC,
    materialsani NUMERIC,
    implantes NUMERIC,
    restomateriasani NUMERIC,
    servcontratado NUMERIC,
    trabajocontratado NUMERIC,
    xrestocompras NUMERIC,
    variaexistencias NUMERIC,
    servexteriores NUMERIC,
    sumistro NUMERIC,
    xrestoserviexter NUMERIC,
    gastopersonal NUMERIC,
    sueldos NUMERIC,
    indemnizacion NUMERIC,
    segsocempresa NUMERIC,
    otrgassocial NUMERIC,
    dotaamortizacion NUMERIC,
    perdidadeterioro NUMERIC,
    xrestogasto NUMERIC,
    totcompragasto NUMERIC,
    FOREIGN KEY (ncodi) REFERENCES hospitales(ncodi)
);
"""

# Ingresos hospitalizaciones 
query_creation_ingresos = """
CREATE TABLE IF NOT EXISTS ingresos (
    id_ingresos SERIAL PRIMARY KEY,
    ncodi INT NOT NULL,
    particulares NUMERIC,
    aseguradoras NUMERIC,
    aseguradoras_enfermedad NUMERIC,
    aseguradoras_trafico NUMERIC,
    mutuas NUMERIC,
    tipo_id INT NOT NULL,
    FOREIGN KEY (ncodi) REFERENCES hospitales(ncodi),
    FOREIGN KEY (tipo_id) REFERENCES tipo_hospitalizacion(tipo_id)
);
"""
