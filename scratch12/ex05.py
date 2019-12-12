import operator
import os
import random
from collections import defaultdict
from math import exp, pi, sqrt

import numpy as np

import pandas as pd
from sklearn.metrics import confusion_matrix, classification_report


class Naive_Bayes():
    def __init__(self, dataset, label_col_num=-1):
        self.df_i = dataset
        self.label_col_num = label_col_num
        self.dataset = self.change_label_to_int()
        self.arranged_list = self.label_to_end()

        print('train_test_split -> predict')

    def separate_by_class(self):
        """데이터 세트를 클래스 별로 분류한 사전(dict)를 리턴
        {class_0: [[], [], ...],
         class_1: [[], [], ...], ...}
         dataset: 리스트라고 가정.
        """
        separated = dict()  # 빈 dict를 생성
        for i in range(len(self.dataset)):  # dataset의 길이(원소의 개수)만큼 반복
            vector = self.dataset[i]  # dataset의 i번째 row(원소)
            class_value = vector[-1]  # 벡터의 가장 마지막 원소가 레이블(클래스)
            if class_value not in separated:
                # 클래스 값이 dict의 키로 존재하지 않으면
                separated[class_value] = []  # 비어 있는 리스트를 생성
            separated[class_value].append(vector)
        return separated

    def separate_by_class2(self, dataset):
        separated = defaultdict(list)  # defaultdict 객체 생성
        for i in range(len(dataset)):  # 리스트의 원소 개수만큼 반복
            vector = dataset[i]  # 리스트의 i번째 원소
            class_value = vector[-1]  # 리스트의 마지막 원소는 클래스(레이블)
            # 클래스를 key를 갖는 리스트에 vector를 추가
            separated[class_value].append(vector)
        return separated

    def summarize_dataset(self, dataset):
        """데이터 세트의 각 컬럼(변수, 특성)의 평균과 표준 편차들을 계산, 리턴
        [(mean, std, count), (), ...]
        """
        # for col in zip(*dataset):
        #     print(col)
        # *: unpacking 연산자
        #   *[1, 2] -> 1, 2
        #   *[[1,2], [3,4]] -> [1,2], [3,4]
        # zip(*[[1,2], [3,4]]) -> zip([1,2], [3,4]) -> [1, 3], [2, 4]
        summaries = [(np.mean(col), np.std(col), len(col))
                     for col in zip(*dataset)]
        # 마지막 컬럼은 데이터가 아니라 클래스(레이블)이므로 평균, 표준편차가 필요 없음
        del summaries[-1]  # 리스트의 마지막 원소를 삭제
        return summaries

    def summarize_by_class(self, dataset):
        """데이터 세트의 컬럼(변수, 특성)들에 대해서, 각 클래스 별로
        평균, 표준 편차, 개수 요약
        {class_0: [(x1_mean, x1_std, x1_len), (x2_mean, x2_std, x2_len), ...],
         class_1: [(x1_mean, x1_std, x1_len), (x2_mean, x2_std, x2_len), ...],
         ...}
        """
        # 데이터 세트를 클래스 별로 분류
        separated = self.separate_by_class2(dataset)
        summaries = dict()
        for class_value, vectors in separated.items():
            summaries[class_value] = self.summarize_dataset(vectors)
        return summaries

    def calculate_probability(self, x, mu, sigma):
        """Gaussian Normal Distribution"""
        exponent = exp(-(x - mu) ** 2 / (2 * sigma ** 2))
        return (1 / (sqrt(2 * pi) * sigma)) * exponent

    def calculate_class_probability(self, summaries, vector):
        """주어진 vector의 각 클래스별 예측값을 계산
        P(class|x1,x2) ~ P(class) * P(x1|class) * P(x2|class)
        """
        total_rows = sum([vectors[0][2] for _, vectors in summaries.items()])
        probabilities = dict()
        for class_value, class_summaries in summaries.items():
            # p = P(class)
            probabilities[class_value] = class_summaries[0][2] / total_rows
            for i in range(len(class_summaries)):
                mu, sigma, count = class_summaries[i]
                # prob = P(x1|class)
                prob = self.calculate_probability(vector[i], mu, sigma)
                # p = P(class) * P(x1|class)
                probabilities[class_value] *= prob
        return probabilities


    def label_to_end(self):
        print(self.dataset.tail())
        df_without_label = self.dataset.iloc[:, :self.label_col_num]
        df_label = self.dataset.iloc[:, self.label_col_num]
        row_num = len(df_without_label)
        arranged_list = []
        temp = []
        for i in range(row_num):
            for data in df_without_label.iloc[i]:
                temp.append(data)
            temp.append(df_label.iloc[i])
            arranged_list.append(temp)
            temp = []
        return arranged_list

    def train_test_split(self, test_size):  # Ctrl + Alt + ←
        """
        X: numpy.ndarray. n x m
        y: numpy.ndarray. 원소의 개수가 n개인 1차원 배열
        len(X) == len(y) 가정.
        test_size: 0.0 ~ 1.0
        """
        X = np.asarray(self.arranged_list)
        length = len(X)
        # 인덱스를 저장하는 배열
        indices = np.array([i for i in range(length)])
        print('shuffle 전:', indices)
        # 인덱스를 임의로 섞음
        np.random.shuffle(indices)
        print('shuffle 후:', indices)
        # Train set의 개수
        cut = int(length * (1 - test_size))  # 소수점 버림
        X_train = X[indices[:cut]]  # Train set points
        X_test = X[indices[cut:]]  # Test set points
        train_label = X[indices[:cut],self.label_col_num]  # Train set points
        test_label = X[indices[cut:],self.label_col_num]  # Test set points

        return X_train, train_label, X_test, test_label

    def change_label_to_int(self):
        if type(self.df_i.iloc[0, 4]) == type(int()):
            pass
        else:
            length = len(self.df_i)
            label = []
            for row in range(length):
                label.append(self.df_i.iloc[row, 4])
            print(label)
            set_label = dict()
            for index, lbl in enumerate(list(set(label))):
                set_label[lbl] = index
            print(set_label)
            temp_label = []
            for lb in label:
                for key, item in set_label.items():
                    if lb == key:
                        temp_label.append(item)

                    else:
                        continue
            print(temp_label)
            temp_label = pd.DataFrame(temp_label)

            del self.df_i[4]
            print(self.df_i.head())
            result_df = pd.concat([self.df_i, temp_label], axis=1)
            result_df.columns = [0, 1, 2, 3, 'label']
            return result_df

    def predict(self, data):
        """테스트 세트의 예측값들의 리스트를 리턴
        [0, 1, 1, 2, 0, 0, 1, ...]"""
        summaries = self.summarize_by_class(data)  # 1 통계량요약
        result = []
        for list_ in data:

            probabilities = self.calculate_class_probability(summaries, list_)  # 각 데이터셋에 대하여 class prob. 계산
            sorted_ = sorted(probabilities.items(), key=operator.itemgetter(1),reverse=True)
            result.append(sorted_[0][0])
        return result


if __name__ == '__main__':
    iris_file = os.path.join('..', 'scratch11', 'iris.csv')
    cancer_file = os.path.join('..', 'scratch11', 'wisc_bc_data.csv')

    iris_dataset = pd.read_csv(iris_file, header=None)
    cancer_dataset = pd.read_csv(cancer_file)

    random.seed(1212)
    print(iris_dataset.tail())
    # print(len(iris_dataset))
    print(cancer_dataset.tail())
    # print(len(cancer_dataset))
    naive_iris = Naive_Bayes(iris_dataset, 4)
    X_train, X_label, y_test, y_label = naive_iris.train_test_split(test_size=0.25)
    train_result = naive_iris.predict(X_train)
    test_result = naive_iris.predict(y_test)
    print('train_result=', train_result)
    print('test_result=', test_result)
    print(confusion_matrix(test_result, y_label))
    print(classification_report(test_result, y_label))
