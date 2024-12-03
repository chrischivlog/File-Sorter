import os

#origin filepath wo das zeug ist
file_path = "/Volumes/title/unsorted/"

files = os.listdir("/Volumes/title/unsorted/")

for f in files: 
    
    # filtere den wert der endung heraus
    file_name, file_ext = os.path.splitext(f)
    orginal_file_name = file_name + file_ext
    
    # nimm nun das file und sortiere es anhand der endung in den korrekten ordner
    
    if file_ext == ".txt":
            origin_folder = file_path + orginal_file_name
            desti_folder = file_path + "/txt/" + orginal_file_name
            print(origin_folder)
            os.replace(f"{origin_folder}", f"{desti_folder}")
            
    elif file_ext == ".mov":
            origin_folder = file_path + orginal_file_name
            desti_folder = file_path + "/mov/" + orginal_file_name
            print(origin_folder)
            os.replace(f"{origin_folder}", f"{desti_folder}")
            
    elif file_ext == ".png":
            origin_folder = file_path + orginal_file_name
            desti_folder = file_path + "/png/" + orginal_file_name
            print(origin_folder)
            os.replace(f"{origin_folder}", f"{desti_folder}")    
            
    elif file_ext == ".jpg":
            origin_folder = file_path + orginal_file_name
            desti_folder = file_path + "/jpg/" + orginal_file_name
            print(origin_folder)
            os.replace(f"{origin_folder}", f"{desti_folder}")      
              
    elif file_ext == ".zip":
            origin_folder = file_path + orginal_file_name
            desti_folder = file_path + "/zip/" + orginal_file_name
            print(origin_folder)
            os.replace(f"{origin_folder}", f"{desti_folder}")    
            
    elif file_ext == ".mp4":
            origin_folder = file_path + orginal_file_name
            desti_folder = file_path + "/mp4/" + orginal_file_name
            print(origin_folder)
            os.replace(f"{origin_folder}", f"{desti_folder}")  
              
    elif file_ext == ".java":
            origin_folder = file_path + orginal_file_name
            desti_folder = file_path + "/java/" + orginal_file_name
            print(origin_folder)
            os.replace(f"{origin_folder}", f"{desti_folder}")   