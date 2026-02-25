CREATE TABLE Cliente (
    id_cliente NUMBER(15) PRIMARY KEY,
    nombre_completo VARCHAR2(50) NOT NULL,
    telefono VARCHAR2(20) NOT NULL,
    email VARCHAR2(50) NOT NULL CHECK (email LIKE '%@%')
);

CREATE TABLE Empleado (
    id_empleado NUMBER(15) PRIMARY KEY,
    nombre_completo VARCHAR2(50) NOT NULL,
    email VARCHAR2(50) NOT NULL
);

CREATE TABLE Cargo (
    id_cargo NUMBER(15) PRIMARY KEY,
    nombre_cargo VARCHAR2(20) NOT NULL
);

CREATE TABLE Empleado_Cargo (
    id_empleado NUMBER(15) NOT NULL,
    id_cargo NUMBER(15) NOT NULL,
    fecha_inicio DATE NOT NULL,
    fecha_fin DATE,
    PRIMARY KEY (id_empleado, id_cargo, fecha_inicio),
    FOREIGN KEY (id_empleado) REFERENCES Empleado(id_empleado),
    FOREIGN KEY (id_cargo) REFERENCES Cargo(id_cargo),
    CHECK (fecha_fin IS NULL OR fecha_fin > fecha_inicio)
);

CREATE TABLE Servicio (
    id_servicio NUMBER(15) PRIMARY KEY,
    tipo_servicio VARCHAR2(20) NOT NULL CHECK (tipo_servicio IN ('Aéreo', 'Terrestre', 'Acuático', 'Combinado', 'Alojamiento', 'Alimentación', 'Tour')),
    descripcion VARCHAR2(100) NOT NULL,
    costo NUMBER(10,2) NOT NULL CHECK (costo > 0)
);

CREATE TABLE Paquete (
    id_paquete NUMBER(15) PRIMARY KEY,
    nombre_paquete VARCHAR2(20) NOT NULL UNIQUE,
    descripcion VARCHAR2(300) NOT NULL
);

CREATE TABLE Paquete_Servicio (
    id_paquete NUMBER(15) NOT NULL,
    id_servicio NUMBER(15) NOT NULL,
    cantidad NUMBER(2) NOT NULL CHECK (cantidad >= 1),
    PRIMARY KEY (id_paquete, id_servicio),
    FOREIGN KEY (id_paquete) REFERENCES Paquete(id_paquete),
    FOREIGN KEY (id_servicio) REFERENCES Servicio(id_servicio)
);

CREATE TABLE Compra (
    id_compra NUMBER(15) PRIMARY KEY,
    id_cliente NUMBER(15) NOT NULL,
    id_empleado NUMBER(15) NOT NULL,
    fecha_compra DATE NOT NULL,
    total NUMBER(10,2) NOT NULL,
    
    CONSTRAINT fk_compra_cliente 
        FOREIGN KEY (id_cliente)
        REFERENCES Cliente(id_cliente),

    CONSTRAINT fk_compra_empleado
        FOREIGN KEY (id_empleado)
        REFERENCES Empleado(id_empleado)

);

CREATE TABLE Compra_Paquete (
    id_compra NUMBER(15) NOT NULL,
    id_paquete NUMBER(15) NOT NULL,
    cantidad NUMBER(2) NOT NULL CHECK (cantidad >= 1),
    PRIMARY KEY (id_compra, id_paquete),
    FOREIGN KEY (id_compra) REFERENCES Compra(id_compra),
    FOREIGN KEY (id_paquete) REFERENCES Paquete(id_paquete)
);

CREATE TABLE Medio_Pago (
    id_medio_pago NUMBER(15) PRIMARY KEY,
    tipo_medio VARCHAR2(20) NOT NULL CHECK (tipo_medio IN ('Tarjeta Crédito',
     'Tarjeta Débito', 'Efectivo', 'Transferencia', 'PayPal', 'Otro'))
);

