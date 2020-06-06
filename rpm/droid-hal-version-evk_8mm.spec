# rpm_device is the name of the ported device
%define rpm_device evk_8mm
# rpm_vendor is used in the rpm space
%define rpm_vendor fsl
# Manufacturer and device name to be shown in UI
%define vendor_pretty Freescale
%define device_pretty IMX8M Mini
# See ../droid-hal-version/droid-hal-device.inc for similar macros:
%define have_vibrator_native 1
%define have_led 1
%include droid-hal-version/droid-hal-version.inc
