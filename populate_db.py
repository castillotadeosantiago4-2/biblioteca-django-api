"""
Script para poblar la base de datos con datos de prueba
Ejecutar con: python populate_db.py
"""
import os
import django
from datetime import date, timedelta
from decimal import Decimal

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'biblioteca_project.settings')
django.setup()

from django.contrib.auth.models import User
from django.utils import timezone
from libros.models import Autor, Categoria, Libro, Prestamo


def crear_usuarios():
    """Crear usuarios de prueba"""
    print("Creando usuarios...")
    
    # Crear superusuario si no existe
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser(
            username='admin',
            email='admin@biblioteca.com',
            password='admin123',
            first_name='Administrador',
            last_name='Sistema'
        )
        print("  ✓ Superusuario 'admin' creado (password: admin123)")
    
    # Crear usuarios normales
    usuarios_data = [
        {'username': 'juan_perez', 'email': 'juan@email.com', 'first_name': 'Juan', 'last_name': 'Pérez'},
        {'username': 'maria_lopez', 'email': 'maria@email.com', 'first_name': 'María', 'last_name': 'López'},
        {'username': 'carlos_ruiz', 'email': 'carlos@email.com', 'first_name': 'Carlos', 'last_name': 'Ruiz'},
        {'username': 'ana_torres', 'email': 'ana@email.com', 'first_name': 'Ana', 'last_name': 'Torres'},
        {'username': 'luis_ramos', 'email': 'luis@email.com', 'first_name': 'Luis', 'last_name': 'Ramos'},
    ]
    
    for user_data in usuarios_data:
        if not User.objects.filter(username=user_data['username']).exists():
            User.objects.create_user(
                password='user123',
                **user_data
            )
            print(f"  ✓ Usuario '{user_data['username']}' creado")


def crear_autores():
    """Crear autores de prueba"""
    print("\nCreando autores...")
    
    # Obtener usuario admin para creado_por
    admin_user = User.objects.get(username='admin')
    
    autores_data = [
        {
            'nombre': 'Gabriel',
            'apellido': 'García Márquez',
            'fecha_nacimiento': date(1927, 3, 6),
            'pais_origen': 'Colombia',
            'biografia': 'Premio Nobel de Literatura 1982. Autor de Cien años de soledad.',
            'foto': 'https://ejemplo.com/fotos/gabriel_garcia_marquez.jpg'
        },
        {
            'nombre': 'Isabel',
            'apellido': 'Allende',
            'fecha_nacimiento': date(1942, 8, 2),
            'pais_origen': 'Chile',
            'biografia': 'Una de las novelistas más leídas en español. Autora de La casa de los espíritus.',
            'foto': 'https://ejemplo.com/fotos/isabel_allende.jpg'
        },
        {
            'nombre': 'Jorge Luis',
            'apellido': 'Borges',
            'fecha_nacimiento': date(1899, 8, 24),
            'pais_origen': 'Argentina',
            'biografia': 'Uno de los escritores más importantes del siglo XX en lengua española.',
            'foto': 'https://ejemplo.com/fotos/jorge_luis_borges.jpg'
        },
        {
            'nombre': 'Octavio',
            'apellido': 'Paz',
            'fecha_nacimiento': date(1914, 3, 31),
            'pais_origen': 'México',
            'biografia': 'Premio Nobel de Literatura 1990. Ensayista y poeta mexicano.',
            'foto': 'https://ejemplo.com/fotos/octavio_paz.jpg'
        },
        {
            'nombre': 'Mario',
            'apellido': 'Vargas Llosa',
            'fecha_nacimiento': date(1936, 3, 28),
            'pais_origen': 'Perú',
            'biografia': 'Premio Nobel de Literatura 2010. Autor de La ciudad y los perros.',
            'foto': 'https://ejemplo.com/fotos/mario_vargas_llosa.jpg'
        },
        {
            'nombre': 'Julio',
            'apellido': 'Cortázar',
            'fecha_nacimiento': date(1914, 8, 26),
            'pais_origen': 'Argentina',
            'biografia': 'Escritor argentino, uno de los grandes innovadores del cuento y la prosa del siglo XX.',
            'foto': 'https://ejemplo.com/fotos/julio_cortazar.jpg'
        },
        {
            'nombre': 'Laura',
            'apellido': 'Esquivel',
            'fecha_nacimiento': date(1950, 9, 30),
            'pais_origen': 'México',
            'biografia': 'Escritora mexicana, autora de "Como agua para chocolate".',
            'foto': 'https://ejemplo.com/fotos/laura_esquivel.jpg'
        },
        {
            'nombre': 'Roberto',
            'apellido': 'Bolaño',
            'fecha_nacimiento': date(1953, 4, 28),
            'pais_origen': 'Chile',
            'biografia': 'Escritor chileno, autor de "Los detectives salvajes" y "2666".',
            'foto': 'https://ejemplo.com/fotos/roberto_bolano.jpg'
        },
        {
            'nombre': 'Elena',
            'apellido': 'Poniatowska',
            'fecha_nacimiento': date(1932, 5, 19),
            'pais_origen': 'México',
            'biografia': 'Periodista y escritora mexicana, Premio Cervantes 2013.',
            'foto': 'https://ejemplo.com/fotos/elena_poniatowska.jpg'
        },
        {
            'nombre': 'Manuel',
            'apellido': 'Puig',
            'fecha_nacimiento': date(1932, 12, 28),
            'pais_origen': 'Argentina',
            'biografia': 'Escritor argentino, autor de "El beso de la mujer araña".',
            'foto': 'https://ejemplo.com/fotos/manuel_puig.jpg'
        },
    ]
    
    for autor_data in autores_data:
        autor, created = Autor.objects.get_or_create(
            nombre=autor_data['nombre'],
            apellido=autor_data['apellido'],
            defaults=autor_data
        )
        if created:
            print(f"  ✓ Autor '{autor.nombre_completo}' creado (País: {autor.pais_origen})")