CREATE TABLE Cuota (
    id_cuota NUMBER(15) PRIMARY KEY,
    id_compra NUMBER(15) NOT NULL,
    id_medio_pago NUMBER(15) NOT NULL,
    fecha_pago DATE NOT NULL,
    monto NUMBER(10,2) NOT NULL CHECK (monto > 0),
    FOREIGN KEY (id_compra) REFERENCES Compra(id_compra),
    FOREIGN KEY (id_medio_pago) REFERENCES Medio_Pago(id_medio_pago)
);

INSERT ALL
  INTO Cliente (id_cliente, nombre_completo, telefono, email) VALUES (1, 'Juan Pérez', '555-1234', 'juan.perez@email.com')
  INTO Cliente (id_cliente, nombre_completo, telefono, email) VALUES (2, 'María López', '555-2345', 'maria.lopez@email.com')
  INTO Cliente (id_cliente, nombre_completo, telefono, email) VALUES (3, 'Carlos Ramírez', '555-3456', 'carlos.ramirez@email.com')
  INTO Cliente (id_cliente, nombre_completo, telefono, email) VALUES (4, 'Ana Torres', '555-4567', 'ana.torres@email.com')
  INTO Cliente (id_cliente, nombre_completo, telefono, email) VALUES (5, 'Luis García', '555-5678', 'luis.garcia@email.com')
SELECT * FROM dual;
 
INSERT ALL
  INTO Empleado (id_empleado, nombre_completo, email) VALUES (1, 'Pedro Martínez', 'pedro.martinez@email.com')
  INTO Empleado (id_empleado, nombre_completo, email) VALUES (2, 'Laura Sánchez', 'laura.sanchez@email.com')
  INTO Empleado (id_empleado, nombre_completo, email) VALUES (3, 'Miguel Fernández', 'miguel.fernandez@email.com')
  INTO Empleado (id_empleado, nombre_completo, email) VALUES (4, 'Sofía Jiménez', 'sofia.jimenez@email.com')
  INTO Empleado (id_empleado, nombre_completo, email) VALUES (5, 'Jorge Ruiz', 'jorge.ruiz@email.com')
SELECT * FROM dual;

INSERT ALL
  INTO Cargo (id_cargo, nombre_cargo) VALUES (1, 'Agente de Ventas')
  INTO Cargo (id_cargo, nombre_cargo) VALUES (2, 'Ejecutivo de Cuentas')
  INTO Cargo (id_cargo, nombre_cargo) VALUES (3, 'Coordinador de Tours')
  INTO Cargo (id_cargo, nombre_cargo) VALUES (4, 'Promotor de Paquetes')
  INTO Cargo (id_cargo, nombre_cargo) VALUES (5, 'Gerente de Ventas')
SELECT * FROM dual;

INSERT ALL
  INTO Empleado_Cargo (id_empleado, id_cargo, fecha_inicio, fecha_fin) VALUES (1, 1, DATE '2023-01-01', NULL)
  INTO Empleado_Cargo (id_empleado, id_cargo, fecha_inicio, fecha_fin) VALUES (2, 2, DATE '2023-02-01', NULL)
  INTO Empleado_Cargo (id_empleado, id_cargo, fecha_inicio, fecha_fin) VALUES (3, 3, DATE '2023-01-15', NULL)
  INTO Empleado_Cargo (id_empleado, id_cargo, fecha_inicio, fecha_fin) VALUES (4, 4, DATE '2023-03-01', NULL)
  INTO Empleado_Cargo (id_empleado, id_cargo, fecha_inicio, fecha_fin) VALUES (5, 5, DATE '2023-01-10', NULL)
SELECT * FROM dual;


