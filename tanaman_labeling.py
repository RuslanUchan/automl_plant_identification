import os

# example
# /home/apiweb3c/train
path = ""
folders = os.listdir(path)

key_tanaman = {
	"bk": "Bakung",
	"bm": "Bawang Merah",
	"bp": "Bunga Popi",
	"bl": "Bunga Lilin",
	"bt": "Brotowali",
    "bw": "Belimbing Wuluh",
    "ck": "Cengkeh",
    "kk": "Kumis Kucing",
    "lb": "Lidah Buaya",
	"cm": "Cabai Merah",
	"bd": "Daun Bayam Duri",
	"dd": "Daun Dewa",
	"jb": "Daun Jambu Biji",
	"ke": "Daun Kelor",
	"dk": "Daun Kemuning",
	"pc": "Daun Pacar Cina",
	"pp": "Daun Pepaya",
	"mt": "Bunga Matahari",
	"sg": "Daun Saga",
	"sl": "Daun Salam",
	"se": "Daun Seledri",
	"si": "Daun Sirih",
	"su": "Daun Sukun",
	"de": "Delima",
	"jn": "Jeruk Nipis",
	"kg": "Kangkung",
	"ky": "Kayu Manis",
	"me": "Mengkudu",
	"pm": "Putri Malu"
}

with open("data_tanaman.csv", 'w') as file_data_tanaman:
	for folder in folders:
		sub_dir_path = os.path.join(path, folder)
		files = os.listdir(sub_dir_path)

		for f in files:
			label = key_tanaman[f[:2]]
			
			# format
			# gs://{BUCKET_NAME}/{FOLDER_IN_BUCKET}
			label_links = f"gs://tanaman/tanaman/{folder}/{f},{label}\n"
			file_data_tanaman.writelines(label_links)