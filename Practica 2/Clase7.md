# Clase 7 - 2024 #

## Analisis de Malware ##

### Analisis estático ###
Inspección del malware sin ejecutarlo  
**Básico:** Antivirus, análisis de string, VirusTotal

### Maquina virtual ###

**Tomar instantaneas:** guarda el estado de la máquina. Hacerlo antes de ejecutar los malwares. Luego, puedo pedir que reinicie y ejecutar la maquina desde donde tomé el snapshot.

# Clase 7 - 2023 #

Analisas de Malware está muy relacionado tanto con CSIRT como con reversing. Sin embargo, hay mucho que se puede hacer sin reversing.  
Esta práctica se centra más en la utilización de herramientas para saber si algo es malware, más allá de los problemas reales que ese malware puede generar, que para eso quizas si es necesario reversing.  

## Analisis de malware ##

### Analisis estático ###
Sin ejecutar. Podemos llegar a tener certezas de que es malware, pero no sabremos exactamente qué hace o el flujo de ejecución.  

**Básico:** Siempre lo que se pretendé es determinar si la muestra es maliciosa o no y, en caso de serlo, obtener toda la información que se pueda sobre el malware.  
**Herramientas**
- Antivirus/ VirusTotal
- Funciones de hash
- Strings observados en el binario

Para confirmar si es malware: Antivirus o VirusTotal.  
En caso de serlo, VirusTotal nos da información sobre el malware. Se pueden usar hashes para identificar las muestras.
Si los Antivirus no confirmen que es malware, se pueden buscar strings que pueda proveer IOC () o herramientas para analizar la estructura del binario (servicios que importa, funciones que exporta, las secciones del programa).  
**Funciones linkeadas** Información muy valiosa. Saber que funciones de cuales DLLs utiliza un malware nos puede dar una idea de qué es lo que hace el malware.

### Analisis dinámico ###
Inspección del malware funcionando.

## Video Sheyla ##

**Run key:** Donde se registran los ejecutables que se van a ejecutar cuando se inicia el sistema.  
Son entradas en el registro.  

**Hay otras tres técnicas más efectivas para persistir malware en el sistema**  

**Persistencia por shell extensions**  
El atacante no precisa privilegios de administrador. El malware se persiste en una Shell Extension, como el context explorer de Windows.

**Persistencia via Com Hijack**
Cuando una aplicación primero va a buscar un objeto, lo va a buscar a current user. Sabemos que la dll no esta en current user sino en local machine.
Eso nos da la posibilidad de replicar el GUID del objeto que va a buscar, así cuando vaya a buscarlo a current user, levante nuestro path en lugar del que busca.
Se depende de una aplicación que podría no existir, porque la que va a buscar el objeto es la aplicación, por más que muchos objetos se comparten entre aplicaciones.  
Es más fácil hacerlo con objetos nativos de Windows, que sabemos que siempre existe.


**Persistencia via extension Handler Hijack**  
