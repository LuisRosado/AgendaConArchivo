# AgendaConArchivo
Una agenda de contactos como el otro repositorio, pero en este se utiliza un archivo.txt para guardar los contactos

En este código de Python, se ha agregado la funcionalidad para cargar y guardar la agenda en un archivo de texto. A continuación, te explico las modificaciones realizadas:

CargarArchivo(agenda, nombre_archivo): Esta función carga los datos de la agenda desde el archivo de texto especificado por nombre_archivo. Si el archivo existe, se lee línea por línea y se agrega cada contacto a la agenda. Si el archivo no existe, se crea uno vacío.

nombre_archivo = 'agenda.txt': Esta línea establece el nombre del archivo en el que se guardarán los datos de la agenda.

with open(nombre_archivo, 'r') as archivo:: En la función CargarArchivo(), se utiliza el contexto with para abrir el archivo en modo lectura ('r'). Esto asegura que el archivo se cierre automáticamente después de leerlo.

with open(nombre_archivo, 'w') as archivo: pass: En la función CargarArchivo(), si el archivo no existe, se utiliza el contexto with para abrirlo en modo escritura ('w') para crearlo, pero no se realiza ninguna operación (pass).

AgregarContacto(agenda, nombre_archivo): Esta función ha sido modificada para agregar un nuevo contacto a la agenda y también para escribir los datos del nuevo contacto en el archivo nombre_archivo para mantener actualizada la información.

with open(nombre_archivo,'a') as archivo: archivo.write(f'{nombre},{telefono},{email},{categoria}\n'): Se utiliza el contexto with para abrir el archivo en modo adición ('a') y se escribe una nueva línea con los datos del contacto recién agregado.

main(): Se ha modificado la función principal para cargar los contactos desde el archivo antes de que se muestre el menú y para guardar los contactos en el archivo después de agregar uno nuevo.

Con estas modificaciones, los datos de la agenda se mantendrán entre ejecuciones del programa, ya que se guardan en el archivo "agenda.txt". Esto proporciona una funcionalidad básica de persistencia de datos para la agenda.
