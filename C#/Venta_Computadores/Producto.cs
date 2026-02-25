namespace Venta_Computadores
{
    class Producto
    {
        public int id { get; set; }
        public string nombre { get; set; }
        public int precio { get; set; }
        public int cantidad { get; set; }

        public Producto(int id, string nombre, int precio, int cantidad)
        {
            this.id = id;
            this.nombre = nombre;
            this.precio = precio;
            this.cantidad = cantidad;
        }

        public override string ToString()
        {
            return $"ID: {id},\nNombre: {nombre},\nPrecio: {precio}\nCantidad: {cantidad}";
        }

       
    }
}