*****
gedit
*****

Introducción
============
gedit es el editor de texto oficial del ambiente de escritorio GNOME.

Aunque fue diseñado teniendo como objetivos principales la simplicidad y la
facilidad de uso, gedit es un editor de texto de propósito general muy
poderoso.

Algunas de sus características principales son:

   * Soporte completo a texto internacionalizado (UTF-8)
   * Resaltado configurable de la sintáxis de varios lenguajes (C, C++,
     Java, HTML, XML, Python, Perl y muchos otros)
   * Deshacer/Rehacer
   * Edición de archivos en ubicaciones remotas
   * File reverting
   * Soporte para impresión e impresión preliminar
   * Soporte para portapapeles (cortar/copiar/pegar)
   * Buscar y reemplazar
   * Ir a una línea específica
   * Indentación automática
   * Text wrapping
   * Números de línea
   * Margen derecho
   * Resaltado de la línea actual
   * Cierres de paréntesis automáticos
   * Respaldo de archivos
   * Fuentes y colores configurables
   * Un manual de usuario completo en línea


gedit también cuenta con sistema flexible de complementos (plugins) los cuales
pueden ser usados para agregarle dinámicamente nuevas características
avanzadas.


Instalación
-----------

Linux - Debian/Ubuntu
^^^^^^^^^^^^^^^^^^^^^
gedit viene instalado por defecto en las distribuciones de Debian y Ubuntu con
ambiente de escritorio GNOME.

OSX
^^^^^
Puede descargar la versión más reciente en: http://ftp.gnome.org/pub/GNOME/binaries/mac/gedit/

Windows
^^^^^^^
Puede descargar la versión más reciente en: http://ftp.gnome.org/pub/GNOME/binaries/win32/gedit/


Configuración
=============
TBD


Complementos (plugins)
======================
.. warning::
   Todos los complementos mencionados en este texto son para la versión 2 de
   gedit.

gedit viene con una serie de complementos instalados por defecto y cuenta con
una gran cantidad de complementos disponibles. Se puede consultar una lista de
algunos de ellos en: http://live.gnome.org/Gedit/PluginsOld

Recomendamos, como mínimo, la instalación adicional de los paquetes de
complementos estándar y para desarrolladores.

Complementos instalados por defecto
-----------------------------------
Algunos de los complementos instalados en gedit por defecto son los
siguientes:

   * Cambiar capitalización: cambia la capitalización del texto seleccionado.
   * Buscar actualización: busca la versión más reciente de gedit (sólo para
     Win32 y OS X)
   * Herramientas externas: ejecuta comandos y scripts de shell.
     (http://live.gnome.org/Gedit/ToolLauncherPlugin)
   * Panel del examinador de archivos: Permite el acceso a archivos de forma
     fácil desde el panel lateral.
     (http://live.gnome.org/Gedit/Plugins/FileBrowser)
   * Consola Python: muestra una consola interactiva de Python en el panel
     inferior.
   * Apertura rápida: permite abrir documentos de forma rápida.
   * Recortes: inserta fragmentos de texto usados con frecuencia.
     (http://live.gnome.org/Gedit/Plugins/Snippets)
   * Ordenar: ordena un documento o el texto seleccionado.
   * Corrector ortográfico: Comprueba la ortografía del documento actual.


Otros complementos estándar
---------------------------
gedit cuenta, de manera adicional, con un paquete de complementos estándar que
incluye, entre otros, los siguiente plugins:

   * Marcadores: Permite navegar fácilmente a través de los documentos.
   * Completar paréntesis: Añade automáticamente cierres de paréntesis.
   * Mapa de caracteres: Inserta caracteres especiales tan sólo pulsando en
     ellos.
   * Comentar código: Comentar o descomentar un bloque de código
     seleccionado.
   * Unir/Dividir líneas: Unir varias líneas o dividir líneas largas.
   * Multiedición: Editar el documento en múltiples ubicaciones a la vez.
   * Salvasesiones: Permite guardar y restablecer sesiones de trabajo.
   * Espacios inteligentes: Permite disminuir la sangría del mismo modo que
     si se estuvieran usando tabulaciones.
   * Terminal empotrado: Muestra un terminal en el panel inferior.


Complementos para desarrollador
-------------------------------
Existe un paquete con complementos para desarrolladores que incluye algunas
funcionalidades muy útiles:

   * GDP Find: Busca texto coincidente en múltiples archivos.
   * GDP Format: Da formato al texto y al código.
   * GDP Sintax Completer: Completa palabras y símbolos de Python en la
     posición del cursor.


Integración con RabbitVCS
-------------------------
RabbitVCS is a set of graphical tools written to provide simple and
straightforward access to the version control systems you use. We provide
multiple clients and extensions designed to give you a uniform experience no
matter what development tools you use.


Instalación de los complementos
-------------------------------

Linux - Debian/Ubuntu
^^^^^^^^^^^^^^^^^^^^^

Los complementos estándar se pueden instalar usando apt:
::

   sudo apt-get install gedit-plugins


Para la instalación de los complementos para desarrollador se procede del
mismo modo:
::

   sudo add-apt-repository ppa:sinzui/ppa
   sudo apt-get update
   sudo apt-get install gedit-developer-plugins


La instalación de RabbitVCS, y su complemento para gedit, se realiza de la
siguiente forma:
::

   sudo add-apt-repository ppa:rabbitvcs/ppa
   sudo apt-get update
   sudo apt-get install rabbitvcs-core rabbitvcs-nautilus rabbitvcs-gedit


OSX
^^^^^
TBD


Windows
^^^^^^^
TBD