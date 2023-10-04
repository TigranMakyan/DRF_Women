from rest_framework import serializers
from .models import Women
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import io

# class WomenModel:
#     def __init__(self, title, content) -> None:
#         self.title = title
#         self.content = content 
    

# def encode():
#     model = WomenModel('Angik', 'Angelina Jolie')
#     model_sr = WomenSerializer(model)
#     print(model_sr.data, type(model_sr.data), sep='\n')
#     json = JSONRenderer().render(model_sr.data)
#     print(json)

# def decode():
#     stream = io.BytesIO(b'{"title":"Angik","content":"Angelina Jolie"}')
#     data = JSONParser().parse(stream)
#     ser = WomenSerializer(data=data)
#     ser.is_valid()
#     print(ser.validated_data)


class WomenSerializer(serializers.ModelSerializer):

    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Women
        fields = "__all__"