import copy
#import collections.defaultdict
import itertools

inputFileObject = open("input.txt", "r")
outputFileObject = open("output.txt", "w")

operators=['or','not']
queryNum = int(inputFileObject.readline().strip())
queryList = []
for i in range(queryNum):
	query = inputFileObject.readline().strip()
	query = query.replace(" ","")
	queryList.append(query)

print queryList
knowledgeBaseNum = int(inputFileObject.readline().strip())
kbList = []
for i in range(knowledgeBaseNum):
	sentence = inputFileObject.readline().strip().replace(" ","")
	kbList.append(sentence)

print kbList

def negate(current_str):
	if current_str[0]=='~':
		current_str=current_str[1:]
	else:
		current_str='~'+current_str
	return current_str

def findPredicate(current_str):
	temp=list(current_str)
	#temp=current_str.split('(')
	if temp[0]=='~':
		flag=1
		return temp[1],flag
	else:
		flag=0
		return temp[0],flag

def findArguments(current_predicate):
	for i in range(len(current_predicate)):
		if current_predicate[i] == '(':
			current_predicate = current_predicate[i + 1:len(current_predicate) - 1]
			break

	args = current_predicate.split(',')
	return args

def isCapitalAlphabet(c):
    if(c >= 'A' and c <= 'Z'):
        return True
    return False
def isVar(c):
	if isinstance(c, str) and len(c) == 1 and c.islower():
		return True
	else:
		return False


def unification(args1,args2):

	substitute={}
	for l1,l2 in zip(args1,args2):
		if  isVar(l1) and isCapitalAlphabet(l2):
			substitute[l1]=l2
		elif isVar(l2) and isCapitalAlphabet(l1):
			substitute[l2]=l1
		elif isCapitalAlphabet(l1) and isCapitalAlphabet(l2) and l1!=l2:
			return {}
		elif isVar(l1) and isVar(l2):
			substitute[l1]=l2

	return substitute


def add_query(str1,str2,each_predicate1,each_predicate2,unified_variables):
	'''
	new_kb_query=str1+str2
	new_kb_query=new_kb_query.replace(each_predicate1,'')
	new_kb_query=new_kb_query.replace(each_predicate2,'')
	new_kb_query=new_kb_query.replace('|','')

	for var1,var2 in unified_variables.items():
		new_kb_query=new_kb_query.replace(var1,var2)
	'''
	new_kb_query=''
	#print str1,str2
	temp_list=str1+str2
	#print temp_list
	for m in temp_list:
		if m!=each_predicate1 and m!=each_predicate2:
			new_kb_query+=m+'|'
	new_kb_query=new_kb_query[:-1]

	for var1,var2 in unified_variables.items():
		new_kb_query=new_kb_query.replace(var1,var2)

	return new_kb_query


for each_query in queryList:

	query_prove=negate(each_query)
	print 'negated query',query_prove

	temp_query = query_prove
	while(len(copy_kbList)):
		copy_kbList = copy.deepcopy(kbList)
		copy_kbList.append(temp_query)
		for sentence in copy_kbList:

			print sentence
			split_sentence1 = temp_query.split('|')
			split_sentence2 = sentence.split('|')

			for each_predicate1,each_predicate2 in itertools.product(split_sentence1,split_sentence2):

				predicate1, flag1 = findPredicate(each_predicate1)
				predicate2,flag2=findPredicate(each_predicate2)
				print predicate1,flag1
				print predicate2,flag2
				if predicate1==predicate2 and flag1!=flag2:
					'''Call to unification'''
					args1=findArguments(each_predicate1)
					args2=findArguments(each_predicate2)
					unified_variables=unification(args1,args2)

					if len(unified_variables)!=0:
						#print unified_variables
						new_kb_query=add_query(split_sentence1,split_sentence2,each_predicate1,each_predicate2,unified_variables)
						if new_kb_query=='':
							print '  #### TRUE #####'

						print new_kb_query
						temp_query=new_kb_query
						copy_kbList.append(new_kb_query)
						copy_kbList.remove(sentence)
						copy_kbList.remove(temp_query)
						print copy_kbList
						break


		break
	#break



