import csv


def read_data():
	pattern_url = re.compile(
            'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    with open('data.tsv') as tsvfile:
        tsvreader = csv.reader(tsvfile,	delimiter='\t')
        for row in tsvreader:
            print('\t'.join(row))

def get_urls(text):
	''' 
	this function returns a list of all urls present in the given text 
	'''
	return None

def get_url_details():
	'''
	this function returns details of an url 
	url_subject: a subject for the url 
	url_type: image, video
	'''
	return None	

def main():
    read_data()
    

if __name__ == '__main__':
    main()
