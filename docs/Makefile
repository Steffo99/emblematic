# Slightly extended makefile for Sphinx documentation

# Sphinx options
export SPHINXOPTS    =
export SPHINXBUILD   = "sphinx-build"
export SOURCEDIR     = "source"
export BUILDDIR      = "build"

# LaTeX builder options
export LATEXMKOPTS   =
export LATEXOPTS     = "-interaction=nonstopmode"

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
