.PHONY: main
main: war-and-peace.flag.txt

FLAG_PHRASE := "gr3p_15_4_5up3rp0w3r_"
FLAG := $(shell echo $(FLAG) | sed "s/.*{/picoCTF{$(FLAG_PHRASE)/1")

war-and-peace.flag.txt: flag
	cp war-and-peace.txt war-and-peace.flag.txt
	python3 byteblast.py war-and-peace.flag.txt flag 49998
	

artifacts.tar.gz: war-and-peace.flag.txt
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
