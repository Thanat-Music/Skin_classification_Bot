from transformers import ViTImageProcessor, AutoModelForImageClassification
from torch import argmax

class classifier():
    def __init__(self):
        model_path = "google-vit-base-patch16-224-ISICmod-19k/10epcoh"
        self.extractor = ViTImageProcessor.from_pretrained(model_path)
        self.model = AutoModelForImageClassification.from_pretrained(model_path)
        self.id2lable = {
                        '0': 'Basal cell carcinoma',
                        '1': 'Benign keratosis',
                        '2': 'Melanoma',
                        '3': 'Melanocytic nevus',
                        '4': 'Normal',
                        '5': 'Squamous cell carcinoma',
                        '6': 'Undefined'
                        }

    def classify(self,image):
        inputs = self.extractor(images=image, return_tensors="pt")
        outputs = self.model(**inputs)
        logits = outputs.logits
        print("logits : ",logits)
        predicted_class = argmax(logits, dim=1).item()
        output = self.id2lable[str(predicted_class)]
        return output