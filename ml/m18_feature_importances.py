# 20-06-10_22 수요일 16:10~

# m17 copy
# 

from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split

cancer = load_breast_cancer()
x_train, x_test, y_train, y_test = train_test_split(
    cancer.data, cancer.target, train_size=0.8, random_state=42
)

model = DecisionTreeClassifier(max_depth=4)

model.fit(x_train, y_train)

acc = model.score(x_test, y_test)

print(model.feature_importances_)
print(acc)

import matplotlib.pyplot as plt
import numpy as np
def plot_feature_importances_cancer(model):
    n_features = cancer.data.shape[1]
    plt.barh(np.arange(n_features), model.feature_importances_, align='center')
    plt.yticks(np.arange(n_features), cancer.feature_names)
    plt.xlabel("Feature Importances")
    plt.ylabel("Features")
    plt.ylim(-1, n_features)

plot_feature_importances_cancer(model)
plt.show()

### 정리 및 과제 ###

# matplot 그래프로 분포를 확인할 수 있다
# 그렇지만 random_state에 따른 분포도 변화는 이해하기 어렵다? (m17 의문의 연장선상)

# matplot 함수로 잘 저장해놔야한다 (나중에 또 쓰인다)
# barh, ticks, lim 찾아서 주석을 적어논다
# 전체적으로 위의 plot에 대해서 분석
# Feature_importance 및 XGB 사용 데이콘 1 모델에 적용해라