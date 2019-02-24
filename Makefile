PYTHON	?= python
SETUP	:= setup.py

package:
	$(PYTHON) $(SETUP) sdist bdist_wheel

.PHONY: package
