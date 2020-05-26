#coding=utf-8
import numpy as np
from sklearn.preprocessing import LabelBinarizer
from sklearn.metrics import make_scorer


def dcg_score(y_true, y_score, k=5):
    """Discounted cumulative gain (DCG) at rank K.

    Parameters
    ----------
    y_true : array, shape = [n_samples]
        Ground truth (true relevance labels).
    y_score : array, shape = [n_samples, n_classes]
        Predicted scores.
    k : int
        Rank.

    Returns
    -------
    score : float
    """
    order = np.argsort(y_score)[::-1]
    y_true = np.take(y_true, order[:k])

    gain = 2 ** y_true - 1

    discounts = np.log2(np.arange(len(y_true)) + 2)
    return np.sum(gain / discounts)


def ndcg_score(ground_truth, predictions, k=5):
    """Normalized discounted cumulative gain (NDCG) at rank K.

    Normalized Discounted Cumulative Gain (NDCG) measures the performance of a
    recommendation system based on the graded relevance of the recommended
    entities. It varies from 0.0 to 1.0, with 1.0 representing the ideal
    ranking of the entities.

    Parameters
    ----------
    ground_truth : array, shape = [n_samples]
        Ground truth (true labels represended as integers).
    predictions : array, shape = [n_samples, n_classes]
        Predicted probabilities.
    k : int
        Rank.

    Returns
    -------
    score : float

    Example
    -------
    >>> ground_truth = [1, 0, 2]
    >>> predictions = [[0.15, 0.55, 0.2], [0.7, 0.2, 0.1], [0.06, 0.04, 0.9]]
    >>> score = ndcg_score(ground_truth, predictions, k=2)
    1.0
    >>> predictions = [[0.9, 0.5, 0.8], [0.7, 0.2, 0.1], [0.06, 0.04, 0.9]]
    >>> score = ndcg_score(ground_truth, predictions, k=2)
    0.6666666666
    """
    lb = LabelBinarizer()
    lb.fit(range(len(predictions) + 1))
    T = lb.transform(ground_truth)

    scores = []

    # Iterate over each y_true and compute the DCG score
    for y_true, y_score in zip(T, predictions):
        actual = dcg_score(y_true, y_score, k)
        best = dcg_score(y_true, y_true, k)
        score = float(actual) / float(best)
        scores.append(score)

    return np.mean(scores)


# -------------------------------------------------------
# NDCG Scorer function
ndcg_scorer = make_scorer(ndcg_score, needs_proba=True, k=5)

# # method 2
# # ndcg
# def get_dcg(y_pred, y_true, k):
#     # 注意y_pred与y_true必须是一一对应的，并且y_pred越大越接近label=1(用相关性的说法就是，与label=1越相关)
#     df = pd.DataFrame({"y_pred": y_pred, "y_true": y_true})
#     df = df.sort_values(by="y_pred", ascending=False)  # 对y_pred进行降序排列，越排在前面的，越接近label=1
#     df = df.iloc[0:k, :]  # 取前K个
#     dcg = (2 ** df["y_true"] - 1) / np.log2(np.arange(1, df["y_true"].count() + 1) + 1)  # 位置从1开始计数
#     dcg = np.sum(dcg)
#
#
# def get_ndcg(df, k):
#     # df包含y_pred和y_true
#     dcg = get_dcg(df["y_pred"], df["y_true"], k)
#     idcg = get_dcg(df["y_true"], df["y_true"], k)
#     ndcg = dcg / idcg
#     return ndcg



# -------------------------------------------------------------------
# # method 3
# def dcg_k(r, k):
#     r = np.asfarray(r)[:k]
#     if r.size != k:
#         raise ValueError('ranking list length < k')
#     return np.sum(r / np.log2(np.arange(2, r.size + 2)))
#
#
# def ndcg_k(r, k):
#     sorted_r = sorted(r, reverse=True)
#     idcg = dcg_k(sorted_r, k)
#     if not idcg:
#         return 0
#     return dcg_k(r, k) / idcg
#
#
# def get_ndcg(prediction, rating_matrix, k):
#     num_user, num_item = rating_matrix.shape
#     ndcg_overall = []
#     for i in range(num_user):
#         # skip the user without any rating
#         if rating_matrix[i].sum() == 0:
#             continue
#         else:
#             pred_list_index = np.argsort(-prediction[i])
#             pred_true_rating = rating_matrix[i][pred_list_index]
#             ndcg_overall.append(ndcg_k(pred_true_rating, k))
#     return np.mean(ndcg_overall)