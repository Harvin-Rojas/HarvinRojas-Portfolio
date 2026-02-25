CREATE TABLE Aerolinea (
    id_aerolinea NUMBER(4) PRIMARY KEY,
    nombre VARCHAR2(50) NOT NULL UNIQUE,
    país_origen VARCHAR2(50),
    sitio_web VARCHAR2(100)
);


CREATE TABLE Avion (
    id_avion NUMBER(10) PRIMARY KEY,
    modelo VARCHAR2(50) NOT NULL,
    capacidad_pasajeros NUMBER(3) CHECK (capacidad_pasajeros <= 180),
    estado_operativo VARCHAR2(20) CHECK (estado_operativo IN ('En servicio', 'En mantenimiento')),
    id_aerolinea NUMBER(4),
    CONSTRAINT fk_avion_aerolinea FOREIGN KEY (id_aerolinea) REFERENCES Aerolinea(id_aerolinea)
);

CREATE TABLE Vuelo (
    id_vuelo VARCHAR2(10) PRIMARY KEY,
    origen VARCHAR2(50) NOT NULL,
    destino VARCHAR2(50) NOT NULL,
    fecha_hora_salida DATE,
    estado VARCHAR2(20) CHECK (estado IN ('Programado', 'Cancelado', 'En vuelo', 'Finalizado')),
    id_avion NUMBER(10),
    CONSTRAINT fk_vuelo_avion FOREIGN KEY (id_avion) REFERENCES Avion(id_avion)
);

CREATE TABLE Pasajero (
    id_pasajero NUMBER(10) PRIMARY KEY,
    nombre_completo VARCHAR2(30) NOT NULL,
    email VARCHAR2(50) UNIQUE,
    telefono VARCHAR2(15)
);

CREATE TABLE Equipaje (
    id_equipaje NUMBER(10) PRIMARY KEY,
    id_pasajero NUMBER(10),
    id_vuelo VARCHAR2(10),
    peso_kg NUMBER(4,2) CHECK (peso_kg > 0),
    tipo VARCHAR2(30),
    CONSTRAINT fk_equipaje_pasajero FOREIGN KEY (id_pasajero) REFERENCES Pasajero(id_pasajero),
    CONSTRAINT fk_equipaje_vuelo FOREIGN KEY (id_vuelo) REFERENCES Vuelo(id_vuelo)
);

CREATE TABLE Empleado (
    id_empleado NUMBER(10) PRIMARY KEY,
    nombre_completo VARCHAR2(50) NOT NULL,
    tipo_empleado VARCHAR2(20) CHECK (tipo_empleado IN ('Tripulante', 'Logística')),
    fecha_ingreso DATE
);

CREATE TABLE Mantenimiento (
    id_mantenimiento NUMBER(10) PRIMARY KEY,
    fecha DATE NOT NULL,
    tipo_mantenimiento VARCHAR2(200) NOT NULL,
    id_avion NUMBER(10),
    id_empleado NUMBER(10),
    CONSTRAINT fk_mantenimiento_avion FOREIGN KEY (id_avion) REFERENCES Avion(id_avion),
    CONSTRAINT fk_mantenimiento_empleado FOREIGN KEY (id_empleado) REFERENCES Empleado(id_empleado)
);

CREATE TABLE Ticket (
    id_ticket NUMBER(10) PRIMARY KEY,
    id_pasajero NUMBER(10),
    id_vuelo VARCHAR2(10),
    asiento NUMBER(3),
    checkin_realizado CHAR(1) CHECK (checkin_realizado IN ('Y','N')),
    CONSTRAINT fk_ticket_pasajero FOREIGN KEY (id_pasajero) REFERENCES Pasajero(id_pasajero),
    CONSTRAINT fk_ticket_vuelo FOREIGN KEY (id_vuelo) REFERENCES Vuelo(id_vuelo),
    CONSTRAINT uq_ticket_asiento UNIQUE (id_vuelo, asiento)
);

