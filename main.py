"""
Google Translator
googletrans API 사용한 구글 번역
멋쟁이 사자처럼 "[심화] 같이 푸는 PYTHON" 강의를 참조하여 만든 번역기.
"""
from googletrans import Translator

translator = Translator()

# sentence = "안녕하세요. 이원권입니다."
sentence = input("번역 문장을 입력하세요 : ")
dest = input("어떤 언어로 번역을 원하시나요? : ")

result = translator.translate(sentence, dest)
detected = translator.detect(sentence)

print("\n============= 번역 결과 ============\n")
print(detected.lang, ":", result.origin)
print(result.dest, ":", result.text)
print("\n====================================\n")
