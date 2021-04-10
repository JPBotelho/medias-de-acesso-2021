from bs4 import BeautifulSoup
import requests
import time
#from typing import namedtuple


#class Course(NamedTuple):
#    codigoEscola : int
#    nomeEscola : str
#    codigoCurso : str
#    nomeCurso : str 
#    tipoCurso : str

def main():
    print("test")
    downloadURL = "https://www.dges.gov.pt/guias/indest.asp"
    data = requests.get(downloadURL)
    print(data)
    soup = BeautifulSoup(data.text, 'html.parser')
    courses = list(soup.findAll(attrs={'class': 'lin-ce'}))
    print (len(courses))

    sectionHeaders = soup.findAll(attrs={'class': 'box9'})
    for sectHeader in sectionHeaders:
        currentSection = sectHeader.findChildren(attrs={'class': 'lin-area-d2'})
        print("\n" + currentSection[0].text + "\n")
        for sibling in sectHeader.findNextSiblings():
            if('class' in sibling.attrs):
                if "box9" in sibling.attrs["class"]:
                    break
                courseName = sibling.findChildren("a")
                for child in courseName:
                    print(child.getText())
            
            


    
if __name__ == '__main__':
    main()