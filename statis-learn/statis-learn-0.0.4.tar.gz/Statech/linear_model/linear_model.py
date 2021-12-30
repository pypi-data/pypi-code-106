import pandas as pd
import numpy as np
from typing import Union
import itertools
from ._base import LinearModel, RegressorMixin
from sklearn.linear_model import LinearRegression

from ..pojo.errors import AlgorithmError


class LinearRegression(RegressorMixin, LinearModel):
    def fit(self, X, y):
        X, y = self._validate_data(X, y)
        theta = np.linalg.inv(X.T.dot(X)).dot(X.T).dot(y.T)
        self._set_intercept(theta)
        self._set_coef(theta)
        return self

    def _check_empty(self, arr):
        pass


class HierarchicalRegression(RegressorMixin, LinearModel):

    def _check_empty(self, arr):
        if not arr.get('layers', None):
            raise AlgorithmError("数据缺失")
        return arr['layers']

    def fit(self, X, y, **kwargs):
        k = 0
        layers = self._check_empty(kwargs)
        for step in layers:
            k += step
            # 回归
            reg = LinearRegression()
            x_constant = reg.add_constant(X.iloc[:, 0:k])
            self._set_multi_model(reg.fit(x_constant, y))
        return self

    def score(self, X: Union[pd.DataFrame, np.ndarray], y: Union[pd.Series, np.ndarray], **kwargs) -> pd.DataFrame:
        layers = self._check_empty(kwargs)
        n, m = X.shape
        k, ssr_old = 0, 0
        result = {}
        f_change_value = pd.Series(0, name='F_change').astype(float)
        f_p_value = pd.Series(0, name='F_change_p').astype(float)
        for model, step, j in zip(self.multi_model_, layers, range(m)):
            k += step
            # 普通值
            score = model.score(X.iloc[:, 0:k], y)
            y_pred = model.predict(X.iloc[:, 0:k])
            # 计算f增量
            from Statech.metrics import ssr, mse, f_change, f_p
            mse_value = mse(y.values, y_pred, n, k)
            ssr_new = ssr(y.values, y_pred)
            f_change_value[0] = f_change(ssr_old, ssr_new, mse_value, step)
            f_p_value[0] = f_p(f_change_value, step, n, k)
            ssr_old = ssr_new
            # 结果
            result['layer' + str(j)] = [score[0], pd.concat([score[1], f_change_value, f_p_value], axis=1)]
        return result


class MediatingEffect(RegressorMixin, LinearModel):

    def _check_empty(self, arr):
        if arr.get('m', None) is None:
            raise AlgorithmError("数据缺失")
        control = arr.get('c', None)
        return arr['m'], control

    def fit(self, X, y, **kwargs):
        # 设置变量
        x = X.copy()
        m, c = self._check_empty(kwargs)
        if c is not None:
            x = pd.concat([c, x], axis=1)

        # x->y
        reg = LinearRegression()
        x_constant = reg.add_constant(x)
        self._set_multi_model(reg.fit(x_constant, y))

        # x->m
        for i in range(m.shape[1]):
            y_m = m.iloc[:, i]
            reg = LinearRegression()
            self._set_multi_model(reg.fit(x_constant, y_m))

        # x_m->y
        x = pd.concat([x, m], axis=1)
        reg = LinearRegression()
        x_constant = reg.add_constant(x)
        self._set_multi_model(reg.fit(x_constant, y))
        return self

    def score(self, X: Union[pd.DataFrame, np.ndarray], y: Union[pd.Series, np.ndarray], **kwargs) -> pd.DataFrame:

        m, c = self._check_empty(kwargs)
        x = X.copy()
        xcol = X.shape[1]
        mcol = m.shape[1]
        if c is not None:
            x = pd.concat([c, x], axis=1)
        score_1 = []
        score_2 = []

        # 计算c
        model = self.multi_model_.pop(0)
        t, r = model.score(x, y)
        score_1.append(t)
        score_2.append(r)
        c_ = np.repeat(model.coef_[-xcol:], mcol)
        c_ = pd.Series(c_, name='c')

        # 计算a
        a_ = None
        for i in range(mcol):
            y_m = m.iloc[:, i]
            model = self.multi_model_.pop(0)
            t, r = model.score(x, y_m)
            score_1.append(t)
            score_2.append(r)
            a_ = model.coef_[-xcol:] if a_ is None else list(
                itertools.chain.from_iterable(zip(a_, model.coef_[-xcol:])))
        a_ = pd.Series(a_, name='a')

        # 计算b
        x = pd.concat([x, m], axis=1)
        model = self.multi_model_.pop(0)
        t, r = model.score(x, y)
        score_1.append(t)
        score_2.append(r)
        b_ = np.tile(model.coef_[-mcol:], xcol)
        b_ = pd.Series(b_, name='b')
        score_3 = pd.concat([c_, a_, b_], axis=1)
        return score_1, score_2, score_3

    def validate_result(self, xcol, mcol):
        a_ = None
        self.multi_model_.pop(0)
        for _ in range(mcol):
            model = self.multi_model_.pop(0)
            a_ = model.coef_[-xcol:] if a_ is None else list(
                itertools.chain.from_iterable(zip(a_, model.coef_[-xcol:])))
        model = self.multi_model_.pop(0)
        b_ = np.tile(model.coef_[-mcol:], xcol)
        return a_, b_

    def bootstrap_score(self,
                        X: Union[pd.DataFrame, np.ndarray],
                        y: Union[pd.Series, np.ndarray],
                        **kwargs
                        ) -> pd.DataFrame:
        from sklearn.utils import resample
        m, c = self._check_empty(kwargs)
        np.random.seed(kwargs.get('seed', 1))
        epoch = kwargs.get('epoch', 500)

        mcol = m.shape[1]
        xcol = X.shape[1]

        reg = MediatingEffect()
        boot = None
        c_boot = None
        for _ in range(epoch):
            if c is not None:
                x_boot, y_boot, m_boot, c_boot = resample(X, y, m, c)
            else:
                x_boot, y_boot, m_boot = resample(X, y, m)
            reg.fit(x_boot, y_boot, m=m_boot, c=c_boot)
            a_, b_ = reg.validate_result(xcol, mcol)
            ab = a_ * b_
            boot = ab if boot is None else np.vstack((boot, ab))
        return np.std(boot, axis=0)
