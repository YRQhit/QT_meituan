# from models.VLE import VLEForVQA, VLEProcessor, VLEForVQAPipeline
# from PIL import Image
#
# model_name="hfl/vle-base-for-vqa"
# text= "What is the picture say?"
# image = Image.open("Picture/1311981.jpg")
#
# model = VLEForVQA.from_pretrained(model_name)
# vle_processor = VLEProcessor.from_pretrained(model_name)
# vqa_pipeline = VLEForVQAPipeline(model=model, device='cpu', vle_processor=vle_processor)
#
# vqa_answers = vqa_pipeline(image=image, question=text, top_k=5)
# print(f"Question: {text}. Answers: {vqa_answers}")



from models.VLE import VLEForVQA, VLEProcessor, VLEForVQAPipeline
from PIL import Image

model_name="hfl/vle-large-for-vqa"
text= "What is in the table?"
image = Image.open("Picture/1311981.jpg")

model = VLEForVQA.from_pretrained(model_name)
vle_processor = VLEProcessor.from_pretrained(model_name)
vqa_pipeline = VLEForVQAPipeline(model=model, device='cpu', vle_processor=vle_processor)

vqa_answers = vqa_pipeline(image=image, question=text, top_k=5)
print(f"Question: {text}. Answers: {vqa_answers}")


