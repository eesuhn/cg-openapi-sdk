submodule:
	@git submodule update --init --recursive

FORCE:

cg-%: FORCE submodule
	@./make.sh $@

.PHONY: submodule cg-% FORCE
