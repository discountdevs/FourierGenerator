from js import console, alert
import numpy, json

def initLogs():
  Element('log').element.innerHTML = "Log:"

def log(text):
  console.log(str(text))
  Element('log').element.innerHTML = Element('log').element.innerHTML + "<br>" + str(text)
  return True

def main(*args, **kwargs):
  initLogs()
  text = Element('coordinates').element.value
  try:
    list = json.loads(text)
  except:
    alert("input was not a well-formed JSON list, make one at https://spotify.github.io/coordinator/")
    return False;
 
  #Code start
  imaginaryList = []
  Length = len(list)
  vectors = int(Element("vCount").element.value)
  #Conver to imaginary
  log("Converting to imaginary...")
  for coords in list:
    x = coords[0]
    y = coords[1]  
    iCoord = numpy.complex(x,y)
    imaginaryList.append(iCoord)
  
  #Apply fourier transform
  log("Applying Fourier Tranform...")
  fourierList = []
  for v in range(-int(numpy.floor(vectors/2)),int(numpy.floor(vectors/2)) + 1):
    vector = []
    z = 0
    for comp in imaginaryList:
      z = z + (1/len(imaginaryList))
      part = comp * (numpy.e ** ((-v) * 2 * numpy.pi * 1j * z)) * (1/len(imaginaryList))
      vector.append(part)
    vector2 = numpy.sum(vector)
    vector = []
    fourierList.append(vector2)
    vector2 = []

  #Rearrange
  log("Rearanging...")
  vectors = Element("vCount").element.value
  rearrange = generateRearrange(vectors)
  fourierList = [fourierList[e] for e in rearrange]

  #Get Args
  argList = []
  for argument in fourierList:
    argList.append(numpy.angle(argument))
  
  
  #Get Radii
  log("Getting Radii...")
  radiiList = []
  for rad in fourierList:
    radiiList.append(numpy.abs(rad))
  
  #Print list
  Element('radii').element.innerHTML = str(radiiList)
  Element('angles').element.innerHTML = str(argList)

def generateRearrange(vectorCount):
  origList = range(int(numpy.floor(0.5 * float(vectorCount))) + 1)
  newList = []
  for element in origList:
    # list output should be [-1,0,-2,1,-3,2,-4,3,-5,4,-6,5,-7,6...]
    if element != 0:
      newList.append(element * -1)
      newList.append(element)
    else:
      newList.append(element)   
  newnewList = []
  for g in newList:
    ge = g + int(numpy.floor(0.5 * float(vectorCount)))
    newnewList.append(ge)
  return newnewList