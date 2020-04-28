import gi
import predecir
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GdkPixbuf

#clase para manejar eventos
class Handler:
    def onDestroy(self, *args):
        Gtk.main_quit()
    
    def directory_set(self, button):
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale(button.get_filename(),500,500,preserve_aspect_ratio=True)
        image.set_from_pixbuf(pixbuf)
        print(button.get_filename())
        respuesta= predecir.predict(button.get_filename())
        textbuffer = text.get_buffer()
        if respuesta==0:
            textbuffer.set_text("FASE 1\nPROPAGACION DE PLANDULAS\nEdad: 2-3 semanas de vida\nTiempo de cosecha: 13-14 semanas aprox.\nINFO: la propagacion de plnadulas consiste en el desarrollo\ninicial de la planta, desde la germinación hasta obtener las primeras ramas principales.")
        elif respuesta==1:
            textbuffer.set_text("FASE 2:\n DESARROLLO DE RAICES\nEdad: 4-6 semanas de vida\nTiempo de cosecha: 10-12 semanas aprox.\nINFO: Se recomienda transplantar a un area mas grande para que\nla planta pueda enraizar correctamente.")
        elif respuesta==2:
            textbuffer.set_text("FASE 6:\nCOSECHA\nEdad: 16- semanas de vida\nTiempo de cosecha: AHORA\nINFO: Coseche según sea su necesidad, Para obtener un sabor\nunico espere hasta que este completamente rojo.")
        elif respuesta==3: 
            textbuffer.set_text("FASE 3:\nMADURACION O DE CRECIMIENTO\nEdad: 7-11 semanas de vida\nTiempo de cosecha: 5-11 semanas aprox.\nINFO: Produre agregar un soporte para que la planta crezca\n correctamente. Se recomienda abonar a cada 10-15 dias para\n que la planta crezca correctamente.")
        elif respuesta==4:
            textbuffer.set_text("FASE 4:\nFLORACION\nEdad: 12-13 semanas de vida\nTiempo de cosecha: 3-4 semanas aprox.\nINFO: Las flores amarillas son los puntos en donde creceran\nlos frutos. Los primeros brotarán en la parte baja de la planta.")
        elif respuesta==5:
            textbuffer.set_text("FASE 5:\nPRODUCCION\nEdad: 14-15 semanas de vida\nTiempo de cosecha: 1-2 semanas aprox.\nINFO: La planta ha iniciado a desarrollar sus frutos.\nDebe esperar a que crezcan y muestren un color rojizo-anaranjado.")

#constructor del archivo glade
builder = Gtk.Builder()
builder.add_from_file("pgrafica.glade")
builder.connect_signals(Handler())

#definicion de objetos
image = builder.get_object("img")
text = builder.get_object("txt") #nombre de la variable del GtkTextView

#definicion de la ventana principal
window = builder.get_object("principal")
window.show_all()
Gtk.main()