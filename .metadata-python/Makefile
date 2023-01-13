# This file is generated automatically from metadata.org
# File edits may be overwritten!

.PHONY: upload
upload: metadata package twine add clean

GUIX-SHELL = guix time-machine -C guix/channels.scm -- shell
DEV = -D -f guix/guix.scm
GUIX-DEV-SHELL = $(GUIX-SHELL) $(DEV)

.PHONY: guix-dev-shell
guix-dev-shell:
	$(GUIX-DEV-SHELL)

.PHONY: ipython-shell
ipython-shell:
	$(GUIX-DEV-SHELL) -- ipython

.PHONY: serial-shell
serial-shell:
	$(GUIX-DEV-SHELL) picocom -- picocom -b 9600 -f n -y n -d 8 -p 1 -c $(PORT)

.PHONY: installed-shell
installed-shell:
	$(GUIX-SHELL) -f guix/guix.scm --rebuild-cache

.PHONY: metadata-edits
metadata-edits:
	$(GUIX-DEV-SHELL) -- sh -c "emacs -q --no-site-file --no-site-lisp --no-splash -l emacs/init.el --file metadata.org"

.PHONY: metadata
metadata:
	$(GUIX-DEV-SHELL) -- sh -c "emacs --batch -Q  -l emacs/init.el --eval '(process-org \"metadata.org\")'"

.PHONY: package
package:
	$(GUIX-DEV-SHELL) -- sh -c "python3 setup.py sdist bdist_wheel"

.PHONY: twine
twine:
	$(GUIX-DEV-SHELL) --network --expose=$$HOME/.pypirc -- sh -c "twine upload dist/*"

.PHONY: add
add:
	$(GUIX-DEV-SHELL) -- sh -c "git add --all"

.PHONY: clean
clean:
	$(GUIX-DEV-SHELL) -- sh -c "git clean -xdf"
