if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer, test

@transformer
def validate_iris(df, *args, **kwargs):
    assert not df.isnull().any().any(), "Missing values found"
    assert df['target'].nunique() == 3, "Expected exactly 3 classes"
    print("Validation passed: no missing values and exactly 3 classes")
    return df

@test
def test_validation(output, *args):
    assert not output.isnull().any().any()
    assert output['target'].nunique() == 3
