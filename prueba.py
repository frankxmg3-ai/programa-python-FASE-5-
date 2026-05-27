# Nombre del estudiante: Franklin David Patiño Coral
# Grupo: 213022_769
# Programa: Ingeniería Electrónica
# Código Fuente: autoría propia

# Columna 0: ID Cliente
# Columna 1: Duración (segundos)
# Columna 2: Eventos Clicks

# Datos Iniciales: Matris definida directamente con 5 filas de datos de ejemplo  
Datos = [
    [111, 215, 10],
    [112, 18, 2],
    [113, 304, 12],
    [114, 10, 1],
    [115, 285, 8]
]

def nivel_compromiso(duracion, clics):
    """
    Módulo que calcula la clasificación del nivel de compromiso
    de una sesión basándose en su duración y clics.
    """
    # Lógica de Negocio
    if duracion > 180 and clics > 8:
        return "Alto"
    elif duracion < 60 or clics < 3:  
        return "Bajo"
    else:
        return "Medio"

# Inicio del programa
on = 's'
while on == 's' or on == 'S':
    print("\n===== clasificación de compromiso =====")
    
    # Recorrido de la matriz para generar el informe
    for i in Datos:
        cliente_id = i[0]
        duracion = i[1]
        clics = i[2]
        
        # Llamado a la función de clasificación
        compromiso = nivel_compromiso(duracion, clics)
        
        # Salida: Informe listando el ID del cliente y su clasificación final
        print(f"Cliente ID: {cliente_id} Nivel de Compromiso: {compromiso}")
        
    print("==================================\n")
    
    # Control para evaluar si se repite o finaliza el ciclo
    on = input('¿Diligenciar de nuevo el informe de clasificación S/N?: ')
    while on not in ['S', 's', 'N', 'n']:
        print('Incorrecto. Digite S o N.')
        on = input()

print('Gracias, vuelva pronto\n')