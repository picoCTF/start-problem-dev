.PHONY: main
main: disk.flag.img.gz

FLAG_PHRASE := "d15k_513uth_"
FLAG := $(shell echo $(FLAG) | sed "s/{/{$(FLAG_PHRASE)/1")

disk.flag.img.gz: flag
	cp disk.img.gz disk.flag.img.gz
	gunzip disk.flag.img.gz
	python3 byteblast.py disk.flag.img flag 509014036
	gzip -c disk.flag.img > disk.flag.img.gz


artifacts.tar.gz: disk.flag.img.gz
	tar czvf $@ $^


flag:
	@echo "$(FLAG)" > flag


metadata.json:
	@echo "Creating the metadata file..."
	@echo "{\"flag\":\"$(FLAG)\"}" > metadata.json


.PHONY: clean
clean:
	rm -f flag
	rm -f war-and-peace.flag.txt
