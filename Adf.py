if __name__ == "__main__":
   try:
       __import__("ADF").reg()
   except Exception as e:
       exit(str(e))