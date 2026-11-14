from sklearn.neighbors import KNeighborsClassifier

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer, test

FEATURES = [
    'sepal length (cm)',
    'sepal width (cm)',
    'petal length (cm)',
    'petal width (cm)'
]

@transformer
def train_knn(df, *args, **kwargs):
    train_df = df[df['split'] == 'train']
    test_df = df[df['split'] == 'test'].copy()

    model = KNeighborsClassifier(n_neighbors=5)
    model.fit(train_df[FEATURES], train_df['target'])

    test_df['predicted'] = model.predict(test_df[FEATURES])
    accuracy = (test_df['predicted'] == test_df['target']).mean()

    print('KNN Test accuracy =', round(accuracy, 3))
    return {'accuracy': accuracy}

@test
def test_knn(output, *args):
    assert output['accuracy'] >= 0.8, 'KNN accuracy is below 80%'