INSERT ALL
  INTO Servicio (id_servicio, tipo_servicio, descripcion, costo) VALUES (1, 'Aéreo', 'Vuelo ida y vuelta a Cancún', 3000)
  INTO Servicio (id_servicio, tipo_servicio, descripcion, costo) VALUES (2, 'Terrestre', 'Transporte terrestre por la ciudad', 500)
  INTO Servicio (id_servicio, tipo_servicio, descripcion, costo) VALUES (3, 'Acuático', 'Excursión en catamarán', 800)
  INTO Servicio (id_servicio, tipo_servicio, descripcion, costo) VALUES (4, 'Alojamiento', 'Hotel 3 estrellas por 3 noches', 1500)
  INTO Servicio (id_servicio, tipo_servicio, descripcion, costo) VALUES (5, 'Tour', 'Tour guiado por lugares turísticos', 400)
SELECT * FROM dual;

INSERT ALL
  INTO Paquete (id_paquete, nombre_paquete, descripcion) VALUES (1, 'Paquete Caribe', 'Paquete completo Caribe con vuelo, hotel y tour')
  INTO Paquete (id_paquete, nombre_paquete, descripcion) VALUES (2, 'Paquete Aventura', 'Tour de aventura y actividades acuáticas')
  INTO Paquete (id_paquete, nombre_paquete, descripcion) VALUES (3, 'Paquete Cultural', 'Visitas culturales y gastronomía local')
  INTO Paquete (id_paquete, nombre_paquete, descripcion) VALUES (4, 'Paquete Relax', 'Descanso en hotel con spa y alimentación')
  INTO Paquete (id_paquete, nombre_paquete, descripcion) VALUES (5, 'Paquete Familiar', 'Paquete ideal para familias con niños')
SELECT * FROM dual;


INSERT ALL
  INTO Paquete_Servicio (id_paquete, id_servicio, cantidad) VALUES (1, 1, 1)
  INTO Paquete_Servicio (id_paquete, id_servicio, cantidad) VALUES (1, 4, 3)
  INTO Paquete_Servicio (id_paquete, id_servicio, cantidad) VALUES (1, 5, 1)
  INTO Paquete_Servicio (id_paquete, id_servicio, cantidad) VALUES (2, 2, 1)
  INTO Paquete_Servicio (id_paquete, id_servicio, cantidad) VALUES (2, 3, 1)
  INTO Paquete_Servicio (id_paquete, id_servicio, cantidad) VALUES (2, 5, 1)
  INTO Paquete_Servicio (id_paquete, id_servicio, cantidad) VALUES (3, 2, 1)
  INTO Paquete_Servicio (id_paquete, id_servicio, cantidad) VALUES (3, 5, 1)
  INTO Paquete_Servicio (id_paquete, id_servicio, cantidad) VALUES (4, 4, 2)
  INTO Paquete_Servicio (id_paquete, id_servicio, cantidad) VALUES (4, 5, 1)
  INTO Paquete_Servicio (id_paquete, id_servicio, cantidad) VALUES (5, 2, 1)
  INTO Paquete_Servicio (id_paquete, id_servicio, cantidad) VALUES (5, 4, 3)
  INTO Paquete_Servicio (id_paquete, id_servicio, cantidad) VALUES (5, 5, 2)
SELECT * FROM dual;

INSERT ALL
  INTO Compra (id_compra, id_cliente, id_empleado, fecha_compra, total) VALUES (1, 1, 1, DATE '2023-11-01', 4900)
  INTO Compra (id_compra, id_cliente, id_empleado, fecha_compra, total) VALUES (2, 2, 1, DATE '2023-11-02', 2300)
  INTO Compra (id_compra, id_cliente, id_empleado, fecha_compra, total) VALUES (3, 3, 2, DATE '2023-11-03', 1900)
  INTO Compra (id_compra, id_cliente, id_empleado, fecha_compra, total) VALUES (4, 1, 3, DATE '2023-12-01', 3200)
  INTO Compra (id_compra, id_cliente, id_empleado, fecha_compra, total) VALUES (5, 4, 1, DATE '2023-12-05', 2700)
