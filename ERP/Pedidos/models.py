from django.db import models

# Create your models here.
class Usuario(models.Model):
    user_name = models.CharField(max_length=100, verbose_name="Usuario")
    position = models.CharField(max_length=50, null=True, verbose_name="Cargo")

    def __str__(self):
        return f"{self.user_name} - {self.position}" 

class Cliente(models.Model):
    client_folio = models.FloatField(max_length=5, verbose_name="No.Cliente")
    client_name = models.CharField(max_length=100, verbose_name="Nombre del cliente")
    direction = models.TextField(max_length=150, verbose_name="Dirección")
    city = models.CharField(max_length=50, verbose_name="Ciudad")
    county = models.CharField(max_length=50, verbose_name="Municipio")
    postal_code = models.FloatField(max_length=5, verbose_name="Código postal")
    telephone_number = models.FloatField(max_length=10, verbose_name= "Número telefónico")
    email = models.EmailField(max_length=250, verbose_name= "Correo electrónico" )
    rfc = models.CharField(max_length=13, verbose_name="RFC")

    def __str__(self):
        return self.folio

class Producto(models.Model):
    product_code = models.CharField(max_length=10, verbose_name="Código de producto")
    product_category = models.CharField(max_length=50, verbose_name="Categoría del producto")
    product_name = models.CharField(max_length=150, verbose_name="Nombre del producto")
    product_image = models.ImageField(upload_to="imagen producto", null = True, blank = True, verbose_name= "Imagen de producto")

    def __str__(self):
        return self.product_code
    
def validate_minutes_only(value):
        if value.total_seconds() % 60 != 0:
            raise ValueError("La duración solo puede contener minutos enteros")

class Fichas_de_costos(models.Model):
    product_code_1= models.ForeignKey(Producto, on_delete=models.DO_NOTHING, verbose_name= "Código del producto")
    product_name_1= models.ForeignKey(Producto, on_delete=models.DO_NOTHING, verbose_name= "Nombre del producto")
    product_image_1= models.ForeignKey(Producto, on_delete=models.DO_NOTHING, verbose_name= "Imagen del producto")
    labor= models.DecimalField(max_digits=4, decimal_places=2, verbose_name="Mano de obra")
    prime_materia = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Materia Prima")
    prime_cost= models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Costo primo")
    indirect_minutes= models.DecimalField(max_digits=2, decimal_places=2, verbose_name="Indirectos por minuto")
    elaboration_minutes= models.DurationField(validators=[validate_minutes_only], verbose_name="Minutos de elaboración")
    indirect_costs= models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Costos indirectos")
    fabrication_cost= models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Costo de fabricación")
    utility= models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Utilidad")
    base_price= models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Precio base")
    dealer_price= models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Precio de distribuidor")
    f_price= models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Precio foráneo")

    def __str__(self):
        return self.product_code_1

class Materia_prima(models.Model):
    area = models.CharField(max_length=20, verbose_name="Área")
    parts = models.FloatField(max_length=2, verbose_name="Piezas")
    material = models.CharField(max_length=25, verbose_name="Material")
    desc_mp = models.TextField(max_length=100, verbose_name="Descripción")
    meas_mp = models.CharField(max_length=50, verbose_name="Medida")
    total_mp = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Total" )
    unit_price_mp = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Precio unitario")
    amount_mp = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Importe")

    def __str__(self):
        return self.area
    
def validate_minutes_only(value):
        if value.total_seconds() % 60 != 0:
            raise ValueError("La duración solo puede contener minutos enteros")
        
class Mano_de_obra(models.Model):
    activity = models.CharField(max_length=20, verbose_name="Actividad")
    quantity_mo = models.FloatField(max_length=2, verbose_name="Cantidad")
    time = models.DurationField(validators=[validate_minutes_only], verbose_name="Tiempo (min)")
    time_a = models.DurationField(validators=[validate_minutes_only], verbose_name="Tiempo por actividad")
    cost = models.DecimalField(max_digits=2, decimal_places=2,verbose_name="Costo")
    amount_mo = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Importe")

    def __str__(self):
        return self.activity
    
