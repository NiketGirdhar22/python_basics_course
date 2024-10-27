import xml.dom.minidom

def main():
    doc = xml.dom.minidom.parse("samplexml.xml")
    print(doc.nodeName)
    print(doc.firstChild.tagName)

    skills = doc.getElementsByTagName("skill")
    print(skills.length," skills are listed")
    for i in skills:
        print(i.getAttribute("name"))

    newSkill = doc.createElement("skill")
    newSkill.setAttribute("name","jQuery")
    doc.firstChild.appendChild(newSkill)

    skills = doc.getElementsByTagName("skill")
    print(skills.length," skills are listed")
    for i in skills:
        print(i.getAttribute("name"))

if __name__ == "__main__":
    main()