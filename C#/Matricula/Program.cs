/*Una universidad requiere analizar el proceso de matrícula para el tercer período académico del 2020 de cada uno de los estudiantes. 
La universidad consta de cinco (5) programas académicos. Cada programa académico tiene un número de créditos asociados. 
El valor de cada crédito académico es de $200.000. 
 
La siguiente Tabla muestra cada uno de los programas académicos con su número de créditos. 
Adicionalmente, muestra el descuento que se le puede aplicar al estudiante si realiza el pago en Efectivo. 
Por ejemplo, si el estudiante va a estudiar Administración de Empresas y paga en Efectivo, 
entonces se le aplica un descuento del 15%. Si paga en línea, NO se le aplica el descuento. 
 
Las dos formas de pago que acepta la universidad son Efectivo y pago en línea. 

Programas Académicos 	Nro. de Créditos por período académico 	 
Descuentos 
Ingeniería de sistemas  	20 	18% 
Psicología              	16 	12% 
Economía 	                18 	10% 
Comunicación Social 	    18 	 5% 
Administración de Empresas 	20 	15% 
 
Se requiere desarrollar una solución básica de programación que permita matricular un número X de estudiantes. 
Al finalizar, la solución de programación debe mostrar los siguientes resultados: 
•	Cantidad de estudiantes inscritos por programa académico. 
•	Total, de créditos inscritos en el tercer período académico del 2020. 
•	Valor total pagado por los estudiantes sin tener en cuenta el descuento. 
•	Valor total de descuentos aplicados por la universidad a los estudiantes. 
•	Valor neto de las inscripciones del primer semestre del 2020. 

  codigo fuente autoria propia
 */
class Program
{
    static Dictionary<int, Dictionary<string, object>> programasAcademicos = new Dictionary<int, Dictionary<string, object>>()
    {
        {1, new Dictionary<string, object> { {"nombre", "Ingeniería de sistemas"},    {"creditos", 20}, {"descuento_efectivo", 0.18} } },
        {2, new Dictionary<string, object> { {"nombre", "Psicología"},                {"creditos", 16}, {"descuento_efectivo", 0.12} } },
        {3, new Dictionary<string, object> { {"nombre", "Economía"},                  {"creditos", 18}, {"descuento_efectivo", 0.10} } },
        {4, new Dictionary<string, object> { {"nombre", "Comunicación Social"},       {"creditos", 18}, {"descuento_efectivo", 0.05} } },
        {5, new Dictionary<string, object> { {"nombre", "Administración de Empresas"},{"creditos", 20}, {"descuento_efectivo", 0.15} } }
    };

    static void Main(string[] args)
    {
        Dictionary<int, int> estudiantesPorPrograma = new Dictionary<int, int>();
        foreach (int key in programasAcademicos.Keys)
        {
            estudiantesPorPrograma[key] = 0;
        }

        int totalCreditos = 0;
        int totalValorSinDescuento = 0;
        int totalDescuentos = 0;

        Console.WriteLine("Ingrese el número de estudiantes a matricular:");
        int numEstudiantes = Convert.ToInt32(Console.ReadLine());

        for (int i = 0; i < numEstudiantes; i++)
        {
            MostrarMenuProgramas();
            Console.WriteLine("Ingrese el número del programa académico:");
            int programaSeleccionado;
            while (!int.TryParse(Console.ReadLine(), out programaSeleccionado) || !programasAcademicos.ContainsKey(programaSeleccionado))
            {
                Console.WriteLine("Opcion inválida. Elija un número valido:");
            }

            MostrarMenuFormaPago();
            string formaPago;
            while (true)
            {
                string opcion = Console.ReadLine();
                if (opcion == "1")
                {
                    formaPago = "Efectivo";
                    break;
                }
                else if (opcion == "2")
                {
                    formaPago = "En línea";
                    break;
                }
                else
                {
                    Console.WriteLine("Opción inválida. Elija una opcion valida:");
                }
            }

            Dictionary<string, object> programa = programasAcademicos[programaSeleccionado];
            double descuento = CalcularDescuento((double)programa["descuento_efectivo"], formaPago);
            int creditos = (int)programa["creditos"];
            int valorSinDescuento = creditos * 200000;

            estudiantesPorPrograma[programaSeleccionado]++;
            totalCreditos += creditos;
            totalValorSinDescuento += valorSinDescuento;
            totalDescuentos += (int)(valorSinDescuento * descuento);
        }

        int valorNeto = totalValorSinDescuento - totalDescuentos;

        Console.WriteLine("\nResultados:");
        foreach (int key in estudiantesPorPrograma.Keys)
        {
            Console.WriteLine($"Estudiantes en {programasAcademicos[key]["nombre"]}: {estudiantesPorPrograma[key]}");
        }
        Console.WriteLine($"Total de créditos inscritos: {totalCreditos}");
        Console.WriteLine($"Valor total pagado sin descuento: ${totalValorSinDescuento:#,0}");
        Console.WriteLine($"Valor total de descuentos aplicados: ${totalDescuentos:#,0}");
        Console.WriteLine($"Valor neto de inscripciones: ${valorNeto:#,0}");
    }

    static void MostrarMenuProgramas()
    {
        Console.WriteLine("Seleccione el programa académico:");
        foreach (int key in programasAcademicos.Keys)
        {
            Console.WriteLine($"{key}. {programasAcademicos[key]["nombre"]}");
        }
    }

    static void MostrarMenuFormaPago()
    {
        Console.WriteLine("Seleccione la forma de pago:");
        Console.WriteLine("1. Efectivo");
        Console.WriteLine("2. En línea");
        Console.WriteLine("Ingrese el número de la forma de pago (1 para Efectivo, 2 para En línea):");
    }

    static double CalcularDescuento(double descuentoEfectivo, string formaPago)
    {
        if (formaPago == "Efectivo")
        {
            return descuentoEfectivo;
        }
        else
        {
            return 0;
        }
    }
}