CREATE TABLE Asignar_avion (
    id_empleado NUMBER(10),
    id_avion NUMBER(10),
    fecha_inicio DATE,
    fecha_fin DATE,
    PRIMARY KEY (id_empleado, id_avion, fecha_inicio),
    CONSTRAINT fk_asignar_empleado FOREIGN KEY (id_empleado) REFERENCES Empleado(id_empleado),
    CONSTRAINT fk_asignar_avion FOREIGN KEY (id_avion) REFERENCES Avion(id_avion),
    CONSTRAINT ck_fecha CHECK (fecha_inicio < fecha_fin)
);

CREATE TABLE Documento_Generado (
    id_documento NUMBER(10) PRIMARY KEY,
    tipo_documento VARCHAR2(50) NOT NULL,
    fecha_generacion DATE NOT NULL,
    descripcion VARCHAR2(100)
);



INSERT ALL
  INTO Aerolinea (id_aerolinea, nombre, país_origen, sitio_web) VALUES (1, 'Avianca', 'Colombia', 'https://aerolineacolombia.com')
  INTO Aerolinea (id_aerolinea, nombre, país_origen, sitio_web) VALUES (2, 'SkyFly', 'Estados Unidos', 'https://skyfly.com')
  INTO Aerolinea (id_aerolinea, nombre, país_origen, sitio_web) VALUES (3, 'Air Europa', 'España', 'https://aireuropa.com')
  INTO Aerolinea (id_aerolinea, nombre, país_origen, sitio_web) VALUES (4, 'Jet Airways', 'India', 'https://jetairways.com')
  INTO Aerolinea (id_aerolinea, nombre, país_origen, sitio_web) VALUES (5, 'FlyHigh', 'México', 'https://flyhigh.mx')
SELECT * FROM dual;

INSERT ALL
  INTO Avion (id_avion, modelo, capacidad_pasajeros, estado_operativo, id_aerolinea) VALUES (101, 'Boeing 737', 150, 'En servicio', 1)
  INTO Avion (id_avion, modelo, capacidad_pasajeros, estado_operativo, id_aerolinea) VALUES (102, 'Airbus A320', 180, 'En servicio', 2)
  INTO Avion (id_avion, modelo, capacidad_pasajeros, estado_operativo, id_aerolinea) VALUES (103, 'Boeing 777', 180, 'En mantenimiento', 3)
  INTO Avion (id_avion, modelo, capacidad_pasajeros, estado_operativo, id_aerolinea) VALUES (104, 'Embraer 190', 100, 'En servicio', 4)
  INTO Avion (id_avion, modelo, capacidad_pasajeros, estado_operativo, id_aerolinea) VALUES (105, 'Bombardier Q400', 80, 'En servicio', 5)
SELECT * FROM dual;

INSERT ALL
  INTO Vuelo (id_vuelo, origen, destino, fecha_hora_salida, estado, id_avion) VALUES ('V001', 'Bogotá', 'Medellín', TO_DATE('2025-12-01 08:00', 'YYYY-MM-DD HH24:MI'), 'Programado', 101)
  INTO Vuelo (id_vuelo, origen, destino, fecha_hora_salida, estado, id_avion) VALUES ('V002', 'Miami', 'Nueva York', TO_DATE('2025-12-02 12:00', 'YYYY-MM-DD HH24:MI'), 'En vuelo', 102)
  INTO Vuelo (id_vuelo, origen, destino, fecha_hora_salida, estado, id_avion) VALUES ('V003', 'Madrid', 'Barcelona', TO_DATE('2025-12-03 09:30', 'YYYY-MM-DD HH24:MI'), 'Cancelado', 103)
  INTO Vuelo (id_vuelo, origen, destino, fecha_hora_salida, estado, id_avion) VALUES ('V004', 'Delhi', 'Mumbai', TO_DATE('2025-12-04 15:00', 'YYYY-MM-DD HH24:MI'), 'Finalizado', 104)
  INTO Vuelo (id_vuelo, origen, destino, fecha_hora_salida, estado, id_avion) VALUES ('V005', 'Ciudad de México', 'Guadalajara', TO_DATE('2025-12-05 07:00', 'YYYY-MM-DD HH24:MI'), 'Programado', 105)
