def test_tf_idf_search_1():
    documents = [
        "cats are small animals",
        "dogs are loyal animals",
        "cats and dogs can be pets",
        "cars and bikes are vehicles",
        "trucks and cars move goods",
    ]
    query = "Are cats pets"
    assert tf_idf_search(query, documents) == "cats and dogs can be pets"

def test_tf_idf_search_2():
    documents = [
        "cats are small animals",
        "dogs are loyal animals",
        "cats and dogs can be pets",
        "cars and bikes are vehicles",
        "trucks and cars move goods",
    ]
    query = "Are cars vehicles"
    assert tf_idf_search(query, documents) == "cars and bikes are vehicles"