def crear_categorias():
    """Crear categorías de prueba"""
    print("\nCreando categorías...")
    
    categorias_data = [
        {'nombre': 'Ficción', 'descripcion': 'Novelas y cuentos de ficción literaria', 'activo': True},
        {'nombre': 'Fantasía', 'descripcion': 'Literatura fantástica y de mundos imaginarios', 'activo': True},
        {'nombre': 'Ciencia Ficción', 'descripcion': 'Narrativa especulativa y futurista', 'activo': True},
        {'nombre': 'Romance', 'descripcion': 'Novelas románticas y de amor', 'activo': True},
        {'nombre': 'Misterio', 'descripcion': 'Novelas policiacas y de suspenso', 'activo': True},
        {'nombre': 'Terror', 'descripcion': 'Literatura de horror y terror', 'activo': True},
        {'nombre': 'Aventura', 'descripcion': 'Historias de aventuras y acción', 'activo': True},
        {'nombre': 'Historia', 'descripcion': 'Libros de historia y biografías', 'activo': True},
        {'nombre': 'Poesía', 'descripcion': 'Obras poéticas y antologías', 'activo': True},
        {'nombre': 'Ensayo', 'descripcion': 'Ensayos literarios y filosóficos', 'activo': True},
        {'nombre': 'Infantil', 'descripcion': 'Libros para niños y jóvenes', 'activo': True},
        {'nombre': 'Autoayuda', 'descripcion': 'Libros de desarrollo personal y superación', 'activo': True},
    ]
    
    for categoria_data in categorias_data:
        categoria, created = Categoria.objects.get_or_create(
            nombre=categoria_data['nombre'],
            defaults=categoria_data
        )
        if created:
            estado = "activa" if categoria.activo else "inactiva"
            print(f"  ✓ Categoría '{categoria.nombre}' creada ({estado})")


