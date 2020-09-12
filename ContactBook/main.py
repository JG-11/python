import csv

from ContactBook import ContactBook
from Contact import Contact

if __name__ == '__main__':
    contact_book = ContactBook()

    try:
        with open('contacts.csv') as f:
            reader = csv.reader(f)

            for index, row in enumerate(reader):
                if index == 0:
                    continue

                contact = Contact(row[0], row[1], row[2])

                contact_book.add(contact)
    except:
        print('Un nuevo archivo de contactos será creado')

    while True:
        opt = input("""
            [a]gregar contacto
            [ac]tualizar contacto
            [b]uscar contacto
            [e]liminar contacto
            [l]istar contactos
            [s]alir
        """)

        if opt == 'a':
            name = input('Ingrese el nombre del contacto: ')
            phone = input('Ingrese el teléfono del contacto: ')
            email = input('Ingrese el correo del contacto: ')

            contact = Contact(name, phone, email)

            contact_book.add(contact)

        elif opt == 'ac':
            name = input('Ingrese el nombre del contacto a actualizar: ')

            contact_book.update(name)

        elif opt == 'b':
            name = input('Ingrese el nombre del contacto a buscar: ')

            contact_book.search(name)

        elif opt == 'e':
            name = input('Ingrese el nombre del contacto a eliminar: ')

            contact_book.delete(name)
        
        elif opt == 'l':
            contact_book.show_all()

        elif opt == 's':
            break

        else:
            print('Opción no válida. Intente de nuevo')


