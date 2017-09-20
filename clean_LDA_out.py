# coding: utf-8
import csv
import pandas as pd
import re #regular expression
import argparse
import os

"""
This script takes the tagged url output from train_LDA, cleans it, joins it to the original url TaxonPath data from govuk (which gives the user-research-generated taxons) and writes it to csv, where it will subsequently be read into R for performance metrics


Example usage:
python clean_lda_out.py --out_path ../DATA/education/clean_lda_output --taxonfile ../DATA/education/educ_link_taxonpath.csv --raw_lda ../DATA/education/raw_lda_output/educ_154tops_tags.csv
"""  
__author__ = "Ellie King"
__copyright__ = "Government Digital Service, 20/09/2017"


parser = argparse.ArgumentParser(description=__doc__)

parser.add_argument(
    '--out_path', dest='out_path', metavar='OUTPUT FOLDER', default=None,
    help='export cleaned url, topics 1-3 and probs 1-3 to csv'
)

parser.add_argument(
    '--taxonfile', dest='taxons_filename', metavar='FILENAME', default=None,
    help='import original url taxonpath data in csv'
)

parser.add_argument(
    '--raw_lda', dest='raw_taggedurls_filename', metavar='FILENAME', default=None,
    help='import tagged urls in csv output from LDA'
)


def read_data(taxonfile, raw_lda):
    """Function to read in original data and tagged documents after LDA"""
    tags = pd.read_csv(raw_lda, header=None, names=['url', 'topic1', 'p1', 'topic2', 'p2', 'topic3', 'p3'])
    print(tags.head(5))
    original = pd.read_csv(taxonfile)
    print(original.head(5))
    return(tags, original)

# def clean_tagged_urls(df_tag):
#     """function to clean the dataframe to result in url 
#     topic_id cols"""
#     #drop the leading parentheses
#     df_tag['b'] = df_tag['b'].str.replace(r'\[\(', '') 
#     # drop the columns containing topics of lower (or equal probability)
#     df2_tag =  df_tag.drop(df_tag.columns[[2, 3, 4, 5, 6, 7]], axis=1)
#     # name the remaining two columns
#     df2_tag.columns = ['url', 'topic_id']
#     return(df2_tag)

# def get_text_by_merging(urls_by_topic_filtered):
#     #merge on the index column to get text back from original url, text data
#     urltext_by_topic = []
#     for df in urls_by_topic_filtered:
#         urltext_by_topic.append(pd.merge(df, df_preLDA, left_index = True, right_index = True , indicator = True))
#     return urltext_by_topic






# out_lda.columns = ['Link', 'topic1', 'p1', 'topic2', 'p2', 'topic3', 'p3']
# out_lda['topic1'] = out_lda['topic1'].str.replace(r'\[\(', '')
# out_lda['topic2'] = out_lda['topic2'].str.replace(r'\(', '')
# out_lda['topic3'] = out_lda['topic3'].str.replace(r'\(', '')

# out_lda['p3'] = out_lda['p3'].str.replace(r'\)\]', '')
# out_lda['p1'] = out_lda['p1'].str.replace(r'\)', '')
# out_lda['p1'] = out_lda['p1'].str.replace(r'\]', '')
# out_lda['p2'] = out_lda['p2'].str.replace(r'\)\]', '')
# out_lda['p2'] = out_lda['p2'].str.replace(r'\)', '')
# out_lda.head()

# both = pd.merge(out_lda, original, how = 'inner', on = 'Link', indicator = True)
# both.head()
# original.shape
# out_lda.shape
# both.shape
# pd.crosstab(index = both['_merge'], columns = 'count')
# both = pd.merge(out_lda, original, how = 'left', on = 'Link', indicator = True)
# both.shape
# pd.crosstab(index = both['_merge'], columns = 'count')
# both = pd.merge(original, out_lda, how = 'left', on = 'Link', indicator = True)
# pd.crosstab(index = both['_merge'], columns = 'count')

# original.Link.nunique()
# out_lda.Link.nunique()
# original.shape
# out_lda.shape
# both.Link.nunique()

# out_lda.to_csv('../DATA/education/educ_lda_out.csv', index = False)

if __name__ == '__main__':
    args = parser.parse_args()
    
    print("Loading input file {}".format(args.taxons_filename))
    print("Loading input file {}".format(args.raw_taggedurls_filename))
    tags, original = read_data(
        taxonfile = args.taxons_filename, 
        raw_lda = args.raw_taggedurls_filename,
        )

