import spacy

nlp = spacy.load("en_core_web_sm")

def anonymize_text(sentences):
    ans = ''
    copy = nlp(sentences)
    name = [i.text for i in copy.ents if i.label_ == "PERSON"]
    print(name)
    news = sentences.split()
    for i in range(len(news)-2):
        if news[i] in name or news[i] + news[i+1] in name:
            if news[i] in name:
                tmp = ' '
                for i in range(len[news[i]]):
                    tmp += 'X'
                news[i] = tmp
            elif news[i] + news[i+1] in name :
                tmp = ' '
                for i in range(len(news[i])+len(news[i+1])):
                    tmp += 'X'
                news[i] = tmp
                news.remove[i+1]
            ans = " ".join(news)
    return ans


print(anonymize_text("This is John Stick"))
