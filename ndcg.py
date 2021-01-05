# #coding=utf-8
import numpy as np
# from sklearn.preprocessing import LabelBinarizer
# from sklearn.metrics import make_scorer
#
#
# def dcg_score(y_true, y_score, k=5):
#     """Discounted cumulative gain (DCG) at rank K.
#
#     Parameters
#     ----------
#     y_true : array, shape = [n_samples]
#         Ground truth (true relevance labels).
#     y_score : array, shape = [n_samples, n_classes]
#         Predicted scores.
#     k : int
#         Rank.
#
#     Returns
#     -------
#     score : float
#     """
#     order = np.argsort(y_score)[::-1]
#     y_true = np.take(y_true, order[:k])
#
#     gain = 2 ** y_true - 1
#
#     discounts = np.log2(np.arange(len(y_true)) + 2)
#     return np.sum(gain / discounts)
#
#
# def ndcg_score(ground_truth, predictions, k=5):
#     """Normalized discounted cumulative gain (NDCG) at rank K.
#
#     Normalized Discounted Cumulative Gain (NDCG) measures the performance of a
#     recommendation system based on the graded relevance of the recommended
#     entities. It varies from 0.0 to 1.0, with 1.0 representing the ideal
#     ranking of the entities.
#
#     Parameters
#     ----------
#     ground_truth : array, shape = [n_samples]
#         Ground truth (true labels represended as integers).
#     predictions : array, shape = [n_samples, n_classes]
#         Predicted probabilities.
#     k : int
#         Rank.
#
#     Returns
#     -------
#     score : float
#
#     Example
#     -------
#     >>> ground_truth = [1, 0, 2]
#     >>> predictions = [[0.15, 0.55, 0.2], [0.7, 0.2, 0.1], [0.06, 0.04, 0.9]]
#     >>> score = ndcg_score(ground_truth, predictions, k=2)
#     1.0
#     >>> predictions = [[0.9, 0.5, 0.8], [0.7, 0.2, 0.1], [0.06, 0.04, 0.9]]
#     >>> score = ndcg_score(ground_truth, predictions, k=2)
#     0.6666666666
#     """
#     lb = LabelBinarizer()
#     lb.fit(range(len(predictions) + 1))
#     T = lb.transform(ground_truth)
#
#     scores = []
#
#     # Iterate over each y_true and compute the DCG score
#     for y_true, y_score in zip(T, predictions):
#         actual = dcg_score(y_true, y_score, k)
#         best = dcg_score(y_true, y_true, k)
#         score = float(actual) / float(best)
#         scores.append(score)
#
#     return np.mean(scores)
#
#
# # -------------------------------------------------------
# # NDCG Scorer function
# ndcg_scorer = make_scorer(ndcg_score, needs_proba=True, k=5)
#
# # # method 2
# # # ndcg
# # def get_dcg(y_pred, y_true, k):
# #     # 注意y_pred与y_true必须是一一对应的，并且y_pred越大越接近label=1(用相关性的说法就是，与label=1越相关)
# #     df = pd.DataFrame({"y_pred": y_pred, "y_true": y_true})
# #     df = df.sort_values(by="y_pred", ascending=False)  # 对y_pred进行降序排列，越排在前面的，越接近label=1
# #     df = df.iloc[0:k, :]  # 取前K个
# #     dcg = (2 ** df["y_true"] - 1) / np.log2(np.arange(1, df["y_true"].count() + 1) + 1)  # 位置从1开始计数
# #     dcg = np.sum(dcg)
# #
# #
# # def get_ndcg(df, k):
# #     # df包含y_pred和y_true
# #     dcg = get_dcg(df["y_pred"], df["y_true"], k)
# #     idcg = get_dcg(df["y_true"], df["y_true"], k)
# #     ndcg = dcg / idcg
# #     return ndcg
#
#
#
# # -------------------------------------------------------------------
# # # method 3
# # def dcg_k(r, k):
# #     r = np.asfarray(r)[:k]
# #     if r.size != k:
# #         raise ValueError('ranking list length < k')
# #     return np.sum(r / np.log2(np.arange(2, r.size + 2)))
# #
# #
# # def ndcg_k(r, k):
# #     sorted_r = sorted(r, reverse=True)
# #     idcg = dcg_k(sorted_r, k)
# #     if not idcg:
# #         return 0
# #     return dcg_k(r, k) / idcg
# #
# #
# # def get_ndcg(prediction, rating_matrix, k):
# #     num_user, num_item = rating_matrix.shape
# #     ndcg_overall = []
# #     for i in range(num_user):
# #         # skip the user without any rating
# #         if rating_matrix[i].sum() == 0:
# #             continue
# #         else:
# #             pred_list_index = np.argsort(-prediction[i])
# #             pred_true_rating = rating_matrix[i][pred_list_index]
# #             ndcg_overall.append(ndcg_k(pred_true_rating, k))
# #     return np.mean(ndcg_overall)
#
#
#
#
#
# #---------------------------------------------------------------------------
# # #method 4
# # import math
# #
# # import pandas as pd
# #
# # import logging
# #
# # class NDCG(object):
# #     """
# #     normalized discount cumulative gain
# #     """
# #     logger = logging.Logger().get_logger()
# #
# #     def __init__(self, topk=20):
# #         self.topk = topk
# #
# #     def error(self, comp_matrix, spar_matrix, pred_matrix):
# #         """
# #         here pred_matrix represnt the predict rating or ranking
# #         """
# #         self.logger.info(str(self.__class__.__name__) + "\t error")
# #         self.comp_matrix = comp_matrix.copy()
# #         self.pred_matrix = pred_matrix.copy()
# #         self.usernum, self.itemnum = self.comp_matrix.shape
# #         pred_usernum, pred_itemnum = self.pred_matrix.shape
# #
# #         assert self.usernum == pred_usernum
# #         assert self.itemnum == pred_itemnum
# #
# #         if self.pred_matrix.dtypes[0] == float:
# #             # predict matrix is rating
# #             ndcg_k = self.rating_ndcg(self.comp_matrix, self.pred_matrix)
# #         else:
# #             # predict matrix is ranking
# #             ndcg_k = self.ranking_ndcg(self.comp_matrix, self.pred_matrix)
# #         return ndcg_k
# #
# #
# #     def rating_ndcg(self, comp_matrix, pred_matrix):
# #         """
# #         change the ranking prediction to ranking in order to calculate the ndcg-k
# #         """
# #         for user in range(self.usernum):
# #             pred_matrix.ix[user] = pred_matrix.ix[user].order(ascending=False).index
# #
# #         ndcg_k = self.ranking_ndcg(comp_matrix, pred_matrix)
# #         return ndcg_k
# #
# #
# #     def ranking_ndcg(self, comp_matrix, pred_matrix):
# #         """
# #         formula ndcg-k calculation of ranking
# #         """
# #         ndcg_vector = []
# #         for user in range(self.usernum):
# #             pred_item_index = pred_matrix.ix[user]
# #             comp_item_index = comp_matrix.ix[user].order(ascending=False).index
# #
# #             ndcg_ki = 0.
# #             idcg_ki = 0.
# #             for ki in range(1, self.topk):
# #                 log_2_i = math.log(ki, 2) if math.log(ki, 2) != 0. else 1.
# #                 ndcg_ki += comp_matrix[pred_item_index[ki]][user] / log_2_i
# #                 idcg_ki += comp_matrix[comp_item_index[ki]][user] / log_2_i
# #
# #             ndcg_ki = ndcg_ki / idcg_ki
# #             ndcg_vector.append(ndcg_ki)
# #
# #             if user == 0:
# #                 self.logger.debug("ndcg_ki_vector %s", ndcg_vector)
# #
# #         ndcg_k = pd.Series(ndcg_vector).sum() / self.usernum
# #         return ndcg_k
# change this if using K > 100
denominator_table = np.log2( np.arange( 2, 102 ))
def dcg_at_k( r, k, method = 1 ):
	"""Score is discounted cumulative gain (dcg)
	Relevance is positive real values.  Can use binary
	as the previous methods.
	Example from
	http://www.stanford.edu/class/cs276/handouts/EvaluationNew-handout-6-per.pdf
	>>> r = [3, 2, 3, 0, 0, 1, 2, 2, 3, 0]
	>>> dcg_at_k(r, 1)
	3.0
	>>> dcg_at_k(r, 1, method=1)
	3.0
	>>> dcg_at_k(r, 2)
	5.0
	>>> dcg_at_k(r, 2, method=1)
	4.2618595071429155
	>>> dcg_at_k(r, 10)
	9.6051177391888114
	>>> dcg_at_k(r, 11)
	9.6051177391888114
	Args:
		r: Relevance scores (list or numpy) in rank order
			(first element is the first item)
		k: Number of results to consider
		method: If 0 then weights are [1.0, 1.0, 0.6309, 0.5, 0.4307, ...]
				If 1 then weights are [1.0, 0.6309, 0.5, 0.4307, ...]
	Returns:
		Discounted cumulative gain
	"""
	r = np.asfarray(r)[:k]
	if r.size:
		if method == 0:
			return r[0] + np.sum(r[1:] / np.log2(np.arange(2, r.size + 1)))
		elif method == 1:
			# return np.sum(r / np.log2(np.arange(2, r.size + 2)))
			return np.sum(r / denominator_table[:r.shape[0]])
		else:
			raise ValueError('method must be 0 or 1.')
	return 0.