class Lista_de_precios(models.Model):
    product_code_2 = models.ForeignKey(Producto, on_delete=models.DO_NOTHING, verbose_name="Código del producto")
    product_category_1 = models.ForeignKey(Producto, on_delete=models.DO_NOTHING, verbose_name="Categoría del producto")
    product_name_2 = models.ForeignKey(Producto, on_delete=models.DO_NOTHING, verbose_name="Nombre del producto")
    base_price_1 = models.ForeignKey(Fichas_de_costos, on_delete=models.DO_NOTHING, verbose_name="Precio base")
    dealer_price_1 = models.ForeignKey(Fichas_de_costos, on_delete=models.DO_NOTHING, verbose_name="Precio de distribuidor")
    f_price_1 = models.ForeignKey(Fichas_de_costos, on_delete=models.DO_NOTHING, verbose_name="Precio froráneo")
    product_image_2 = models.ForeignKey(Producto, on_delete=models.DO_NOTHING, verbose_name="Imagen de producto")

    def __str__(self):
        return self.product_code_2
   
class Hoja_de_Presupuesto(models.Model):
    folio_pres = models.FloatField(max_length=10, verbose_name="Folio de Presupuesto")
    budget = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Presupuesto")
    cliente_name1 = models.ForeignKey(Cliente, on_delete = models.DO_NOTHING, verbose_name="Cliente" )
    client_folio1 = models.ForeignKey(Cliente, on_delete = models.DO_NOTHING, verbose_name="No.Cliente")
    date_of_quotation = models.DateField(auto_now_add = True, verbose_name="Fecha de cotización")
    rfc_1 = models.ForeignKey(Cliente, on_delete= models.DO_NOTHING, verbose_name="RFC")
    direction_1 = models.ForeignKey(Cliente, on_delete= models.DO_NOTHING, verbose_name="Dirección")
    city_1 = models.ForeignKey(Cliente, on_delete= models.DO_NOTHING, verbose_name="Ciudad")
    county_1 = models.ForeignKey(Cliente,on_delete= models.DO_NOTHING, verbose_name="Municipio")
    postal_code_1 = models.ForeignKey(Cliente,on_delete= models.DO_NOTHING, verbose_name="Código postal")
    telephone_number_1 = models.ForeignKey(Cliente,on_delete= models.DO_NOTHING, verbose_name="Número telefónico")
    email_1 = models.ForeignKey(Cliente,on_delete= models.DO_NOTHING, verbose_name="Correo electrónico")
    category = models.FloatField(max_length=3, verbose_name="Partida")
    quantity = models.FloatField(max_length=5, verbose_name="Cantidad")
    product_code_3 = models.ForeignKey(Producto, on_delete= models.DO_NOTHING, verbose_name="Código de producto")
    description = models.TextField(max_length=500, verbose_name="Descripción")
    measurement = models.CharField(max_length=100, verbose_name="Unidad")
    unit_price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Precio unitario")
    amount = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Importe")
    product_image_3 = models.ForeignKey(Producto, on_delete= models.DO_NOTHING, verbose_name="Imagen de producto")
    sub_total = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Sub-total")
    total = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Total")
    observations = models.TextField(max_length=500, verbose_name="Observaciones")
    
    def __str__(self):
        return self.folio_pres

class Archivo_de_presupuestos(models.Model):
    folio_de_pres = models.ForeignKey(Hoja_de_Presupuesto, on_delete=models.DO_NOTHING, verbose_name = "Folio de presupuesto")
    date_of_elaboration = models.ForeignKey(Hoja_de_Presupuesto,on_delete=models.DO_NOTHING, verbose_name = "Fecha")
    archive_document = models.FileField(upload_to="uploads/", verbose_name = "Archivo almacenado")

    def __str__(self):
        return self.folio_de_pres

