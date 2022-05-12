# # def on_generation(ga_instance):
# #     return
import math
import re
from collections import Counter

WORD = re.compile(r"\w+")


def get_cosine(vec1, vec2):
    intersection = set(vec1.keys()) & set(vec2.keys())
    numerator = sum([vec1[x] * vec2[x] for x in intersection])

    sum1 = sum([vec1[x] ** 2 for x in list(vec1.keys())])
    sum2 = sum([vec2[x] ** 2 for x in list(vec2.keys())])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)
    print(numerator)
    if not denominator:
        return 0.0
    else:
        return float(numerator) / denominator

def text_to_vector(text):
    words = WORD.findall(text)
    print(len(words))
    return Counter(words)


text1 = "Chuẩn bị tài liệu Nhật NetK"
text2 = "tài liệu Nhật NetK"

vector1 = text_to_vector(text1)
vector2 = text_to_vector(text2)




cosine = get_cosine(vector1, vector2)

print("Cosine:", cosine)