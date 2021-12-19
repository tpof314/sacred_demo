mongodb:
	docker run -p 27017:27017 -d mongo:4.2.18-rc0-bionic

pull_mongo:
	docker pull mongo

omniboard:
	omniboard -m localhost:27017:sacred
