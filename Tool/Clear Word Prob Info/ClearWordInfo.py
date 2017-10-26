
import json
from builtins import print

in_file = open('dolphin_t6_word_prob_info.json', 'r')

data_file = in_file.read()
data = json.loads(data_file)
word_prob_info={}

dataJSON=[]

for x in data:
    temArray=[]
    for questionObject in data[x]:
        print(questionObject)
        temQuestionObjectJson={}
        # questionObjectJson=json.loads(questionObject);

        temQuestionObjectJson['index']=questionObject['index']
        temQuestionObjectJson['equation'] = questionObject['equation']
        temQuestionObjectJson['question'] = questionObject['question']
        temQuestionObjectJson['template'] = questionObject['template']
        solution_list=[]
        for ans in questionObject['ans'].split(";"):
            if ans.isdigit():
                solution_list.append(float(ans))
            else:
                solution_list.append((ans))
        temQuestionObjectJson['solution']=solution_list
        temArray.append(temQuestionObjectJson)
    word_prob_info[x]=temArray;
    print(word_prob_info[x])

#     dictJSON = {}
#     equationList=[]
#     solutionList=[]
#     dictJSON['iIndex']=x['index']
#     equationList.append(x['equation'])
#     dictJSON['lEquations']=equationList
#     dictJSON['sQuestion']=x['question']
#     solutionList.append(1)
#     dictJSON['lSolutions']=solutionList
#     dataJSON.append(dictJSON)
#
with open('dolphin_t6_word_prob_info_clear.json', 'w') as outfile:
    json.dump(word_prob_info, outfile)