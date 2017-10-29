# Datasets preprocess

Convert data to value making mining convenience

## Requirements

	pip install -r requirements.txt

## Usage

Use parameter

	pre.py -f <Input dataset File> \
		   -o <Output covert dataset path> \
		   -s <Enter your file's symbol> \
		   -D <Upload Output file to HDFS>

Example:
	
	pre.py -f example.txt -o Output.txt -s " "

If you wnat to upload to HDFS:

You must have $HADOOP_HOME path or it can't upload 

	pre.py -f example.txt -o Output.txt -s " " -D /hadoop 

In parameter has default setting so you can also use:

	pre.py -f example.txt



