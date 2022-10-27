# Application streamlit analyse de données

https://amine-alami-h3python-myapp-8vvgxt.streamlitapp.com/

## Docker cheat sheet

# installer docker
	apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin		
    docker --version

# construire une image docker
	docker build [-f <file name> optionnal] -t <app name>:<version/tag default: "latest"> .		
# lancer l'image
	docker run -d -p <docker port>:<host port> <app name>:<version/tag>	

# lister toutes les images
	docker images	
# lister toutes les instances d'images (containers)
	docker ps -a	
# lister les images actives
	docker ps	
# afficher les logs d'une image
	docker logs <image ID>	