umm\_script (Ultimate Math Machine Script)
==========

A Python script that will automatically turn any apt-posessing virtual machine into a mathematician's heaven.

Running
---------
This script has been tested with 100% installation success on Linux Mint 14.1. Use of Linux Mint 14 is highly recommended, but Ubuntu or Debian should work as well. Note that `udm` is heavily reliant on `apt-get`, so make sure that it exists on your machine before running.

 - Navigate to `umm_script/` and run the command `sudo ./umm.py`


Adding and Removing Packages
---------
To remove or add a cluster (container) of packages:

 - Navigate to `umm_script/packs`
 - Open `desired_packages.py` in an editor
 - Remove or add `<mypack>.container` to the `package_containers` list at the bottom of the file. If you are adding a new package container, be sure to import its module above this list

To remove or add individual packages:

 - Navigate to `umm_script/packs`
 - Open the container of the package that you want to add or remove
 - Add or remove items from the `packages` dictionary in the following form: <br/>`'<user-friendly-name>': '<actual-package-name>'` (note that the `<actual-package-name>` is what `apt` will be expecting)