SELECT * FROM dual;

INSERT ALL
  INTO Pasajero (id_pasajero, nombre_completo, email, telefono) VALUES (201, 'Juan Pérez', 'juan.perez@correo.com', '+571234567890')
  INTO Pasajero (id_pasajero, nombre_completo, email, telefono) VALUES (202, 'Ana Gómez', 'ana.gomez@correo.com', '+573003003003')
  INTO Pasajero (id_pasajero, nombre_completo, email, telefono) VALUES (203, 'Carlos Rodríguez', 'carlos.rodriguez@correo.com', '+57111222333')
  INTO Pasajero (id_pasajero, nombre_completo, email, telefono) VALUES (204, 'María Fernández', 'maria.fernandez@correo.com', '+573224455667')
  INTO Pasajero (id_pasajero, nombre_completo, email, telefono) VALUES (205, 'Laura Martínez', 'laura.martinez@correo.com', '+573335556667')
SELECT * FROM dual;D

INSERT ALL
  INTO Equipaje (id_equipaje, id_pasajero, id_vuelo, peso_kg, tipo) VALUES (301, 201, 'V001', 15.50, 'Maleta')
  INTO Equipaje (id_equipaje, id_pasajero, id_vuelo, peso_kg, tipo) VALUES (302, 202, 'V002', 8.75, 'Bolso')
  INTO Equipaje (id_equipaje, id_pasajero, id_vuelo, peso_kg, tipo) VALUES (303, 203, 'V003', 12.00, 'Maleta')
  INTO Equipaje (id_equipaje, id_pasajero, id_vuelo, peso_kg, tipo) VALUES (304, 204, 'V004', 9.20, 'Bolso')
  INTO Equipaje (id_equipaje, id_pasajero, id_vuelo, peso_kg, tipo) VALUES (305, 205, 'V005', 20.00, 'Maleta')
SELECT * FROM dual;

INSERT ALL
  INTO Empleado (id_empleado, nombre_completo, tipo_empleado, fecha_ingreso) VALUES (401, 'Pedro Sánchez', 'Tripulante', TO_DATE('2020-01-15', 'YYYY-MM-DD'))
  INTO Empleado (id_empleado, nombre_completo, tipo_empleado, fecha_ingreso) VALUES (402, 'Lucía Martínez', 'Logística', TO_DATE('2019-03-10', 'YYYY-MM-DD'))
  INTO Empleado (id_empleado, nombre_completo, tipo_empleado, fecha_ingreso) VALUES (403, 'Andrés Gómez', 'Tripulante', TO_DATE('2021-06-01', 'YYYY-MM-DD'))
  INTO Empleado (id_empleado, nombre_completo, tipo_empleado, fecha_ingreso) VALUES (404, 'Sofía López', 'Logística', TO_DATE('2018-11-20', 'YYYY-MM-DD'))
  INTO Empleado (id_empleado, nombre_completo, tipo_empleado, fecha_ingreso) VALUES (405, 'Miguel Torres', 'Tripulante', TO_DATE('2022-02-05', 'YYYY-MM-DD'))
SELECT * FROM dual;

INSERT ALL
  INTO Mantenimiento (id_mantenimiento, fecha, tipo_mantenimiento, id_avion, id_empleado) VALUES (501, TO_DATE('2025-11-01', 'YYYY-MM-DD'), 'Revisión general', 101, 402)
  INTO Mantenimiento (id_mantenimiento, fecha, tipo_mantenimiento, id_avion, id_empleado) VALUES (502, TO_DATE('2025-10-15', 'YYYY-MM-DD'), 'Cambio de motor', 103, 404)
  INTO Mantenimiento (id_mantenimiento, fecha, tipo_mantenimiento, id_avion, id_empleado) VALUES (503, TO_DATE('2025-11-20', 'YYYY-MM-DD'), 'Limpieza profunda', 105, 402)
  INTO Mantenimiento (id_mantenimiento, fecha, tipo_mantenimiento, id_avion, id_empleado) VALUES (504, TO_DATE('2025-09-30', 'YYYY-MM-DD'), 'Actualización software', 102, 405)
  INTO Mantenimiento (id_mantenimiento, fecha, tipo_mantenimiento, id_avion, id_empleado) VALUES (505, TO_DATE('2025-11-05', 'YYYY-MM-DD'), 'Revisión de frenos', 104, 403)
