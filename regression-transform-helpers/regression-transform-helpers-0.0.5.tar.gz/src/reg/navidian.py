from sklearn.preprocessing import OneHotEncoder

from scipy.sparse import csr_matrix

class NavidianEncoder(OneHotEncoder):
    def transform(self, X):
        transformed = super().transform(X)
        
        feats = self.get_feature_names_out().tolist()

        idx_bm_none = feats.index('badge_model_None')
        idx_sm_none = feats.index('series_model_None')

        transformed = transformed[:, :idx_bm_none]
        transformed = transformed[:, :idx_sm_none]

        transformed = csr_matrix(transformed)

        return transformed
