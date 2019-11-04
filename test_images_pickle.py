import pickle


list_test_image_names=[]



with open("Flickr_8k.testImages.txt", "r") as fp:   #Flickr8k.token.txt
  token_data = fp.readlines()



for i in range(len(token_data)):
	token_data[i]=token_data[i].strip('\n')

print(len(token_data))
print(token_data)


pickle_out = open("test_image_names_revised.pickle","wb")
pickle.dump(token_data, pickle_out)
pickle_out.close()