SELECT * FROM dual;

INSERT ALL
  INTO Ticket (id_ticket, id_pasajero, id_vuelo, asiento, checkin_realizado) VALUES (601, 201, 'V001', 12, 'Y')
  INTO Ticket (id_ticket, id_pasajero, id_vuelo, asiento, checkin_realizado) VALUES (602, 202, 'V002', 15, 'N')
  INTO Ticket (id_ticket, id_pasajero, id_vuelo, asiento, checkin_realizado) VALUES (603, 203, 'V003', 10, 'Y')
  INTO Ticket (id_ticket, id_pasajero, id_vuelo, asiento, checkin_realizado) VALUES (604, 204, 'V004', 22, 'N')
  INTO Ticket (id_ticket, id_pasajero, id_vuelo, asiento, checkin_realizado) VALUES (605, 205, 'V005', 5, 'Y')
SELECT * FROM dual;

INSERT ALL
  INTO Asignar_avion (id_empleado, id_avion, fecha_inicio, fecha_fin) VALUES (401, 101, TO_DATE('2024-01-01', 'YYYY-MM-DD'), TO_DATE('2025-12-31', 'YYYY-MM-DD'))
  INTO Asignar_avion (id_empleado, id_avion, fecha_inicio, fecha_fin) VALUES (402, 103, TO_DATE('2023-06-01', 'YYYY-MM-DD'), TO_DATE('2025-11-30', 'YYYY-MM-DD'))
  INTO Asignar_avion (id_empleado, id_avion, fecha_inicio, fecha_fin) VALUES (403, 104, TO_DATE('2024-05-01', 'YYYY-MM-DD'), TO_DATE('2025-12-31', 'YYYY-MM-DD'))
  INTO Asignar_avion (id_empleado, id_avion, fecha_inicio, fecha_fin) VALUES (404, 105, TO_DATE('2024-07-01', 'YYYY-MM-DD'), TO_DATE('2025-12-31', 'YYYY-MM-DD'))
  INTO Asignar_avion (id_empleado, id_avion, fecha_inicio, fecha_fin) VALUES (405, 102, TO_DATE('2025-01-01', 'YYYY-MM-DD'), TO_DATE('2025-12-31', 'YYYY-MM-DD'))
SELECT * FROM dual;

INSERT ALL
  INTO Documento_Generado (id_documento, tipo_documento, fecha_generacion, descripcion) VALUES (701, 'Reporte Pasajeros', TO_DATE('2025-11-20', 'YYYY-MM-DD'), 'Listado completo de pasajeros')
  INTO Documento_Generado (id_documento, tipo_documento, fecha_generacion, descripcion) VALUES (702, 'Reporte Vuelos', TO_DATE('2025-11-21', 'YYYY-MM-DD'), 'Listado de vuelos programados')
  INTO Documento_Generado (id_documento, tipo_documento, fecha_generacion, descripcion) VALUES (703, 'Reporte Mantenimientos', TO_DATE('2025-11-22', 'YYYY-MM-DD'), 'Historial de mantenimientos')
  INTO Documento_Generado (id_documento, tipo_documento, fecha_generacion, descripcion) VALUES (704, 'Reporte Equipaje', TO_DATE('2025-11-23', 'YYYY-MM-DD'), 'Equipajes extraviados')
  INTO Documento_Generado (id_documento, tipo_documento, fecha_generacion, descripcion) VALUES (705, 'Reporte Tripulación', TO_DATE('2025-11-24', 'YYYY-MM-DD'), 'Tripulación por vuelo')