def crear_libros():
    """Crear libros de prueba"""
    print("\nCreando libros...")
    
    # Obtener usuario admin para creado_por
    admin_user = User.objects.get(username='admin')
    
    # Obtener autores
    garcia_marquez = Autor.objects.get(apellido='García Márquez')
    allende = Autor.objects.get(apellido='Allende')
    borges = Autor.objects.get(apellido='Borges')
    paz = Autor.objects.get(apellido='Paz')
    vargas_llosa = Autor.objects.get(apellido='Vargas Llosa')
    cortazar = Autor.objects.get(apellido='Cortázar')
    esquivel = Autor.objects.get(apellido='Esquivel')
    bolaño = Autor.objects.get(apellido='Bolaño')
    poniatowska = Autor.objects.get(apellido='Poniatowska')
    puig = Autor.objects.get(apellido='Puig')
    
    # Obtener categorías
    ficcion = Categoria.objects.get(nombre='Ficción')
    poesia = Categoria.objects.get(nombre='Poesía')
    ensayo = Categoria.objects.get(nombre='Ensayo')
    misterio = Categoria.objects.get(nombre='Misterio')
    historia = Categoria.objects.get(nombre='Historia')
    romance = Categoria.objects.get(nombre='Romance')
    terror = Categoria.objects.get(nombre='Terror')  # <-- Definir la variable terror
    
    libros_data = [
        {
            'titulo': 'Cien años de soledad',
            'subtitulo': 'Novela del realismo mágico',
            'isbn': '9780307474728',
            'autor': garcia_marquez,
            'categoria': ficcion,
            'editorial': 'Editorial Sudamericana',
            'fecha_publicacion': date(1967, 5, 30),
            'paginas': 471,
            'idioma': 'Español',
            'descripcion': 'Obra maestra del realismo mágico que narra la historia de la familia Buendía.',
            'imagen_portada': 'https://ejemplo.com/portadas/cien_anos.jpg',
            'stock': 5,
            'estado': Libro.DISPONIBLE,
            'precio': Decimal('450.00'),
            'valoracion': Decimal('4.85'),
            'activo': True,
            'creado_por': admin_user
        },
        {
            'titulo': 'El amor en los tiempos del cólera',
            'subtitulo': '',
            'isbn': '9780307387738',
            'autor': garcia_marquez,
            'categoria': ficcion,
            'editorial': 'Editorial Sudamericana',
            'fecha_publicacion': date(1985, 1, 1),
            'paginas': 368,
            'idioma': 'Español',
            'descripcion': 'Historia de amor que transcurre a lo largo de más de cincuenta años.',
            'imagen_portada': 'https://ejemplo.com/portadas/amor_colera.jpg',
            'stock': 3,
            'estado': Libro.DISPONIBLE,
            'precio': Decimal('380.00'),
            'valoracion': Decimal('4.70'),
            'activo': True,
            'creado_por': admin_user
        },
        {
            'titulo': 'La casa de los espíritus',
            'subtitulo': '',
            'isbn': '9788401242281',
            'autor': allende,
            'categoria': ficcion,
            'editorial': 'Planeta',
            'fecha_publicacion': date(1982, 1, 1),
            'paginas': 433,
            'idioma': 'Español',
            'descripcion': 'Saga familiar chilena que mezcla lo cotidiano con lo maravilloso.',
            'imagen_portada': 'https://ejemplo.com/portadas/casa_espiritus.jpg',
            'stock': 4,
            'estado': Libro.DISPONIBLE,
            'precio': Decimal('420.00'),
            'valoracion': Decimal('4.65'),
            'activo': True,
            'creado_por': admin_user
        },
        {
            'titulo': 'Ficciones',
            'subtitulo': 'Cuentos filosóficos',
            'isbn': '9780802130303',
            'autor': borges,
            'categoria': ficcion,
            'editorial': 'Editorial Sudamericana',
            'fecha_publicacion': date(1944, 1, 1),
            'paginas': 174,
            'idioma': 'Español',
            'descripcion': 'Colección de cuentos que explora temas filosóficos y metafísicos.',
            'imagen_portada': 'https://ejemplo.com/portadas/ficciones.jpg',
            'stock': 3,
            'estado': Libro.DISPONIBLE,
            'precio': Decimal('290.00'),
            'valoracion': Decimal('4.90'),
            'activo': True,
            'creado_por': admin_user
        },
        {
            'titulo': 'El laberinto de la soledad',
            'subtitulo': 'Ensayo sobre la identidad mexicana',
            'isbn': '9786071613578',
            'autor': paz,
            'categoria': ensayo,
            'editorial': 'Fondo de Cultura Económica',
            'fecha_publicacion': date(1950, 1, 1),
            'paginas': 191,
            'idioma': 'Español',
            'descripcion': 'Ensayo sobre la identidad mexicana y latinoamericana.',
            'imagen_portada': 'https://ejemplo.com/portadas/laberinto.jpg',
            'stock': 2,
            'estado': Libro.DISPONIBLE,
            'precio': Decimal('280.00'),
            'valoracion': Decimal('4.55'),
            'activo': True,
            'creado_por': admin_user
        },
        {
            'titulo': 'La ciudad y los perros',
            'subtitulo': '',
            'isbn': '9788420412146',
            'autor': vargas_llosa,
            'categoria': ficcion,
            'editorial': 'Alfaguara',
            'fecha_publicacion': date(1963, 1, 1),
            'paginas': 399,
            'idioma': 'Español',
            'descripcion': 'Novela ambientada en un colegio militar de Lima.',
            'imagen_portada': 'https://ejemplo.com/portadas/ciudad_perros.jpg',
            'stock': 4,
            'estado': Libro.DISPONIBLE,
            'precio': Decimal('390.00'),
            'valoracion': Decimal('4.60'),
            'activo': True,
            'creado_por': admin_user
        },
        {
            'titulo': 'Conversación en La Catedral',
            'subtitulo': '',
            'isbn': '9788420412153',
            'autor': vargas_llosa,
            'categoria': ficcion,
            'editorial': 'Alfaguara',
            'fecha_publicacion': date(1969, 1, 1),
            'paginas': 729,
            'idioma': 'Español',
            'descripcion': 'Retrato crítico de la sociedad peruana bajo dictadura.',
            'imagen_portada': 'https://ejemplo.com/portadas/conversacion.jpg',
            'stock': 2,
            'estado': Libro.DISPONIBLE,
            'precio': Decimal('520.00'),
            'valoracion': Decimal('4.75'),
            'activo': True,
            'creado_por': admin_user
        },
        {
            'titulo': 'Rayuela',
            'subtitulo': 'Novela experimental',
            'isbn': '9788437604578',
            'autor': cortazar,
            'categoria': ficcion,
            'editorial': 'Editorial Sudamericana',
            'fecha_publicacion': date(1963, 6, 28),
            'paginas': 608,
            'idioma': 'Español',
            'descripcion': 'Novela experimental que puede leerse de múltiples maneras.',
            'imagen_portada': 'https://ejemplo.com/portadas/rayuela.jpg',
            'stock': 3,
            'estado': Libro.DISPONIBLE,
            'precio': Decimal('480.00'),
            'valoracion': Decimal('4.80'),
            'activo': True,
            'creado_por': admin_user
        },
        {
            'titulo': 'Como agua para chocolate',
            'subtitulo': 'Novela de entregas mensuales',
            'isbn': '9788401335181',
            'autor': esquivel,
            'categoria': romance,
            'editorial': 'Planeta',
            'fecha_publicacion': date(1989, 1, 1),
            'paginas': 224,
            'idioma': 'Español',
            'descripcion': 'Novela que combina recetas de cocina con una historia de amor.',
            'imagen_portada': 'https://ejemplo.com/portadas/agua_chocolate.jpg',
            'stock': 5,
            'estado': Libro.DISPONIBLE,
            'precio': Decimal('320.00'),
            'valoracion': Decimal('4.40'),
            'activo': True,
            'creado_por': admin_user
        },
        {
            'titulo': 'Los detectives salvajes',
            'subtitulo': '',
            'isbn': '9788433920672',
            'autor': bolaño,
            'categoria': ficcion,
            'editorial': 'Alfaguara',
            'fecha_publicacion': date(1998, 1, 1),
            'paginas': 618,
            'idioma': 'Español',
            'descripcion': 'Novela que narra la búsqueda de una poeta desaparecida.',
            'imagen_portada': 'https://ejemplo.com/portadas/detectives.jpg',
            'stock': 2,
            'estado': Libro.DISPONIBLE,
            'precio': Decimal('550.00'),
            'valoracion': Decimal('4.50'),
            'activo': True,
            'creado_por': admin_user
        },
        {
            'titulo': 'La noche de Tlatelolco',
            'subtitulo': 'Testimonios de historia oral',
            'isbn': '9789684113800',
            'autor': poniatowska,
            'categoria': historia,
            'editorial': 'Fondo de Cultura Económica',
            'fecha_publicacion': date(1971, 1, 1),
            'paginas': 282,
            'idioma': 'Español',
            'descripcion': 'Testimonios sobre la masacre estudiantil de 1968 en México.',
            'imagen_portada': 'https://ejemplo.com/portadas/tlatelolco.jpg',
            'stock': 3,
            'estado': Libro.DISPONIBLE,
            'precio': Decimal('340.00'),
            'valoracion': Decimal('4.70'),
            'activo': True,
            'creado_por': admin_user
        },
        {
            'titulo': 'El beso de la mujer araña',
            'subtitulo': '',
            'isbn': '9788433920542',
            'autor': puig,
            'categoria': ficcion,
            'editorial': 'Editorial Sudamericana',
            'fecha_publicacion': date(1976, 1, 1),
            'paginas': 287,
            'idioma': 'Español',
            'descripcion': 'Diálogo entre dos presos en una celda argentina.',
            'imagen_portada': 'https://ejemplo.com/portadas/beso_mujer.jpg',
            'stock': 2,
            'estado': Libro.DISPONIBLE,
            'precio': Decimal('360.00'),
            'valoracion': Decimal('4.45'),
            'activo': True,
            'creado_por': admin_user
        },
        {
            'titulo': 'Bestiario',
            'subtitulo': 'Cuentos',
            'isbn': '9788437601234',
            'autor': cortazar,
            'categoria': terror,  # <-- Ahora terror está definida
            'editorial': 'Editorial Sudamericana',
            'fecha_publicacion': date(1951, 1, 1),
            'paginas': 176,
            'idioma': 'Español',
            'descripcion': 'Primer libro de cuentos de Julio Cortázar.',
            'imagen_portada': 'https://ejemplo.com/portadas/bestiario.jpg',
            'stock': 3,
            'estado': Libro.DISPONIBLE,
            'precio': Decimal('310.00'),
            'valoracion': Decimal('4.35'),
            'activo': True,
            'creado_por': admin_user
        },
    ]
    
    for libro_data in libros_data:
        libro, created = Libro.objects.get_or_create(
            isbn=libro_data['isbn'],
            defaults=libro_data
        )
        if created:
            print(f"  ✓ Libro '{libro.titulo}' creado (Stock: {libro.stock}, Precio: L{libro.precio}, Valoración: {libro.valoracion})")


