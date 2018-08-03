
"""
  - python -m unittest discover -s "Calculadora Binaria"
  - python -m unittest discover -s "Cartola FC"
  - python -m unittest discover -s "Cubo Magico"
  - python -m unittest discover -s "Hipotese de Collatz"
  - python -m unittest discover -s "Jogo Rima Musical"
  - python -m unittest discover -s "Project Euller"
  - python -m unittest discover -s "Soccer Review"
"""
  
import unittest
import os

if __name__ == "__main__":
   dir_corrente = os.getcwd()
   subfolders = [dI for dI in os.listdir(dir_corrente) if os.path.isdir(os.path.join(dir_corrente,dI))]
   for folder in subfolders:
      print(folder)
      suite = unittest.TestLoader().discover(folder, pattern = "test_*.py")
      unittest.TextTestRunner(verbosity=2).run(suite)