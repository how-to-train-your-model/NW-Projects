from pandas.io.html import read_html


# find year founded
def get_founded(page):
    try:
        # get infoboxes
        infoboxes = read_html(page, index_col=0, attrs={"class": "infobox"})
        infobox_df = infoboxes[0]
        founded = infobox_df.loc["Founded"]
        return founded.to_string()
    except:
        return None


# find number employees
def get_emp(page):
    try:
        # get infoboxes
        infoboxes = read_html(page, index_col=0, attrs={"class": "infobox"})
        infobox_df = infoboxes[0]
        emp = infobox_df.loc["Number of employees"]
        return emp.to_string()
    except:
        return None

# find industry
def get_industry(page):
    try:
        # get infoboxes
        infoboxes = read_html(page, index_col=0, attrs={"class": "infobox"})
        infobox_df = infoboxes[0]
        industry = infobox_df.loc["Industry"]
        return industry.to_string()
    except:
        return None

# page = 'https://en.wikipedia.org/wiki/Nestle'

# get infoboxes
# infoboxes = read_html(page, index_col=0, attrs={"class":"infobox"})
# infobox_df = infoboxes[0]
#
# # get tables
# wikitables = read_html(page, index_col=0, attrs={"class":"wikitable"})
# wikitables_df = wikitables[0]
#
# founded = infobox_df.loc["Founded"]
# industry = infobox_df.loc["Industry"]
# num_employees = infobox_df.loc["Number of employees"]
