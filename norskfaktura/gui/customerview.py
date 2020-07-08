import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

from norskfaktura.customer import Customer
from norskfaktura.gui import signaling

class CustomerView(Gtk.Box):
    def __init__(self, window, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.window = window

        grid = Gtk.Grid()
        self.add(grid)

        horizontal_margin = 12
        vertical_margin = 12

        name_label = Gtk.Label("Navn: ")
        name_label.set_justify(Gtk.Justification.RIGHT)
        name_label.set_margin_left(horizontal_margin)
        name_label.set_margin_right(5)
        name_label.set_margin_top(horizontal_margin)
        grid.attach(name_label, 0, 0, 1, 1)
        self.name_entry = Gtk.Entry()
        self.name_entry.set_width_chars(25)
        self.name_entry.set_margin_top(vertical_margin)
        grid.attach(self.name_entry, 1, 0, 4, 1)

        org_label = Gtk.Label("Org. nr (om aktuelt): ")
        org_label.set_justify(Gtk.Justification.RIGHT)
        org_label.set_margin_left(horizontal_margin)
        org_label.set_margin_right(5)
        grid.attach(org_label, 0, 1, 1, 1)
        self.org_entry = Gtk.Entry()
        self.org_entry.set_width_chars(25)
        grid.attach(self.org_entry, 1, 1, 4, 1)

        address_label = Gtk.Label("Adresse: ")
        address_label.set_justify(Gtk.Justification.RIGHT)
        address_label.set_margin_left(horizontal_margin)
        address_label.set_margin_right(5)
        address_label.set_margin_top(12)
        grid.attach(address_label, 0, 3, 1, 1)
        self.address_entry_one = Gtk.Entry()
        self.address_entry_one.set_width_chars(25)
        self.address_entry_one.set_margin_top(12)
        grid.attach(self.address_entry_one, 1, 3, 3, 1)
        self.address_entry_two = Gtk.Entry()
        self.address_entry_two.set_width_chars(25)
        grid.attach(self.address_entry_two, 1, 4, 3, 1)
        
        postal_label = Gtk.Label("Postnr og sted: ")
        postal_label.set_justify(Gtk.Justification.RIGHT)
        postal_label.set_margin_left(horizontal_margin)
        postal_label.set_margin_right(5)
        grid.attach(postal_label, 0, 5, 1, 1)
        self.postal_entry = Gtk.Entry()
        self.postal_entry.set_margin_top(12)
        self.postal_entry.set_margin_bottom(vertical_margin)
        grid.attach(self.postal_entry, 1, 5, 3, 1)

        save_button = Gtk.Button("Lagre")
        save_button.set_margin_right(horizontal_margin)
        save_button.set_margin_left(horizontal_margin)
        save_button.set_margin_bottom(vertical_margin)
        save_button.connect("clicked", self.on_save_clicked)
        grid.attach(save_button, 5, 6, 1, 1)

        back_button = Gtk.Button("Tilbake")
        back_button.set_margin_right(horizontal_margin)
        back_button.set_margin_bottom(vertical_margin)
        grid.attach(back_button, 6, 6, 1, 1)
        
        # creating and attaching signal to go home
        signaling.new("home-clicked", self) # signal to get back
        back_button.connect("clicked", self.on_back_clicked)

        signaling.new("new-invoice", self)
        self.create_invoice_button = Gtk.Button("Ny faktura")
        self.create_invoice_button.set_margin_right(horizontal_margin)
        self.create_invoice_button.set_margin_left(horizontal_margin)
        self.create_invoice_button.set_margin_top(vertical_margin)
        self.create_invoice_button.set_sensitive(False)
        self.create_invoice_button.connect(
            "clicked",
            self.on_create_invoice_clicked,
        )
        grid.attach(self.create_invoice_button, 5, 0, 2, 1)

    def on_save_clicked(self, widget):
        #self.customer.id = 1 # save customer data

        # And on confirmation, enable invoice button
        self.create_invoice_button.set_sensitive(True)

    def on_back_clicked(self, widget):
        self.emit("home-clicked", widget)
        
    
    def on_create_invoice_clicked(self, widget):
        pass


def testWindow():
    class TestWindow(Gtk.Window):
        def __init__(self):
            Gtk.Window.__init__(self, title="testwindow")

            self.content = CustomerView(self)
            self.add(self.content)
    win = TestWindow()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()