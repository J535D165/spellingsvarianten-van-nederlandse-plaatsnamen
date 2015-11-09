import pandas as pd
import unicodedata

# Function to clean the given data to make it easier comaprable. 
def clean(string, lower=True, replace_by_none='[^ \-\_A-Za-z0-9]+', replace_by_whitespace='[\-\_]', remove_brackets=True, inplace=True):

    # Lower the string if lower is True
    string = string.str.lower() if lower else string 

    # Remove all content between brackets
    if remove_brackets:
        string = string.str.replace(r'(\[.*?\]|\(.*?\)|\{.*?\})', '')

    # Remove the special characters
    string = string.str.replace(replace_by_none, '')
    string = string.str.replace(replace_by_whitespace, ' ')

    # Remove multiple whitespaces
    string = string.str.replace(r'\s\s+', ' ')

    # Strip string
    string = string.str.lstrip().str.rstrip()

    return string

def main():

	# Read the data from CBS and parse it into a readable format
	places = pd.read_csv(
		'../raw/Woonplaatsen_in_Nederland.csv', 
		skiprows=3, 
		skipfooter=1, 
		delimiter=';', 
		engine='python', 
		encoding='latin1'
		)

	places.columns = ['Woonplaats', 'Woonplaatscode','Gemeente', 'Gemeente_code', 'Provincie', 'Provincie_code', 'Landsdeel', 'Landsdeel_code']

	municipalities = places.drop_duplicates('Gemeente')
	municipalities['Woonplaats'] = municipalities['Gemeente']
	municipalities['Woonplaatscode'] = ''
	places = places.append(municipalities)

	# Convert all places to lowercase
	places['Variant'] = places['Woonplaats'].str.lower()

	# Add misc cases
	misc = pd.read_csv(
		'../input/miscellaneous.csv', 
		delimiter=';',
		encoding='latin1'
		)
	misc['Variant'] = misc['Variant'].str.lower()
	places_misc = misc.merge(places[[x for x in list(places) if 'Variant' not in x]], how='left', on='Woonplaats')
	places = places.append(places_misc)

	# Replace places with the letter ij by y
	places_with_ij = places[places['Variant'].str.contains('ij')].copy()
	places_with_ij['Variant'] = places_with_ij['Variant'].str.replace('ij', 'y')
	places = places.append(places_with_ij)

	# Remove special tokens 
	places_with_special_tokens = places[~(places['Variant'] == clean(places['Variant'], remove_brackets=False))].copy()
	places_with_special_tokens['Variant'] = clean(places_with_special_tokens['Variant'], remove_brackets=False)
	places = places.append(places_with_special_tokens)

	# Add common misspellings 
	mistakes = pd.read_csv(
		'../input/misspelling.csv', 
		header=None,
		delimiter=';'
		)

	for index, mistake in mistakes.iterrows():

		# Left to right
		places_with = places[places['Variant'].str.contains(str(mistake[0]))].copy()
		places_with['Variant'] = places_with['Variant'].str.replace(str(mistake[0]), str(mistake[1]))
		places = places.append(places_with)

		# # Right to left
		# places_with = places[places['Variant'].str.contains(str(mistake[1]))].copy()
		# places_with['Variant'] = places_with['Variant'].str.replace(str(mistake[1]), str(mistake[0]))
		# places = places.append(places_with)

	# # Replace all special tokens by their latin equivalent
	places_with_special_letters = places.copy()
	places_with_special_letters['Variant'] = places_with_special_letters['Variant'].apply(lambda x: unicodedata.normalize('NFD', x).encode('ascii', 'ignore'))
	places = places.append(places_with_special_letters)

	# Remove all double whitespaces
	places['Variant'] = places['Variant'].str.replace(r'\s\s+', ' ')

	# Remove duplicates
	places.drop_duplicates(['Variant', 'Woonplaats', 'Provincie'], inplace=True)

	# Drop placename of municipalities
	places.loc[(places.Woonplaatscode == ''), 'Woonplaats'] = ''

	# Store
	cols=['Variant', 'Woonplaats', 'Woonplaatscode','Gemeente', 'Gemeente_code', 'Provincie', 'Provincie_code', 'Landsdeel', 'Landsdeel_code']

	places.reset_index(drop=True, inplace=True)
	places.sort(['Gemeente','Woonplaats'], ascending=True, inplace=True)
	places[cols].to_csv(
		'../plaatsnamen_spelling.csv', 
		index=False, 
		sep=';', 
		encoding='utf-8'
		)

	print places.Variant.sample(30)

	# print places[cols].tail(400).sample(10).to_html()

if __name__ == "__main__":
	main()


