BASE_URL = https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-today.aspx
TARGETS = $(shell cat input/targets.txt)
TARGETS_HTML = $(foreach t,$(TARGETS),input/$(t).html)

.PHONY: all clean install
all: data/corpus.txt

clean:
	rm data/corpus.txt

install:
	pipenv install --dev

data/corpus.txt: $(TARGETS_HTML)
	pipenv run python scripts/scrape_horoscopes.py > $@

.PRECIOUS: input/%.html
input/%.html:
	mkdir -p $(dir $@)
	wget -q -O $@ '$(BASE_URL)?ladate=$(word 1,$(subst /, ,$*))&sign=$(word 2,$(subst /, ,$*))'

input/targets.txt:
	python3 scripts/create_targets.py > $@