class Orden_de_pedido(models.Model):
    folio_de_ped = models.FloatField(max_length=10, verbose_name="Folio de pedido")
    date_of_order = models.DateField(auto_now_add = True, verbose_name="Fecha de pedido")
    date_of_delivery = models.DateField(auto_now_add = True, verbose_name="Fecha de entrega")
    no_of_bill = models.FloatField(max_length=25, verbose_name="No. de factura")
    client_name_2 = models.ForeignKey(Cliente, on_delete = models.DO_NOTHING, verbose_name = "Nombre del cliente")
    email_2 = models.ForeignKey(Cliente, on_delete = models.DO_NOTHING,verbose_name = "Correo electrónico")
    direction_2 = models.ForeignKey(Cliente, on_delete = models.DO_NOTHING, verbose_name = "Dirección")
    city_2 = models.ForeignKey(Cliente, on_delete = models.DO_NOTHING, verbose_name="Ciudad")
    county_2 = models.ForeignKey(Cliente, on_delete = models.DO_NOTHING, verbose_name="Municipio")
    postal_code_2 = models.ForeignKey(Cliente, on_delete = models.DO_NOTHING, verbose_name="Código Postal")
    rfc_2 = models.ForeignKey(Cliente, on_delete = models.DO_NOTHING, verbose_name="RFC")
    place_of_delivery = models.CharField(max_length=50, verbose_name="Lugar de entrega")
    conditions = models.TextField(max_length=500, verbose_name="Condiciones de entrega")
    down_payment = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Anticipo")
    balance = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Saldo")
    amount_of_product = models.FloatField(max_length=3, verbose_name="Cantidad")
    product_code_4 = models.ForeignKey(Producto, on_delete = models.DO_NOTHING, verbose_name="Código de Producto")
    description_ped = models.TextField(max_length=500, verbose_name="Descripción")
    unit_price_ped = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Precio unitario")
    mesuarement_ped = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Importe")
    product_image_4 = models.ForeignKey(Producto, on_delete= models.DO_NOTHING, verbose_name="Imagen de producto")
    sub_totalped = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Sub-total")
    total_ped = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Total")
    observations_ped = models.TextField(max_length=500, verbose_name="Observaciones")

    def __str__(self):
        return self.folio_de_ped

class Archivo_de_pedidos(models.Model):
    folio_ap = models.ForeignKey(Orden_de_pedido, on_delete=models.DO_NOTHING, verbose_name = "Folio de pedido")
    date_of_ped = models.ForeignKey(Hoja_de_Presupuesto,on_delete=models.DO_NOTHING, verbose_name = "Fecha")
    document_archive = models.FileField(upload_to="uploads/", verbose_name = "Archivo almacenado")

    def __str__(self):
        return self.folio_ap

class control_cuentas(models.Model):
    client_folio2 = models.ForeignKey(Cliente, on_delete = models.DO_NOTHING, verbose_name= "No.Cliente")
    client_name_3 = models.ForeignKey(Cliente, on_delete = models.DO_NOTHING, verbose_name= "Nombre del cliente")
    date_of_advance = models.DateField(auto_now_add= True, verbose_name = "Fecha") 
    concept = models.CharField(max_length=50, verbose_name="Concepto")
    down_payment1 = models.ForeignKey(Orden_de_pedido, on_delete = models.DO_NOTHING, verbose_name= "Anticipo")
    balance1 = models.ForeignKey(Orden_de_pedido, on_delete = models.DO_NOTHING, verbose_name= "Saldo")
    total_dp = models.DecimalField(max_digits=8, decimal_places=2, verbose_name= "Total anticipo")
    balance_total = models.DecimalField(max_digits=8, decimal_places=2, verbose_name= "Total Saldo")

    def __str__(self):
        return self.client_folio2

class Orden_de_produccion (models.Model):
    folio_order = models.FloatField(max_length=10, verbose_name= "Folio de orden de producción")
    date_product = models.DateField(auto_now_add= True, verbose_name= "Fecha")
    folio_de_ped1 = models.ForeignKey(Orden_de_pedido, on_delete=models.DO_NOTHING, verbose_name="No. de Pedido")
    date_of_delivery1 = models.ForeignKey(Orden_de_pedido, on_delete=models.DO_NOTHING, verbose_name=" Fecha de entrega")
    place_of_delivery1 = models.ForeignKey(Orden_de_pedido, on_delete=models.DO_NOTHING, verbose_name="Lugar de entrega")
    amount_of_product1 = models.ForeignKey(Orden_de_pedido, on_delete=models.DO_NOTHING, verbose_name="Cantidad")
    product_code_5 = models.ForeignKey(Producto, on_delete=models.DO_NOTHING, verbose_name="Código de producto")
    description_ped_1 =  models.ForeignKey(Orden_de_pedido, on_delete=models.DO_NOTHING, verbose_name="Descripción")
    specs = models.TextField(max_length=500, verbose_name="Especificaciones")
    product_image_5 = models.ForeignKey(Producto, on_delete= models.DO_NOTHING, verbose_name="Imagen del producto")

    def __str__(self):
        return self.folio_order

class Archivo_de_producción(models.Model):
    folio_order1 = models.ForeignKey(Orden_de_produccion, on_delete=models.DO_NOTHING, verbose_name = "Folio de orden de producción")
    date_product1 = models.ForeignKey(Orden_de_produccion,on_delete=models.DO_NOTHING, verbose_name = "Fecha")
    document_archive1 = models.FileField(upload_to="uploads/", verbose_name = "Archivo almacenado")

    def __str__(self):
        return self.folio_order1