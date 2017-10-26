import json
def parse(text):
    chunks = ['']
    tem = ''
    for character in text:
        if character.isdigit() or character == '.':
            tem += character # Add onto that number
        elif len(tem)>0 :
            chunks.append(tem)
            tem = ''  # This doesn't account for `1 ++ 2`.
    if len(tem) > 0:
        chunks.append(tem)
    return chunks[1:]


def parseAdvance(text):
    chunks = ['']
    tem = ''
    for character in text:
        if character.isdigit() or character == '.':
            tem += character # Add onto that number
        elif len(tem)>0 :
            chunks.append(tem)
            tem = ''
            chunks.append(character)
        else :
            chunks.append(character)# This doesn't account for `1 ++ 2`.
    if len(tem) > 0:
        chunks.append(tem)
    return chunks[1:]


print('hai')
with open('eval_linear_manual_t6.json') as json_data:
    d = json.load(json_data)
    z=1;
    word_prob=[]
    for jsonObject in d:
        newJson={}
        equationArray=jsonObject['equations'].split('\r\n')
        equations = []
        templates = []
        numbers = []
        unkn = []
        for values in equationArray:
             tem=values.split(':')
             if len(tem)>=2 and tem[0]=='equ':
                 # print(tem[1],parse(tem[1]))
                 equations.insert(len(equations),tem[1])
                 templates.insert(len(templates), tem[1])
                 numbers.extend(parse(tem[1]))
             elif len(tem)>=2 and tem[0]=='unkn':
                 # print(tem[1])
                 unkn.extend(tem[1].split(','))
        print(unkn)
        print(equations)
        print(numbers)

        replaceUnkn=['m','n','p' ,'q','x','y','z']
        for i in range(len(unkn)) :
            for j in range(len(templates)):
                templates[j]=templates[j].replace(unkn[i].replace(" ",""),replaceUnkn[i])
                print i
                equations[j]=templates[j]
        print templates
        numbers=list(set(numbers))
        replaceNumbers = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i','j','k','l','r','s','t','u','v']
        for i in range(len(numbers)) :
            for j in range(len(templates)):
                newE='';
                # print(parseAdvance(equations[j]))
                for str in parseAdvance(templates[j]) :
                    if str==numbers[i].replace(" ",""):
                        newE+=replaceNumbers[i]
                    else:
                        newE+=str
                templates[j]=newE

                # equations[j].replace(numbers[i].replace(" ",""),replaceNumbers[i])
        print templates
        newJson['index']=z
        newJson['question'] =jsonObject['text']
        temEquation=''
        temTemplate=''
        k=0
        for str in equations:
            temEquation+=str
            temTemplate+=templates[k]
            k += 1
            if k<len(equations):
                temEquation += ", "
                temTemplate+=", "

        newJson['equation']=temEquation
        newJson['template'] = temTemplate
        print newJson
        z+=1
        word_prob.append(newJson)

    with open('word_prob_eval_linear_manual_t6.json', 'w') as outfile:
        json.dump(word_prob, outfile)