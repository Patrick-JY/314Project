import src.pulling_logic as pulling_logic
# Checks if github workflow is working by just doing a simple auto succeed test


def test_github():
    pass

# Checks the amazon data pulling from the amazon data sets


def test_amazon_pulling():
    pulling_logic.pulling_amazon("reviews_Amazon_Instant_Video_5.json.gz")
    pass
