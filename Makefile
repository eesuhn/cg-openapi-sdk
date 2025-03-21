submodule:
	@git submodule update --init --remote --recursive

FORCE:

cg-%: FORCE submodule
	@./make.sh $@

.PHONY: submodule cg-% FORCE
