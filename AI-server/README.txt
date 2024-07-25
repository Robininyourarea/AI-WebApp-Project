# How to run the code:

1.create virtual environment (in this case use python 3.10)

	py -3.10 -m venv venv

2.Activate virtual environment 

	cd .\venv\

	cd .\Scripts\ 

	.\activate 

	cd .. 

	cd ..

3.Install Dependencies
	
	pip install -r requirements.txt

4.Install torch & torchvision packages

    pip3 install torch torchvision --index-url https://download.pytorch.org/whl/cu121

5.Run code (open AI server) 
    python aiservermaster.py