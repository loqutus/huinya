def upload(self, filename, DATA_DIR):
    with open(DATA_DIR + "/" + filename) as f:
        f.write(self.request.data)
