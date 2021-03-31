class GlobalData:
    incomingString = '' 
    resultString = '' 
    parametersString = [] 
    counter = 0
    status = 0
def addLine(command,text):
    if command[1] != ' ': return text
    text += command[2:]
    return text
def delSymbol(command,text):
    if command[1] != ' ' or command[2:].isdigit() == False: return text
    GlobalData.incomingString ='2 ' + text[len(text)-int(command[2:]):]
    if int(command[2:]) >= len(text): 
        text = '' 
        return text
    text = text[:len(text)-int(command[2:])]
    return text
def symbolPrint(command,text):
    if command[1] != ' ' or command[2:].isdigit() == False: return text 
    if int(command[2:]) >= len(text):
        text = '' 
        return text
    text = text[int(command[2:])]
    return text
def undo(command,text):
    if len(command) > 1: return text
    if len(GlobalData.parametersString) == GlobalData.counter: return text
    GlobalData.counter +=1
    lineUndo = GlobalData.parametersString[len(GlobalData.parametersString) - GlobalData.counter]
    if lineUndo[0] == '1' and lineUndo[1] == ' ':
        text = text[:len(text)-len(lineUndo[2:])]
    else:
        text = text + lineUndo[2:]
    
    return text
def redo(command,text):
    if len(command) > 1: return text
    if GlobalData.counter == 0: return text    
    lineRedo = GlobalData.parametersString[len(GlobalData.parametersString) - GlobalData.counter]
    if lineRedo[0] == '1' and lineRedo[1] == ' ':
        text = text + lineRedo[2:]
    else:
        text = text[:len(text)-len(lineRedo[2:])]
    GlobalData.counter -=1
    return text
def BastShoe(command):
    text = GlobalData.resultString
    GlobalData.incomingString = command
    if command[0] in '4,5': GlobalData.status = 1
    if GlobalData.status == 1 and command[0] in '1,2':
        GlobalData.parametersString = []
        GlobalData.status = 0
        GlobalData.counter = 0
    GlobalData.incomingString = command
    if command[0] not in '1,2,3,4,5': return text 
    method =[0,addLine,delSymbol,symbolPrint,undo,redo]
    text = method[int(command[0])](command,text)
    if command[0] != '3': GlobalData.resultString = text
    if command[0] not in '3,4,5': GlobalData.parametersString.append(GlobalData.incomingString)
    return text