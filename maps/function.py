import numpy as np
R = 6371
def deg2rad(deg):
    return deg*(np.pi/180)

def dist(lat1, long1, lat2, long2):
    d_lat = deg2rad(lat2 - lat1)
    d_long = deg2rad(long2 - long1)
    a = np.sin(d_lat/2)**2 + np.cos(deg2rad(lat1)) * np.cos(deg2rad(lat2)) * np.sin(d_long/2)**2
    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1-a))
    return float("{:.2f}".format(R * c))

from DeepImageSearch import Load_Data, Search_Setup
def findSimilar():
    # Load images from a folder
    image_list = Load_Data().from_folder(['images'])
    # Set up the search engine, You can load 'vit_base_patch16_224_in21k', 'resnet50' etc more then 500+ models 
    st = Search_Setup(image_list=image_list, model_name='vgg19', pretrained=True, image_count=100)
    # Index the images
    st.run_index()
    # Get metadata
    metadata = st.get_image_metadata_file()
    # Plot similar images
    st.plot_similar_images(image_path='images/Experimental Cocktail Club/Image_4.jpg', number_of_images=1)
    return None
