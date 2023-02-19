import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

from recommendations.dao.index import RecommendationsDAO

class RecommendationsService:
    def __init__(self):
        self.dao=RecommendationsDAO()
        self.tf_idf = TfidfVectorizer(stop_words='english')
        product_list = self.dao.select_id_name_list_from_products()
        self.product_df = pd.DataFrame(product_list)
        name_matrix = self.tf_idf.fit_transform(self.product_df['name'])
        self.similarity_matrix = cosine_similarity(name_matrix, name_matrix)
        self.mapping = pd.Series(self.product_df.index,index = self.product_df['name'])

    def select_recommended_product_list(self, product_id):
        product_name = self.dao.select_name_from_id(product_id)
        product_index = self.mapping[product_name]
        similarity_score = list(enumerate(self.similarity_matrix[product_index]))
        similarity_score = sorted(similarity_score, key=lambda x: x[1], reverse=True)
        similarity_score = similarity_score[1:5]
        product_indices = [i[0] for i in similarity_score]
        product_id_list=list(self.product_df['id'].iloc[product_indices])
        product_list=list(map(lambda x:self.dao.select_product_details_from_id(x), product_id_list))
        return product_list
