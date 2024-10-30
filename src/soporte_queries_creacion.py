query_creacion_ncodi = """create table if not exists ncodi (
                            id_ncodi int primary key,
                            ncodi int not null
                            );"""

query_creacion_tipo_hospi = """create table if not exists tipo_hospi (
                            id_tipo_hospi int primary key,
                            nombre varchar(100) not null
                            );"""


query_creacion_gastos = """create table if not exists gastos (
                            id_gastos SERIAL primary key,
                            id_ncodi int not null,
                            anio int not null,
                            totalcompra int,
                            producto_farma float,
                            material_sanitario int,
                            implantes float,
                            resto_material_sanitario float,
                            servicio_contratado float,
                            trabajo_contratado float,
                            resto_compras float,
                            varias_existencias float,
                            servicios_exteriores int,
                            suministro float,
                            resto_servicios_exteriores float,
                            gasto_personal int,
                            sueldos int,
                            indemnizacion float,
                            ss_empresa int,
                            ss_otra float,
                            dotacion_amortizacion float,
                            perdida_deterioro float,
                            resto_gastos float,
                            total_compra_gastos int,
                            foreign key (id_ncodi) references ncodi(id_ncodi) on delete restrict on update cascade
                            );"""

query_creacion_ingresos = """create table if not exists ingresos (
                            id_ingresos SERIAL primary key,
                            id_ncodi int not null,
                            anio int not null,
                            id_tipo_hospi int not null,
                            particulares float,
                            aseguradoras float,
                            aseguradoras_enfermedad float,
                            aseguradoras_trafico float,
                            mutuas float,
                            foreign key (id_ncodi) references ncodi(id_ncodi) on delete restrict on update cascade,
                            foreign key (id_tipo_hospi) references tipo_hospi(id_tipo_hospi) on delete restrict on update cascade
                            );"""