def crear_prestamos():
    """Crear préstamos de prueba"""
    print("\nCreando préstamos...")
    
    # Obtener usuarios
    juan = User.objects.get(username='juan_perez')
    maria = User.objects.get(username='maria_lopez')
    carlos = User.objects.get(username='carlos_ruiz')
    ana = User.objects.get(username='ana_torres')
    luis = User.objects.get(username='luis_ramos')
    
    # Obtener libros
    cien_anos = Libro.objects.get(isbn='9780307474728')
    ficciones = Libro.objects.get(isbn='9780802130303')
    rayuela = Libro.objects.get(isbn='9788437604578')
    detectives = Libro.objects.get(isbn='9788433920672')
    casa_espiritus = Libro.objects.get(isbn='9788401242281')
    agua_chocolate = Libro.objects.get(isbn='9788401335181')
    
    # Fechas para préstamos
    hoy = timezone.now().date()
    
    # Crear préstamos activos
    prestamos_activos = [
        {
            'libro': cien_anos,
            'usuario': juan,
            'fecha_devolucion_esperada': hoy + timedelta(days=14),
            'estado': Prestamo.ACTIVO,
            'notas': 'Primera vez que toma este libro'
        },
        {
            'libro': ficciones,
            'usuario': maria,
            'fecha_devolucion_esperada': hoy + timedelta(days=7),
            'estado': Prestamo.ACTIVO,
            'notas': 'Libro para trabajo de literatura'
        },
        {
            'libro': rayuela,
            'usuario': carlos,
            'fecha_devolucion_esperada': hoy + timedelta(days=10),
            'estado': Prestamo.ACTIVO,
            'notas': ''
        },
        {
            'libro': detectives,
            'usuario': juan,
            'fecha_devolucion_esperada': hoy + timedelta(days=21),
            'estado': Prestamo.ACTIVO,
            'notas': 'Cliente frecuente'
        },
        {
            'libro': agua_chocolate,
            'usuario': ana,
            'fecha_devolucion_esperada': hoy + timedelta(days=5),
            'estado': Prestamo.ACTIVO,
            'notas': 'Recomendación del mes'
        },
    ]
    
    # Crear préstamo atrasado
    prestamos_atrasados = [
        {
            'libro': casa_espiritus,
            'usuario': luis,
            'fecha_devolucion_esperada': hoy - timedelta(days=3),  # 3 días atrasado
            'estado': Prestamo.ATRASADO,
            'notas': 'Cliente no responde a notificaciones'
        },
    ]
    
    # Crear préstamos devueltos
    prestamos_devueltos = [
        {
            'libro': agua_chocolate,
            'usuario': maria,
            'fecha_devolucion_esperada': hoy - timedelta(days=30),
            'fecha_devolucion_real': hoy - timedelta(days=25),
            'estado': Prestamo.DEVUELTO,
            'notas': 'Devuelto en buen estado'
        },
        {
            'libro': cien_anos,
            'usuario': carlos,
            'fecha_devolucion_esperada': hoy - timedelta(days=15),
            'fecha_devolucion_real': hoy - timedelta(days=14),
            'estado': Prestamo.DEVUELTO,
            'notas': ''
        },
    ]
    
    # Combinar todos los préstamos
    prestamos_data = prestamos_activos + prestamos_atrasados + prestamos_devueltos
    
    for prestamo_data in prestamos_data:
        # Verificar si ya existe un préstamo similar
        existing = Prestamo.objects.filter(
            libro=prestamo_data['libro'],
            usuario=prestamo_data['usuario'],
            estado=prestamo_data['estado']
        ).exists()
        
        if not existing:
            # Crear el préstamo
            prestamo = Prestamo.objects.create(
                libro=prestamo_data['libro'],
                usuario=prestamo_data['usuario'],
                fecha_devolucion_esperada=prestamo_data['fecha_devolucion_esperada'],
                estado=prestamo_data['estado'],
                notas=prestamo_data.get('notas', '')
            )
            
            # Si tiene fecha de devolución real, asignarla
            if 'fecha_devolucion_real' in prestamo_data:
                prestamo.fecha_devolucion_real = timezone.make_aware(
                    timezone.datetime.combine(
                        prestamo_data['fecha_devolucion_real'], 
                        timezone.datetime.min.time()
                    )
                )
                prestamo.save()
            
            # Actualizar stock del libro según el estado
            libro = prestamo_data['libro']
            if prestamo_data['estado'] in [Prestamo.ACTIVO, Prestamo.ATRASADO]:
                libro.actualizar_stock(-1)  # Reducir stock en 1
            print(f"  ✓ Préstamo de '{libro.titulo}' para {prestamo.usuario.username} creado ({prestamo.estado})")
        else:
            print(f"  ℹ Préstamo ya existe: '{prestamo_data['libro'].titulo}' - {prestamo_data['usuario'].username}")


