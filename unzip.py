import zipfile
with zipfile.ZipFile("asl_alphabet_test.zip", 'r') as zip_ref:
    zip_ref.extractall("alphabet_test")
with zipfile.ZipFile("alphabet_train.zip", 'r') as zip_ref:
    zip_ref.extractall("alphabet_train")