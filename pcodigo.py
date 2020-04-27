import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GdkPixbuf

#clase para manejar eventos
class Handler:
    def onDestroy(self, *args):
        Gtk.main_quit()
    
    def directory_set(self, button):
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale(button.get_filename(),250,250,preserve_aspect_ratio=True)
        image.set_from_pixbuf(pixbuf)
        # print(button.get_filename())
    
    #metodo para agregar la descipcion
    def description_set(self, button):
        textbuffer = text.get_buffer()
        textbuffer.set_text("Hola mundo!")

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