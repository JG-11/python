import csv

class ContactBook:
    def __init__(self):
        self._contacts = []

    def _save(self):
        with open('contacts.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerow(('name', 'phone', 'email'))

            for contact in self._contacts:
                writer.writerow((contact.name, contact.phone, contact.email))

    def add(self, contact):
        self._contacts.append(contact)
        self._save()

    def update(self, name):
        for contact in self._contacts:
            if contact.name.lower() == name.lower():
                self._show_contact(contact)

                try:
                    phone = input('Ingrese el nuevo teléfono: ')
                    email = input('Ingrese el nuevo correo: ')

                    contact.phone = phone
                    contact.email = email

                    print('Contacto actualizado exitosamente')

                    self._save()
                except:
                    print('Error al intentar actualizar el contacto. Intente de nuevo')
                finally:
                    break
        else:
            self._not_found(name)

    def search(self, name):
        for contact in self._contacts:
            if contact.name.lower() == name.lower():
                self._show_contact(contact)
                break
        else:
            self._not_found(name)

    def delete(self, name):
        # enumerate is useful for obtaining an indexed list
        for index, contact in enumerate(self._contacts):
            if contact.name.lower() == name.lower():
                del self._contacts[index]
                print('Contacto eliminado correctamente')
                self._save()
                break
        else:
            self._not_found(name)

    def show_all(self):
        for contact in self._contacts:
            self._show_contact(contact)

    def _show_contact(self, contact):
        print("""
            -------
            Nombre: {}
            Teléfono: {}
            Email: {}
            -------
        """.format(contact.name, contact.phone, contact.email))

    def _not_found(self, name):
        print('Contacto con el nombre {}, no ha sido encontrado'.format(name))