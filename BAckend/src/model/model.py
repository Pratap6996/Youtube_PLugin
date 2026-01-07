from transformers import AutoTokenizer,AutoModelForSequenceClassification
import torch
import torch.nn.functional as F
MODEL_NAME = "cardiffnlp/twitter-roberta-base-sentiment"
# MODEL_NAME="distilbert-base-uncased-finetuned-sst-2-english"
class my_model:
     def __init__(self):
       """
       loads Tokenizer from AutoTokenizer.from_pretrained()
       loads Model from AutoModelForSequenceClassification.from_pretrained

       """
       self.tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
       self.model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME)
       self.model.eval() 
       self.comments=" "
     def predict_sentiment(self,text):
        """

        predicts sentiment return integer
        predicted values as
        {

        (0)Negative 
        (1)Neutral
        (2)Positive
        
        }
        """
        inputs = self.tokenizer(
            text,
            return_tensors="pt",
            truncation=True,
            max_length=128)
 
        with torch.no_grad():
            outputs = self.model(**inputs)
            probs = F.softmax(outputs.logits, dim=1)

        pred_label_id = torch.argmax(probs).item()
        # confidence = probs[0][pred_label_id].item()
        return pred_label_id
        
     def return_sentiment_count(self,comments):
         self.comments=comments
         """

         Returns Sentiment count 
         
         """
         positive=0
         negative=0
         neutral=0
         for c in self.comments:
             x=self.predict_sentiment(c)
             if x==0:
                 negative+=1
             if x==1:
                 neutral+=1
             if x==2:
                 positive+=1
         return {"positive":positive,"negative":negative,"neutral":neutral}


