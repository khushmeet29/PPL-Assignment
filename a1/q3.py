print("To block certain websites from opening. eg- www.facebook.com")

host_path = r"/etc/hosts"  
redirect = "127.0.0.1"  
websites = ["www.facebook.com", "https://www.facebook.com"]  
while True:  
        with open(host_path,"r+") as fileptr:  
            content = fileptr.read()  
            for website in websites:  
                if website in content:
                    print("Website is already blocked")  
                    pass  
                else:  
                    fileptr.write(redirect+"        "+website+"\n") 
                    print("Website blocked") 

