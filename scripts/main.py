import socket
import collections
import os
import string


data_dir = "/home/data/"
output_dir = "/home/output/"
file1 = "IF.txt"
file2 = "Limerick-1.txt"
output_file = "result.txt"


# All the stdout would go into result.txt
# Thus, starting to right the output file

with open(os.path.join(output_dir, output_file), "w+") as f:

	# Listing Directories in data_dir
	dir_list = os.listdir(data_dir)
	f.write("\n1. Files in the {} directory are - {}".format(data_dir, dir_list))

	# Finding total number of words in both the files
	words_list1 = len(open(os.path.join(data_dir, file1)).read().split())
	words_list2 = len(open(os.path.join(data_dir, file2)).read().split())
	f.write("\n2. The total number of words in {} is {} and the total number of words in {} is {}.\n".format(file1, words_list1, file2, words_list2))

	# Adding the number of words
	f.write("\n3. The total number of words for {} and {} are = {}\n".format(file1, file2, words_list1, words_list2))

	# Top 3 words calculations
	counts = {}
	words = open(os.path.join(data_dir, file1)).read().split()
	for word in words:
		word = word.translate(str.maketrans("", "", string.punctuation)).capitalize()
		if word in counts:
			counts[word] += 1
		else:
			counts[word] = 1
	x = dict(sorted(counts.items(), key=lambda item: item[1],reverse=True))
	out = dict(list(x.items())[0: 3])
	f.write("\n4. The top 3 words in {} are - {}\n".format(file1, str(out)))


	# Gathering IP Address
	hostname = socket.gethostname()
	IPAddr = socket.gethostbyname(hostname)
	f.write("\n5. IP Address of your system is - {}".format(IPAddr))

f.close()

with open(os.path.join(output_dir, output_file)) as f:
	print("Below is the output of {} - \n{}\n".format(output_file, f.read()))
f.close()
