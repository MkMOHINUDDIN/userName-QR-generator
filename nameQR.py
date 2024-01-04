import os
import qrcode

Name_List = ['Khaja Mohinuddin', "Abdul Rahiman", 'Lateef Rahiman', "Afroz", "Parveen Banu"]

def QR_Generator():
    # Create a directory to store the QR codes if it doesn't exist
    directory = "QR_Codes"
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Generate and save QR codes for each name
    for index, name in enumerate(Name_List, start=1):
        qr = qrcode.make(name)
        qr.save(os.path.join(directory, f"QR_{index}_{name.replace(' ', '_')}.png"))

QR_Generator()