SELECT * FROM dual;


INSERT ALL
  INTO Compra_Paquete (id_compra, id_paquete, cantidad) VALUES (1, 1, 1)
  INTO Compra_Paquete (id_compra, id_paquete, cantidad) VALUES (2, 2, 1)
  INTO Compra_Paquete (id_compra, id_paquete, cantidad) VALUES (3, 3, 1)
  INTO Compra_Paquete (id_compra, id_paquete, cantidad) VALUES (4, 4, 1)
  INTO Compra_Paquete (id_compra, id_paquete, cantidad) VALUES (5, 5, 1)
SELECT * FROM dual;

INSERT ALL
  INTO Medio_Pago (id_medio_pago, tipo_medio) VALUES (1, 'Tarjeta Crédito')
  INTO Medio_Pago (id_medio_pago, tipo_medio) VALUES (2, 'Tarjeta Débito')
  INTO Medio_Pago (id_medio_pago, tipo_medio) VALUES (3, 'Efectivo')
  INTO Medio_Pago (id_medio_pago, tipo_medio) VALUES (4, 'Transferencia')
  INTO Medio_Pago (id_medio_pago, tipo_medio) VALUES (5, 'PayPal')
SELECT * FROM dual;

INSERT ALL
  INTO Cuota (id_cuota, id_compra, id_medio_pago, fecha_pago, monto) VALUES (1, 1, 1, DATE '2023-11-01', 2500)
  INTO Cuota (id_cuota, id_compra, id_medio_pago, fecha_pago, monto) VALUES (2, 1, 2, DATE '2023-11-10', 2400)
  INTO Cuota (id_cuota, id_compra, id_medio_pago, fecha_pago, monto) VALUES (3, 2, 3, DATE '2023-11-02', 2300)
  INTO Cuota (id_cuota, id_compra, id_medio_pago, fecha_pago, monto) VALUES (4, 3, 4, DATE '2023-11-03', 1900)
  INTO Cuota (id_cuota, id_compra, id_medio_pago, fecha_pago, monto) VALUES (5, 4, 1, DATE '2023-12-01', 3200)
  INTO Cuota (id_cuota, id_compra, id_medio_pago, fecha_pago, monto) VALUES (6, 5, 5, DATE '2023-12-05', 2700)
SELECT * FROM dual;

SELECT mp.tipo_medio,
       COUNT(c.id_medio_pago) AS veces_utilizado
FROM Cuota c
JOIN Medio_Pago mp ON mp.id_medio_pago = c.id_medio_pago
GROUP BY mp.tipo_medio
ORDER BY veces_utilizado DESC;

SELECT e.nombre_completo AS empleado,
       COUNT(cp.id_paquete) AS paquetes_vendidos
FROM Empleado e
JOIN Compra co ON co.id_empleado = e.id_empleado
JOIN Compra_Paquete cp ON cp.id_compra = co.id_compra
GROUP BY e.nombre_completo
ORDER BY paquetes_vendidos DESC;

SELECT SUM(total) AS total_ventas
FROM Compra
WHERE fecha_compra BETWEEN DATE '2023-11-01'
                      AND DATE '2023-12-31';      

                
SELECT e.nombre_completo AS empleado,
       c.nombre_cargo AS cargo,
       ec.fecha_inicio,
       ec.fecha_fin
FROM Empleado_Cargo ec
JOIN Empleado e ON e.id_empleado = ec.id_empleado
JOIN Cargo c ON c.id_cargo = ec.id_cargo
ORDER BY e.nombre_completo, ec.fecha_inicio;

SELECT cl.nombre_completo AS cliente,
       COUNT(co.id_compra) AS compras_realizadas
FROM Cliente cl
JOIN Compra co ON co.id_cliente = cl.id_cliente
GROUP BY cl.nombre_completo
ORDER BY compras_realizadas DESC;
