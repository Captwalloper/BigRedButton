import hid

# Replace with the IDs you find using ListDevices
VENDOR_ID = 0x2704 # VID 9988
PRODUCT_ID = 0x2018 # PID 8216
ENTER = 0x28
F13 = 0x68

def program_button(key_code):
    try:
        interfaces = hid.enumerate(VENDOR_ID, PRODUCT_ID)
        # interfaces = hid.enumerate()
        if not interfaces or len(interfaces) < 1:
            print(f"Failed to find any device interfaces for {VENDOR_ID}:{PRODUCT_ID}")
            return
        # for interface in interfaces:
        #     print(interface)
        device_info = next((info for info in interfaces if info['usage_page'] == 65280), None)
        if not device_info:
            print(f"Failed to find interface 1 for device")
            return
        
        # print(device_info)
        device = hid.device()
        device.open_path(device_info['path'])

        print("Sending Handshake...")
        data = [
            # 0x21, 0x09, # USB Setup
            # 0x10, 0x02, # ReportId, Type
            # 0x01, 0x00, 0x07, 0x00, # wIndex, wLength
            0x10, 0xff, 0x0e, 0x2a, 0x00, 0x00, 0x00, # Data Fragment
        ]
        result = device.write([0x00] + data) # Prepend the 0x00 Report ID for Windows
        if result > 0:
            print(f"Successfully wrote {result} bytes.")
        else:
            print(f"Write failed. {result}")
            return
        
        print("Sending Keycode...")
        data = [
            0xaa, 0x01, 0x00, 0x00, key_code
        ] + [0x00] * 59 # pad to 64
        result = device.write([0x00] + data) # Prepend the 0x00 Report ID for Windows
        if result > 0:
            print(f"Successfully wrote {result} bytes. Successfully set key to {key_code}!")
        else:
            print(f"Write failed. {result}")
            return
        
        device.close()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    program_button(F13)

# test with https://www.keyboardtester.com/tester.html
# unofficial lookup for keycodes https://gist.github.com/MightyPork/6da26e382a7ad91b5496ee55fdc73db2

"""
# Wireshark Filter for sniffing around USB button traffic
((((((((!(_ws.col.info == "URB_INTERRUPT in")) && !(_ws.col.info == "URB_BULK out")) && !(_ws.col.info == "URB_BULK in")) && !(_ws.col.info == "SCSI Test Unit Ready LUN: 0x00 ")) && !(_ws.col.info == "GET DESCRIPTOR Request STRING")) && !(_ws.col.info == "GET DESCRIPTOR Response DEVICE")) && !(_ws.col.info == "GET DESCRIPTOR Request CONFIGURATION")) && !(_ws.col.info == "GET DESCRIPTOR Request DEVICE")) && !(_ws.col.info == "GET DESCRIPTOR Response STRING")

# Send SET_REPORT for handshake (critically ReportType = 2 (Output))
0000   1c 00 10 50 0f e5 88 b4 ff ff 00 00 00 00 1b 00   ...P............
0010   00 04 00 11 00 00 02 0f 00 00 00 00 21 09 10 02   ............!...
0020   01 00 07 00 10 ff 0e 2a 00 00 00                  .......*...

# Send URB_INTERRUPT OUT to set the key (the 28 in there is the keycode for 'enter')
0000   1b 00 b0 e2 40 e9 88 b4 ff ff 00 00 00 00 09 00   ....@...........
0010   00 04 00 0f 00 03 01 40 00 00 00 aa 01 00 00 28   .......@.......(
0020   00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00   ................
0030   00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00   ................
0040   00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00   ................
0050   00 00 00 00 00 00 00 00 00 00 00                  ...........
"""