using Venta_Computadores;


class Program
{
    static List<Compra> compras = new List<Compra>();
    static List<Producto> productos = new List<Producto>();
    static List<Usuario> usuarios = new List<Usuario>();
    static List<HistorialCompra> historial = new List<HistorialCompra>();
    static int ValidarOpcion()
    {
        int opcion;
        bool isValid;

        do
        {
            Console.Write("Digite su opción: ");
            string? input = Console.ReadLine();
            isValid = int.TryParse(input, out opcion); // Intentamos convertir la entrada

            if (!isValid || opcion < 0 || opcion > 2) // Si no es válido o no está en el rango permitido
            {
                Console.WriteLine("Opción no válida. Por favor, ingrese un número entre 0 y 2.");
            }
        } while (!isValid || opcion < 0 || opcion > 2); // Continuar pidiendo hasta que la opción sea válida

        return opcion; // Retorna la opción válida
    }
    static int ValidarOpciones()
    {
        int opciones;
        bool isValid;

        do
        {
            Console.Write("Digite su opción: ");
            string? input = Console.ReadLine();
            isValid = int.TryParse(input, out opciones); // Intentamos convertir la entrada

            if (!isValid || opciones < 0 || opciones > 6) // Si no es válido o no está en el rango permitido
            {
                Console.WriteLine("Opción no válida. Por favor, ingrese un número entre 0 y 6.");
            }
        } while (!isValid || opciones < 0 || opciones > 6); // Continuar pidiendo hasta que la opción sea válida

        return opciones; // Retorna la opción válida
    }
    static string LeerClave()
    {
        string clave = "";
        while (true)
        {
            var tecla = Console.ReadKey(true); // lee la tecla sin mostrarla
            if (tecla.Key == ConsoleKey.Enter) // cuando se presiona Enter, termina la lectura
            {
                break;
            }
            else if (tecla.Key == ConsoleKey.Backspace && clave.Length > 0) // soporte para borrar la última tecla
            {
                clave = clave.Substring(0, clave.Length - 1);
                Console.Write("\b \b"); // borrar en la consola
            }
            else
            {
                clave += tecla.KeyChar; // agregar la tecla al valor de la clave
                Console.Write("*"); // mostrar un asterisco como marcador
            }
        }
        Console.WriteLine(); // para mover el cursor a la siguiente línea
        return clave;
    }
        static void Main(string[] args)
        {
            int opcion;
            do
            {
                Console.Clear();
                Console.WriteLine("Bienvenido a el sistema Venta de computadores");
                Console.WriteLine("Seleccione una opcion: ");
                Console.WriteLine("1. Ingresar");
                Console.WriteLine("2. Crear usuario");
                Console.WriteLine("0. Cerrar sistema");
                opcion = ValidarOpcion();
                switch (opcion)
                {
                    case 1:
                        Console.Clear();
                        Console.WriteLine("Ingrese su correo electronico: ");
                        string correo1 = Console.ReadLine()!.Trim();
                        Console.WriteLine("Ingrese su clave");                        
                        string clave1 = LeerClave().Trim();
                        Usuario usuarioEncontrado = usuarios.Find(u => u.correo.Equals(correo1, StringComparison.OrdinalIgnoreCase) && u.clave == clave1)!;

                    if (usuarioEncontrado != null)
                    {
                        Console.WriteLine("Bienvenido, " + usuarioEncontrado.correo);
                        int opciones;
                        do
                        {
                            Console.Clear();
                            Console.WriteLine("Bienvenido usuario " + correo1);
                            Console.WriteLine("MENÚ");
                            Console.WriteLine("1. Crear productos");
                            Console.WriteLine("2. Ver catalogo de productos");
                            Console.WriteLine("3. Eliminar productos");
                            Console.WriteLine("4. Hacer compra");
                            Console.WriteLine("5. Eliminar compra");
                            Console.WriteLine("6. Ver historial de compras");
                            Console.WriteLine("0. Cerrar sistema");
                            opciones = ValidarOpciones();
                            switch (opciones)
                            {
                                case 1:
                                    Crear();
                                    break;

                                case 2:
                                    Ver();
                                    break;

                                case 3:
                                    Eliminar();
                                    break;

                                case 4:
                                    HacerCompra(usuarioEncontrado);
                                    break;

                                case 5:
                                    EliminarCompra(usuarioEncontrado);
                                    break;

                                case 6:
                                    VerHistorialCompras(usuarioEncontrado);
                                    break;
                            }
                        } while (opciones != 0);
                          Console.WriteLine("regresando al Menu principal");
                          Console.WriteLine("presione cualquier tecla");
                    }
                    else
                    {
                        Console.WriteLine("Correo o clave incorrectos. Intente de nuevo.");
                    }
                    
                    break;
                    case 2:
                        Console.Clear();
                        Console.WriteLine("Ingrese su correo electronico: ");
                        string correoC = Console.ReadLine()!;
                        Console.WriteLine("Ingrese su clave");                   
                        string claveC = LeerClave();
                        Usuario usuario1 = new Usuario(correoC, claveC);
                        usuarios.Add(usuario1);
                        Console.WriteLine("usuario creado con éxito.");
                        Console.WriteLine("se creo el usuario " + correoC);
                        Console.WriteLine("-------------------------------------------");
                        break;
                }
                Console.ReadKey();

            } while (opcion != 0);
        }
    public static void Crear()
    {
        Console.Clear();
        Console.Write("Ingrese el ID del producto: ");
        int id = Convert.ToInt32(Console.ReadLine());
        Console.Write("Ingrese el nombre del producto: ");
        string nombre = Console.ReadLine()!;
        Console.Write("Ingrese el precio: ");
        int precio = Convert.ToInt32(Console.ReadLine());
        Console.Write("Ingrese la cantidad del producto: ");
        int cantidad = Convert.ToInt32(Console.ReadLine());
        Producto producto1 = new Producto(id, nombre, precio, cantidad);
        productos.Add(producto1);
        Console.WriteLine("Producto creado con éxito.");
        Console.WriteLine(producto1);
        Console.WriteLine("-------------------------------------------");
        Console.ReadKey();
    }
    public static void Ver()
    {
        Console.Clear();
        Console.WriteLine("Catalogo de productos:");
        foreach (var product in productos)
        {
            Console.WriteLine(product);
            Console.WriteLine("-------------------------------------------");
            Console.WriteLine("");
        }
        Console.ReadKey();
    }
    public static void Eliminar()
    {
        Console.Clear();
        Console.Write("Ingrese el ID del producto a eliminar: ");
        int idDe = Convert.ToInt32(Console.ReadLine());
        var producE = productos.Find(p => p.id == idDe);

        if (producE != null)
        {
            productos.Remove(producE);
            Console.WriteLine("Producto eliminado con éxito.");
        }
        else
        {
            Console.WriteLine("Producto no encontrado.");
        }
        Console.ReadKey();
    }
    public static void HacerCompra(Usuario usuario)
    {
        Console.Clear();
        Console.WriteLine("Seleccione los productos a comprar:");
        List<Producto> productosSeleccionados = new List<Producto>();
        decimal totalCompra = 0m;  // Variable para almacenar el precio total de la compra
        Console.WriteLine("presiona una tecla para hacer compra");
        // Mostrar productos disponibles
        Ver();

        // Seleccionar productos
        bool seguirComprando = true;
        while (seguirComprando)
        {
            Console.Write("Ingrese el ID del producto que desea comprar (0 para finalizar): ");
            int idProducto = Convert.ToInt32(Console.ReadLine());
            if (idProducto == 0) break;

            var productoSeleccionado = productos.Find(p => p.id == idProducto);
            if (productoSeleccionado != null)
            {
                // Verificar cantidad disponible
                Console.Write($"¿Cuántas unidades de {productoSeleccionado.nombre} desea comprar? ");
                int cantidad = Convert.ToInt32(Console.ReadLine());

                if (cantidad > 0 && cantidad <= productoSeleccionado.cantidad)
                {
                    // Agregar el producto y la cantidad al carrito
                    productosSeleccionados.Add(productoSeleccionado);
                    totalCompra += productoSeleccionado.precio * cantidad;

                    // Restar la cantidad comprada del inventario del producto
                    productoSeleccionado.cantidad -= cantidad;

                    Console.WriteLine($"Producto {productoSeleccionado.nombre} x{cantidad} agregado al carrito.");
                }
                else
                {
                    Console.WriteLine("Cantidad no válida o no disponible.");
                }
            }
            else
            {
                Console.WriteLine("Producto no encontrado.");
            }

            // Preguntar si quiere seguir comprando
            Console.Write("¿Desea agregar otro producto? (s/n): ");
            char respuesta = Console.ReadKey(true).KeyChar;
            seguirComprando = respuesta == 's' || respuesta == 'S';
            Console.WriteLine("");
        }

        // Crear compra
        if (productosSeleccionados.Count > 0)
        {
            // Mostrar precio total
            Console.WriteLine($"Total a pagar: {totalCompra:C}");

            // Preguntar si el usuario confirma la compra
            Console.Write("¿Desea confirmar la compra? (s/n): ");
            char confirmar = Console.ReadKey(true).KeyChar;
            if (confirmar == 's' || confirmar == 'S')
            {
                Compra nuevaCompra = new Compra(usuario, productosSeleccionados, DateTime.Now, totalCompra);
                compras.Add(nuevaCompra);

                // Agregar al historial del usuario
                HistorialCompra historialCompra = new HistorialCompra(productosSeleccionados, totalCompra);
                usuario.HistorialCompras.Add(historialCompra);

                Console.WriteLine("\nCompra realizada con éxito.");
            }
            else
            {
                Console.WriteLine("\nCompra cancelada.");
            }
        }
        else
        {
            Console.WriteLine("No se seleccionaron productos para comprar.");
        }

        Console.ReadKey();
    }
    public static void EliminarCompra(Usuario usuario)
    {
        Console.Clear();
        Console.WriteLine("Historial de compras:");
        for (int i = 0; i < usuario.HistorialCompras.Count; i++)
        {
            Console.WriteLine($"{i + 1}. {usuario.HistorialCompras[i]}");
        }

        Console.Write("Ingrese el número de la compra a eliminar (0 para cancelar): ");
        int numCompra = Convert.ToInt32(Console.ReadLine()) - 1;

        if (numCompra >= 0 && numCompra < usuario.HistorialCompras.Count)
        {
            usuario.HistorialCompras.RemoveAt(numCompra);
            Console.WriteLine("Compra eliminada con éxito.");
        }
        else if (numCompra == -1)
        {
            Console.WriteLine("Operación cancelada.");
        }
        else
        {
            Console.WriteLine("Opracion no válida.");
        }

        Console.ReadKey();
    }
    public static void VerHistorialCompras(Usuario usuario)
    {
        Console.Clear();
        Console.WriteLine("Historial de compras:");
        foreach (var historial in usuario.HistorialCompras)
        {
            Console.WriteLine(historial);
        }
        Console.ReadKey();
    }
}