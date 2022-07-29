import os
import urllib.request
from nudenet.classifier import Classifier

# initialize classifier (downloads the checkpoint file automatically the first time)
classifier = Classifier()

def predict(images, batch_size=32):
    if not images:
        return None
    result = classifier.classify(images, batch_size=batch_size)
    return result

def predict_web_image(url):
    if url is None:
        return None
    if not os.path.exists('tmp'):
        os.makedirs('tmp')
    file = 'tmp/' + os.path.basename(url)
    urllib.request.urlretrieve(url, file)
    result = predict(file)
    result = round(result.get(file).get('unsafe') * 100, 2)
    if os.path.exists(file):
        os.remove(file)
    return result
