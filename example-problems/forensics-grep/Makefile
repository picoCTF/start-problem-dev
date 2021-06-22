.PHONY: main
main: war-and-peace.flag.txt


artifacts.tar.gz: war-and-peace.flag.txt
	tar czvf $@ $^
	
war-and-peace.flag.txt: flag
	cp war-and-peace.txt war-and-peace.flag.txt
	python3 byteblast.py war-and-peace.flag.txt flag 50000

flag:
	@echo "$(FLAG)" > flag

metadata.json:
	@echo "Creating the metadata file..."
	@echo "{\"flag\":\"$(FLAG)\"}" > metadata.json

clean:
	rm -f flag