def main():
    """Función principal"""
    print("="*60)
    print("📚 POBLANDO BASE DE DATOS - Sistema de Biblioteca")
    print("="*60)
    
    try:
        crear_usuarios()
        crear_autores()
        crear_categorias()
        crear_libros()
        crear_prestamos()
        
        print("\n" + "="*60)
        print("✅ BASE DE DATOS POBLADA EXITOSAMENTE")
        print("="*60)
        print("\n📊 Resumen:")
        print(f"  • Usuarios: {User.objects.count()}")
        print(f"  • Autores: {Autor.objects.count()}")
        print(f"  • Categorías: {Categoria.objects.count()}")
        print(f"  • Libros: {Libro.objects.count()}")
        print(f"  • Préstamos: {Prestamo.objects.count()}")
        
        # Mostrar resumen de autores por país
        print("\n📊 Autores por país:")
        for pais in Autor.objects.values_list('pais_origen', flat=True).distinct():
            if pais:  # Solo mostrar si hay país
                count = Autor.objects.filter(pais_origen=pais).count()
                print(f"  • {pais}: {count} autor(es)")
        
        # Mostrar resumen de libros por categoría
        print("\n📚 Libros por categoría:")
        for categoria in Categoria.objects.filter(activo=True):
            count = Libro.objects.filter(categoria=categoria).count()
            if count > 0:
                print(f"  • {categoria.nombre}: {count} libro(s)")
        
        # Mostrar estadísticas de libros
        libros = Libro.objects.all()
        if libros.exists():
            print(f"\n💰 Estadísticas de libros:")
            print(f"  • Stock total: {sum(libro.stock for libro in libros)} ejemplares")
            print(f"  • Precio promedio: L{sum(libro.precio for libro in libros)/len(libros):.2f}")
            print(f"  • Valoración promedio: {sum(libro.valoracion for libro in libros)/len(libros):.2f} ⭐")
        
        # Mostrar estadísticas de préstamos
        print(f"\n📊 Préstamos:")
        print(f"  • Activos: {Prestamo.objects.filter(estado=Prestamo.ACTIVO).count()}")
        print(f"  • Atrasados: {Prestamo.objects.filter(estado=Prestamo.ATRASADO).count()}")
        print(f"  • Devueltos: {Prestamo.objects.filter(estado=Prestamo.DEVUELTO).count()}")
        
        print("\n🔑 Credenciales de acceso:")
        print("  Admin: username='admin', password='admin123'")
        print("  Usuarios: password='user123'")
        print("\n🌐 Accede al panel de administración en:")
        print("  http://localhost:8000/admin/")
        
    except Exception as e:
        print(f"\n❌ ERROR: {e}")
        import traceback
        traceback.print_exc()


if __name__ == '__main__':
    main()