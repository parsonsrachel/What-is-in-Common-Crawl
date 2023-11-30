from google.cloud import language_v1, language_v2

def classify(text, verbose=False):
    """Classify the input text into categories."""

    language_client = language_v2.LanguageServiceClient()

    document = language_v2.Document(
        content=text, type_=language_v2.Document.Type.PLAIN_TEXT
    )

    result = {}
    try:
        response = language_client.classify_text(request={"document": document})
        categories = response.categories
    except:
        try:
            # If it didn't work try Language model v1
            language_client = language_v1.LanguageServiceClient()
            document = language_v1.Document(content=text, type_=language_v1.Document.Type.PLAIN_TEXT)
            response = language_client.classify_text(request={"document": document})
            categories = response.categories
        except:
            return result

    for category in categories:
        # Turn the categories into a dictionary of the form:
        # {category.name: category.confidence}, so that they can
        # be treated as a sparse vector.
        result[category.name] = category.confidence

    if verbose:
        print(text)
        for category in categories:
            print("=" * 20)
            print("{:<16}: {}".format("category", category.name))
            print("{:<16}: {}".format("confidence", category.confidence))

    return result
