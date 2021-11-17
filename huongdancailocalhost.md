
1) cai dat git
	sudo apt update
	sudo apt install git
	git --version
	1.1) cau hinh git 
		git config --global user.name "D7cThuan"
		git config --global user.email "knownleage@gmail.com"
		git config --list (kiem tra ten va email)
	git clone https://github.com/D7cThuan/carzone_gitproject.git
2) cai dat python
	sudo apt update
	sudo apt install software-properties-common
	sudo add-apt-repository ppa:deadsnakes/ppa
	sudo apt install python3.8
	sudo apt-get install libpq-dev python-dev
	sudo apt update
	sudo apt install python3-pip
3) cai dat requirements.txt
sudo apt-get install libpq-dev python-dev
	sudo apt install python3-testresources
	sudo pip3 install -r requirements.txt
4) Cai dat atom
	sudo apt update
	sudo apt install software-properties-common apt-transport-https wget
	wget -q https://packagecloud.io/AtomEditor/atom/gpgkey -O- | sudo apt-key add -
	sudo add-apt-repository "deb [arch=amd64] https://packagecloud.io/AtomEditor/atom/any/ any main"
	sudo apt install atom
5) Cai dat PostgreSQL va pgadmin4
	sudo apt update 
	sudo apt install wget curl ca-certificates 
	wget -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
	sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt/ focal-pgdg main" >> /etc/apt/sources.list.d/pgdg.list'
	sudo apt-get install postgresql postgresql-contrib
	sudo systemctl status postgresql 
	sudo su - postgres
	psql 
	\conninfo 
	sudo passwd postgres
	sudo passwd postgres
	psql -U postgres
	psql -c "ALTER USER postgres WITH PASSWORD 'Th09092000';"
	\q
	psql -c "ALTER USER postgres WITH PASSWORD 'Th09092000';"
	sudo systemctl restart postgresql 
	curl https://www.pgadmin.org/static/packages_pgadmin_org.pub | sudo apt-key add -
	sudo sh -c 'echo "deb https://ftp.postgresql.org/pub/pgadmin/pgadmin4/apt/focal pgadmin4 main" > /etc/apt/sources.list.d/pgadmin4.list' 
	sudo apt update
	sudo apt install pgadmin4 
	sudo /usr/pgadmin4/bin/setup-web.sh 
	(them server va carzone_db (PostgreSQL12))
 
 
 
6) 	sudo python3 manage.py migrate
sudo python3 manage.py loaddata project_dump.json (load database)

sudo python3 manage.py runserver
