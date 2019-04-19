On Linux, you need to give your user access to the USB device.

You can do that by creating a file under ``/etc/udev/rules.d/`` named
``99-lda.rules`` with the following content::

    SUBSYSTEM=="usb", ATTR{idVendor}=="041f", MODE="0666"

Then you need to tell udev to reload its rules::

    $ sudo invoke-rc.d udev reload

You must also unplug/replug your device if it was already plugged in.

Then, to run the Lab Brick Digital Attenuator (LDA) controller::

    $ aqctl_lda -d SN:xxxxx

The serial number must contain exactly 5 digits, prepend it with the necessary number of 0s.
Also, the ``SN:`` prefix is mandatory.

You can choose the LDA model with the ``-P`` parameter. The default is LDA-102.