# ndcg with explicitly given best and worst possible relevances
# for recommendations including unrated movies
def get_ndcg_2(r, best_r, worst_r, k, method=1):
    dcg_max = dcg_at_k(sorted(best_r, reverse=True), k, method)

    if worst_r == None:
        dcg_min = 0.
    else:
        dcg_min = dcg_at_k(sorted(worst_r), k, method)

    # assert( dcg_max >= dcg_min )

    if not dcg_max:
        return 0.

    dcg = dcg_at_k(r, k, method)

    # print dcg_min, dcg, dcg_max

    return (dcg - dcg_min) / (dcg_max - dcg_min)


import numpy as np
from sklearn.metrics import ndcg_score

def getRatingMatrix(filename):
    data = []
    data_fo = []
    feature = []
    with open(filename) as file:
        for line in file:
            d = line[:-1].split(",")
            list1 = [int(x) for x in d[:-1]]
            list2 = [int(x) for x in d[-1].split(" ")]

            data.append(list1)
            data_fo.append(list2)
            for i in list2:
                feature.append(i)
    data = np.array(data)
    # data_fo = np.array(data_fo)

    num_users = data[:, 0].max() + 1
    num_items = data[:, 1].max() + 1
    num_features = max(feature) + 1
    # print num_features

    # create rating matrix, and user_opinion, item_opinion matrices
    # user_opinion: user preference for each feature
    # item_opinion: item performance on each feature
    rating_matrix = np.zeros((num_users, num_items), dtype=float)
    user_opinion = np.full((num_users, num_features), np.nan)
    item_opinion = np.full((num_items, num_features), np.nan)
    # update the matrices with input data
    # get the accumulated feature opinion scores for users and items.
    for i in range(len(data)):
        user_id, item_id, rating = data[i]
        # print type(data_fo)
        rating_matrix[user_id][item_id] = rating
        num_pos = 0
        num_neg = 0
        for j in range(0, len(data_fo[i]), 2):
            # for user, count the frequency
            # print data_fo[i][j]
            if np.isnan(user_opinion[user_id][data_fo[i][j]]):
                user_opinion[user_id][data_fo[i][j]] = 1
            else:
                user_opinion[user_id][data_fo[i][j]] += 1
            # for item, count the sentiment score
            if np.isnan(item_opinion[item_id][data_fo[i][j]]):
                item_opinion[item_id][data_fo[i][j]] = data_fo[i][j + 1]
            else:
                item_opinion[item_id][data_fo[i][j]] += data_fo[i][j + 1]

    return rating_matrix, user_opinion, item_opinion


if __name__ == "__main__":
    test_file = "./data/yelp_test.txt"
    pred_rating_file = "./results/pred_rating.txt"
    # test on test data with the trained model
    print ("********** Load test data **********")
    test_rating, user_opinion_test, item_opinion_test = getRatingMatrix(test_file)
    print ("Number of users", test_rating.shape[0])
    print ("Number of items", test_rating.shape[1])

    print ("*********** Loading pred_rating data *************")
    pred_rating = np.loadtxt(pred_rating_file)
    print ("*********** complete Load **************")
    # get the NDCG results
    print ("********** NDCG **********")
    true_relevance = np.asarray([[10, 0, 0, 1, 5]])
    scores = np.asarray([[.1, .2, .3, 4, 70]])
    print(type(true_relevance))
    print(ndcg_score(true_relevance, scores))

    print(type(test_rating),type(np.asarray(pred_rating_file)))
    print (ndcg_score(test_rating,np.asarray(pred_rating)))