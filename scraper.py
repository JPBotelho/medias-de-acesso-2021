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
        schoolName = currentSection[0].text
        for sibling in sectHeader.findNextSiblings():
            if('class' in sibling.attrs):
                if "box9" in sibling.attrs["class"] or "br" in sibling.name or "nobottomgap" in sibling.attrs["class"]:
                    break
                subDivs = sibling.findChildren()

                courseNumber = subDivs[1].text
                courseURL = "https://www.dges.gov.pt/guias/"+subDivs[2].next["href"]
                courseName = subDivs[3].text
                courseType = subDivs[4].text
                #courseName = sibling.findChildren("a")
                #courseDataURL = courseName[0]["href"]
                #print(courseName[0].getText())
                #print(courseDataURL)

                print("\n"+schoolName)
                print(courseName)
                print(courseNumber)
                print(courseType)
                print(courseURL)
                
            
            


    
if __name__ == '__main__':
    main()