.PHONY: main
main: war-and-peace.flag.txt


war-and-peace.flag.txt: flag
	cp war-and-peace.txt war-and-peace.flag.txt
	python3 byteblast.py war-and-peace.flag.txt flag 50000
	

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
