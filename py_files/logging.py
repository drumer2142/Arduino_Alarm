def log_error(file_name, errors):
    
    log_path = "logs/"+file_name+".log"

    file_append = open(log_path, "a+")
    file_append.write(errors)
    file_append.write("\n")
    file_append.close()