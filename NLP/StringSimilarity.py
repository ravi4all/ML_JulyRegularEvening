text_1 = "Machine learning (ML) is a category of algorithm that allows software applications to become more accurate in predicting outcomes without being explicitly programmed. The basic premise of machine learning is to build algorithms that can receive input data and use statistical analysis to predict an output while updating outputs as new data becomes available."
text_2 = "Machine learning is an application of artificial intelligence (AI) that provides systems the ability to automatically learn and improve from experience without being explicitly programmed. Machine learning focuses on the development of computer programs that can access data and use it learn for themselves."

def textFormatting(text):
    # Step-1 : Tokenization
    token = text.split()

    # print(token)

    for i in range(len(token)):
        token[i] = token[i].lower()

    # print(token)

    # Step-2 : Remove Stopwords
    stopwords = ['is','am','are','and','the','it','as',
                 'has','that','in','of','to','an','can',
                 'for','from','being','a','while', 'more']

    words = []
    for word in token:
        if word not in stopwords:
            words.append(word)

    # print(words)
    for i in range(len(words)):
        if words[i].endswith("."):
            words[i] = words[i].replace(".","")
        elif words[i].endswith(","):
            words[i] = words[i].replace(",","")

    # print(words)
    return words

def findSimilarity(text_1,text_2):

    set_1, set_2 = set(textFormatting(text_1)), set(textFormatting(text_2))

    numer = set_1.intersection(set_2)
    denom = set_1.union(set_2)

    j = len(numer) / len(denom)

    return j

similarity = findSimilarity(text_1, text_2)
print("Similarity is",round(similarity*100,2),"%")