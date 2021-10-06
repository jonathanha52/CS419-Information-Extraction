def splitFile(file_path):
  data_file = open(file_path, 'r', encoding="utf-8")
  word_list = data_file.read().lower().translate(str.maketrans('', '', string.punctuation)).split()
  return word_list
