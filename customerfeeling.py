#referenece: https://learn.microsoft.com/zh-cn/azure/ai-services/language-service/sentiment-opinion-mining/quickstart?tabs=windows&pivots=programming-language-python#code-example

language_key = 'GHQu3HVecma9RB9KFlrBMScRBUcYWeDcjERIMu60zdu7ClGCNuitJQQJ99BGAC3pKaRXJ3w3AAAaACOGP1mZ'
#language_key = os.environ.get('LANGUAGE_KEY')

language_endpoint = 'https://customerfeeling.cognitiveservices.azure.com/'
#language_endpoint = os.environ.get('LANGUAGE_ENDPOINT')

# pip install azure-ai-textanalytics==5.2.0 done already
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

# Authenticate the client using your key and endpoint 
def authenticate_client():
    ta_credential = AzureKeyCredential(language_key)
    text_analytics_client = TextAnalyticsClient(endpoint=language_endpoint,credential=ta_credential)
    return text_analytics_client

def sentiment_analysis_with_opinion_mining_example(documents):

    documents = [documents]
    #Azure Text Analytics 的 analyze_sentiment() 方法
    #要求 documents 是一个字符串列表（list of strings）
    #传进来的documents，需要先转成list

    result = client.analyze_sentiment(documents, show_opinion_mining=True)
    doc_result = [doc for doc in result if not doc.is_error]

    #is_error 不是 Python 原生属性，而是 Azure Text Analytics SDK 的一个字段;排除掉doc输入进来一个空值不存在的情况

    positive_reviews = [doc for doc in doc_result if doc.sentiment == "positive"]
    negative_reviews = [doc for doc in doc_result if doc.sentiment == "negative"]

    positive_mined_opinions = []
    mixed_mined_opinions = []
    negative_mined_opinions = []

    for document in doc_result:
        print("Document Sentiment: {}".format(document.sentiment))
        print("Overall scores: positive={0:.2f}; neutral={1:.2f}; negative={2:.2f} \n".format(
            document.confidence_scores.positive,
            document.confidence_scores.neutral,
            document.confidence_scores.negative,
        ))
        for sentence in document.sentences:
            print("Sentence: {}".format(sentence.text))
            print("Sentence sentiment: {}".format(sentence.sentiment))
            print("Sentence score:\nPositive={0:.2f}\nNeutral={1:.2f}\nNegative={2:.2f}\n".format(
                sentence.confidence_scores.positive,
                sentence.confidence_scores.neutral,
                sentence.confidence_scores.negative,
            ))
            for mined_opinion in sentence.mined_opinions:
                target = mined_opinion.target
                print("......'{}' target '{}'".format(target.sentiment, target.text))
                print("......Target score:\n......Positive={0:.2f}\n......Negative={1:.2f}\n".format(
                    target.confidence_scores.positive,
                    target.confidence_scores.negative,
                ))
                for assessment in mined_opinion.assessments:
                    print("......'{}' assessment '{}'".format(assessment.sentiment, assessment.text))
                    print("......Assessment score:\n......Positive={0:.2f}\n......Negative={1:.2f}\n".format(
                        assessment.confidence_scores.positive,
                        assessment.confidence_scores.negative,
                    ))
            print("\n")
        print("\n")
          
if __name__=='__main__':
    client = authenticate_client()#主程序开始，先authentication
    customer_input = input("What did your customer say?") #ask for custmomer feeling
    sentiment_analysis_with_opinion_mining_example(customer_input)

