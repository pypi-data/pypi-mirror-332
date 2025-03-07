Changelog
=========

0.0.1 (2025-03-07)
------------------

- initial release, code moved here from https://github.com/wairas/happy-tools
- fixed exception in data-viewer when cancelling the open dialog
- fixed loading of initial scan/references happens now in thread launched from main loop
- changes in r/g/b scales of the envi-viewer no longer trigger image update when `ignore_updates==True`
- the `set_wavelengths` method of the envi-viewer no longer triggers image updates, but can trigger one after setting all values

