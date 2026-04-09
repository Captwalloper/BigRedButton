import hid

def list_hid_devices():
    print(f"{'Manufacturer':<20} | {'Product':<30} | {'VID:PID'}")
    print("-" * 70)
    for device in hid.enumerate():
        # Convert decimal IDs to Hex (Standard format)
        vid_hex = f"{device['vendor_id']:04x}"
        pid_hex = f"{device['product_id']:04x}"
        m_name = str(device['manufacturer_string'])
        p_name = str(device['product_string'])
        print(f"{m_name[:20]:<20} | {p_name[:30]:<30} | {vid_hex}:{pid_hex}")

if __name__ == "__main__":
    list_hid_devices()