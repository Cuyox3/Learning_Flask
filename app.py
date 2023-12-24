from main import create_app
import os
#from logging import debug 

app = create_app()

app.app_context().push() #Poder entrar a las variables de la aplicacion de cualquier parte del sistema  

if __name__ == '__main__': 

    app.run(port=os.getenv("PORT"), debug=True)
