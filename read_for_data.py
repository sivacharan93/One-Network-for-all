# The training and testing procedure for image caption generation uses a similar approach as that of the one used in the Image caption generation using attention tutorial by tensorflow. But our method is different in many aspects, starting with that fact that we dont use attention.


import pickle


list_data=[]

sentence_list=[]


with open("Flickr_8k.trainImages.txt", "r") as fp:   #Flickr8k.token.txt
  token_data_training = fp.readlines()

for i in range(0,len(token_data_training)):
	token_data_training[i]=token_data_training[i].strip('\n')




with open("Flickr8k.lemma.token.txt", "r") as fp:   #Flickr8k.token.txt
  token_data = fp.readlines()


for a in token_data:
	pos=a.find('.jpg#')
	i=a[:pos+4]
	j=a[pos+4:pos+6]
	k=a[pos+6:]
	k=k.strip()
	k=k.strip('.')
	k=k.strip()

	
	list_data.append([i,j,k])
	sentence_list.append(k)


pickle_out = open("sentence_list_and_reference_data_revision2.pickle","wb")
pickle.dump([list_data,sentence_list], pickle_out)
pickle_out.close()

training_indexes_from_total_training=[]

for i in range(0,len(token_data_training)):
	flag=0
	for j in range(0,len(list_data)):
		if token_data_training[i]==list_data[j][0]:
			flag=1
			training_indexes_from_total_training.append(j)
	if flag==0:
		print("missing-",token_data_training[i])

print(training_indexes_from_total_training)


pickle_out = open("training_indexes_from_total_data.pickle","wb")
pickle.dump(training_indexes_from_total_training, pickle_out)
pickle_out.close()


print(len(sentence_list))
print(len(list_data))
print(len(training_indexes_from_total_training))
