# Big Red Button Programming

Guide and resources to program a [Yoqanr USB Button](https://www.amazon.com/dp/B0DL5XHNJX).

Yes, it comes with decentish setup software. No, I wasn't satisfied...

## How to use

1. Clone git repo
2. Ensure you have python
3. `pip install -r requirements.txt`
4. Run ListDevices to figure out the PID and VID of your button, `python ListDevices.py`
5. Update ProgramButton with the correct PID + VID, as well as the key you want to set
6. Run ProgramButton, `python ProgramButton.py`

## Other Resources

* [Wireshark](https://www.wireshark.org/)
  * [USBPcap](https://desowin.org/usbpcap/)
    * [Wireshark + USBPcap](https://desowin.org/usbpcap/tour.html)
* [KeyboardTester](https://www.keyboardtester.com/tester.html)
* [Keycodes](https://gist.github.com/MightyPork/6da26e382a7ad91b5496ee55fdc73db2)
* [HIDAPI](https://trezor.github.io/cython-hidapi/index.html)

## But... why tho?

Because I wanted to program the button to whatever I wanted, GUI limitations be d*mned! But really F13, which is a good unused key to listen for.
