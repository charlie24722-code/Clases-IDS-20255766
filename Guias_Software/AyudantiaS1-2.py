correo = input()

print(correo.count("@") >= 1 and correo.find("@") >= 3 and len(correo) - correo.find("@") -1>= 3 and "." in correo and " " not in correo and not correo.startswith(".") and not correo.endswith("."))
    
    
