from django.shortcuts import render
from .models import Location, Paris
from geopy.geocoders import Nominatim
from .function import dist, findSimilar
import pandas as pd 
import os

from .models import Image
from keras.models import load_model  # TensorFlow is required for Keras to work
from PIL import Image, ImageOps  # Install pillow instead of PIL

import numpy as np
from django.conf import settings
from django.core.files.storage import default_storage


def explore(request):
    df = pd.read_csv(os.path.join('.','notebooks', 'df_list.csv'))
    return render(request, 'explore.html', {'df': df})

def home(request):
    return render(request, 'home.html', {})

def searchbar(request):
    if request.method == 'GET':
        search = request.GET.get('search')
        post = Paris.objects.all().filter(name=search)
        obj = Paris.objects.all()
        min = 100
        for i in post:
            for x in obj:
                distance = dist(i.lat, i.lng, x.lat, x.lng)
                if distance < min and distance != 0:
                    min = distance
                    get_name = x.name
    
    context = {
            'post': post,
            'min': min,
            'get_name': get_name,
            'search': search
    }  
    return render(request, 'searchbar.html', context)

def rec(request):
    if request.method == "POST":
        file = request.FILES["imageFile"]
        file_name = default_storage.save(file.name, file)
        file_url = default_storage.path(file_name)
        dir = os.path.join('.','media')

        # Disable scientific notation for clarity
        np.set_printoptions(suppress=True)
        # Load the model
        model = load_model("keras_model.h5", compile=False)
        # Load the labels
        class_names = open("labels.txt", "r").readlines()
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
        for file in os.listdir(dir):
            img_file = os.path.join('.','media', file)
            # Replace this with the path to your image
            image = Image.open(img_file).convert("RGB")
            # resizing the image to be at least 224x224 and then cropping from the center
            size = (224, 224)
            image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)
            # turn the image into a numpy array
            image_array = np.asarray(image)
            # Normalize the image
            normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1
            # Load the image into the array
            data[0] = normalized_image_array
            # Predicts the model
            prediction = model.predict(data)
            index = np.argmax(prediction)
            class_name = class_names[index]
            get_result = str(class_name[2:])
            length = len(get_result)
            place_list = 'Bar' 
            length_true = len(place_list)
            object = Paris.objects.all()
            post = Paris.objects.all().filter(subCategory=place_list)
            # for p in object:
            #     if p.subCategory == get_result:
            #         place_list = p.name
        context = {
        'file_name': file_name,
        'file_url': file_url,
        'dir': dir,
        'get_result': get_result,
        'place_list': place_list,
        'object': object,
        'post': post,
        'length': length,
        'length_true': length_true,
        }
        return render(request, "rec.html", context)
    else:
        return render(request, "rec.html")
    return render(request, "rec.html")