SELECT * FROM dual;


SELECT *
FROM Aerolinea;

SELECT *
FROM Pasajero
WHERE email LIKE '%.co%' OR telefono LIKE '+57%';

SELECT *
FROM Vuelo
WHERE estado = 'Programado';

SELECT e.id_equipaje,
       p.nombre_completo AS pasajero,
       v.id_vuelo,
       e.peso_kg,
       e.tipo,
       'Extraviado' AS estado
FROM Equipaje e
JOIN Pasajero p ON e.id_pasajero = p.id_pasajero
JOIN Vuelo v ON e.id_vuelo = v.id_vuelo
WHERE e.Estado = 'Y';




SELECT v.id_vuelo, v.origen, v.destino, v.fecha_hora_salida, v.estado,
       a.nombre AS aerolinea, a.país_origen
FROM Vuelo v
JOIN Avion av ON v.id_avion = av.id_avion
JOIN Aerolinea a ON av.id_aerolinea = a.id_aerolinea;


SELECT av.id_avion, av.modelo, MAX(m.fecha) AS ultima_fecha_mantenimiento
FROM Avion av
LEFT JOIN Mantenimiento m ON av.id_avion = m.id_avion
GROUP BY av.id_avion, av.modelo;

SELECT e.id_empleado, e.nombre_completo, COUNT(m.id_mantenimiento) AS total_mantenimientos
FROM Empleado e
LEFT JOIN Mantenimiento m ON e.id_empleado = m.id_empleado
GROUP BY e.id_empleado, e.nombre_completo;

SELECT av.id_avion, av.modelo, COUNT(v.id_vuelo) AS total_vuelos
FROM Avion av
LEFT JOIN Vuelo v ON av.id_avion = v.id_avion
GROUP BY av.id_avion, av.modelo;

SELECT p.nombre_completo AS pasajero, v.id_vuelo, v.origen, v.destino, a.nombre AS aerolinea
FROM Ticket t
JOIN Pasajero p ON t.id_pasajero = p.id_pasajero
JOIN Vuelo v ON t.id_vuelo = v.id_vuelo
JOIN Avion av ON v.id_avion = av.id_avion
JOIN Aerolinea a ON av.id_aerolinea = a.id_aerolinea;

SELECT e.nombre_completo AS empleado, e.tipo_empleado, v.id_vuelo, v.origen, v.destino, a.nombre AS aerolinea
FROM Asignar_avion aa
JOIN Empleado e ON aa.id_empleado = e.id_empleado
JOIN Avion av ON aa.id_avion = av.id_avion
JOIN Vuelo v ON v.id_avion = av.id_avion
JOIN Aerolinea a ON av.id_aerolinea = a.id_aerolinea
ORDER BY v.id_vuelo;

SELECT p.nombre_completo, e.peso_kg, e.tipo, v.id_vuelo
FROM Equipaje e
JOIN Pasajero p ON e.id_pasajero = p.id_pasajero
JOIN Vuelo v ON e.id_vuelo = v.id_vuelo
WHERE v.id_vuelo IN ('V001','V002'); 

SELECT m.id_mantenimiento, m.fecha, m.tipo_mantenimiento,
       av.id_avion, av.modelo, a.nombre AS aerolinea,
       e.id_empleado, e.nombre_completo
FROM Mantenimiento m
JOIN Avion av ON m.id_avion = av.id_avion
JOIN Aerolinea a ON av.id_aerolinea = a.id_aerolinea
JOIN Empleado e ON m.id_empleado = e.id_empleado;


ALTER TABLE Equipaje
ADD Estado CHAR(1) DEFAULT 'N' CHECK (Estado IN ('Y','N'));

UPDATE Equipaje
SET Estado = 'Y'
WHERE id_equipaje IN (301, 304); 


select * from Equipaje;