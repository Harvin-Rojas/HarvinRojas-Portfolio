namespace Venta_Computadores
{
    class Usuario
    {
        

        public  string correo { get; set; }
        public string clave { get; set; }
        public List<HistorialCompra> HistorialCompras { get; set; }

        public Usuario(string correo, string clave)
        {
            this.correo = correo;
            this.clave = clave;
            HistorialCompras = new List<HistorialCompra>();
        }

    }
}