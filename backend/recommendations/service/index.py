import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

from recommendations.dao.index import RecommendationsDAO

class RecommendationsService:
    def __init__(self):
        self.dao=RecommendationsDAO()
        
        # use the tf-idf (term frequency - inverse document frequency) vectorizer
        self.tf_idf = TfidfVectorizer(stop_words='english')
        
        # select list of all products
        product_list = self.dao.select_id_name_list_from_products()
        
        # convert above list to dataframe
        self.product_df = pd.DataFrame(product_list)
        
        # fit and transform
        name_matrix = self.tf_idf.fit_transform(self.product_df['name'])

        # obtain similarity matrix using cosine similarity on the fit and transform matrix
        self.similarity_matrix = cosine_similarity(name_matrix, name_matrix)

        # create mapping with name as key and index as value
        self.mapping = pd.Series(self.product_df.index,index = self.product_df['name'])

    def select_recommended_product_list(self, product_id):
        product_name = self.dao.select_name_from_id(product_id)
        product_index = self.mapping[product_name]
        
        # calculate 4 highest similarity score
        similarity_score = list(enumerate(self.similarity_matrix[product_index]))
        similarity_score = sorted(similarity_score, key=lambda x: x[1], reverse=True)
        similarity_score = similarity_score[1:5]
        product_indices = [i[0] for i in similarity_score]
        product_id_list=list(self.product_df['id'].iloc[product_indices])
        
        # obtain list of products having highest similarity
        product_list=list(map(lambda x:self.dao.select_product_details_from_id(x), product_id_list))
        return product_list
