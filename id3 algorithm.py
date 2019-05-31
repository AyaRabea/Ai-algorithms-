import numpy as np
import pandas as np
import math

age = []
pres= []
ast= []
tear= []
total_ENTROPY=[]
NL=[]
arrnode={}
node_now=None
class Node:
    name=None
    left=None
    right=None

class item:
    def __init__(self, age, prescription, astigmatic, tearRate, needLense):
        self.age = age
        self.prescription = prescription
        self.astigmatic = astigmatic
        self.tearRate = tearRate
        self.needLense = needLense


def getDataset():
    data = []
    labels = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0]
    data.append(item(0, 0, 0, 0, labels[0]))
    data.append(item(0, 0, 0, 1, labels[1]))
    data.append(item(0, 0, 1, 0, labels[2]))
    data.append(item(0, 0, 1, 1, labels[3]))
    data.append(item(0, 1, 0, 0, labels[4]))
    data.append(item(0, 1, 0, 1, labels[5]))
    data.append(item(0, 1, 1, 0, labels[6]))
    data.append(item(0, 1, 1, 1, labels[7]))
    data.append(item(1, 0, 0, 0, labels[8]))
    data.append(item(1, 0, 0, 1, labels[9]))
    data.append(item(1, 0, 1, 0, labels[10]))
    data.append(item(1, 0, 1, 1, labels[11]))
    data.append(item(1, 1, 0, 0, labels[12]))
    data.append(item(1, 1, 0, 1, labels[13]))
    data.append(item(1, 1, 1, 0, labels[14]))
    data.append(item(1, 1, 1, 1, labels[15]))
    data.append(item(1, 0, 0, 0, labels[16]))
    data.append(item(1, 0, 0, 1, labels[17]))
    data.append(item(1, 0, 1, 0, labels[18]))
    data.append(item(1, 0, 1, 1, labels[19]))
    data.append(item(1, 1, 0, 0, labels[20]))
    return data


class Feature:

    def __init__(self, name):
        self.name = name
        self.visited = -1
        self.infoGain = -1















class ID3:
    def __init__(self, features):
        self.features = features
        #self.set_Dataset()

    def set_Dataset(self):
        l=getDataset()
        global age
        global pres
        global ast
        global tear
        global total_ENTROPY
        global NL
        global arrnode

        age.clear()
        pres.clear()
        ast.clear()
        tear.clear()
        NL.clear()
        for i in range (0,len (l)):
          age.append(l[i].age)
          pres.append(l[i].prescription)
          ast.append(l[i].astigmatic)
          tear.append(l[i].tearRate)
          NL.append(l[i].needLense)
        self.cal(2)
    def cal(self,dire):
        global gain_out
        global name_feature
        global max_gain
        max_gain=-10000
        global max_name
        max_name=""
        global arr
        age_zero=[]
        press_zero=[]
        ast_zero=[]
        tear_zero=[]
        nl_zero=[]
        age_one=[]
        press_one=[]
        ast_one=[]
        tear_one=[]
        nl_one=[]

        global node_now


        for i in range(0,len(self.features)):
            if self.features[i].visited==-1:
                if self.features[i].name=='age':
                    gain_out=self.gain(age,NL)
                    name_feature='age'
                if self.features[i].name=='prescription':
                    gain_out=self.gain(pres,NL)
                    name_feature = 'prescription'
                if self.features[i].name=='astigmatic':
                    gain_out=self.gain(ast,NL)
                    name_feature = 'astigmatic'
                if self.features[i].name=='tearRate':
                    gain_out=self.gain(tear,NL)
                    name_feature = 'tearRate'
                if gain_out>max_gain:

                    max_gain=gain_out
                    max_name=name_feature

        global c
        c=0
        if dire ==2:
            N=Node()
            N.name=max_name
            arrnode[N.name]=N
            node_now=N
        elif dire==1:

            N=arrnode.get(node_now.name)
            N.right=max_name
            arrnode[node_now.name]=N
            N=Node()

            N.name=max_name
            node_now=N

            arrnode[max_name]=N
        elif dire==0:
            N=arrnode.get(node_now.name)
            N.left=max_name
            arrnode[node_now.name]=N
            N=Node()
            N.name=max_name
            node_now=N
            arrnode[max_name]=N

        for i in range(0, len(self.features)):
            if max_name==self.features[i].name:
                self.features[i].visited=0
                c+=1
        if  max_name=='age':
            arr=age.copy()
        elif max_name=='prescription':
            arr=pres.copy()
        elif max_name=='astigmatic':
            arr=ast.copy()
        elif max_name == 'tearRate':
            arr =tear.copy()
        zero=0
        one=0
        age_zero.clear()
        age_one.clear()
        press_zero.clear()
        press_one.clear()
        ast_zero.clear()
        ast_one.clear()
        tear_zero.clear()
        tear_one.clear()
        nl_zero.clear()
        nl_one.clear()
        for i in range(0,len(arr)):
            if arr[i]==0:

                age_zero.append(age[i])
                press_zero.append(pres[i])
                ast_zero.append(ast[i])
                tear_zero.append(tear[i])
                nl_zero.append(NL[i])
                zero+=1
            elif arr[i]==1:
                age_one.append(age[i])
                press_one.append(pres[i])
                ast_one.append(ast[i])
                tear_one.append(tear[i])
                nl_one.append(NL[i])
                one+=1
        a=np.unique(nl_zero)
        #print(a)
        if len(a)>1:
            age.clear()
            pres.clear()
            ast.clear()
            tear.clear()
            NL.clear()
            for i in len(0,len(age_zero)):
                age[i]=age_zero[i]
                pres[i]=press_zero[i]
                ast[i]=age_zero[i]
                tear[i]=tear_zero[i]
                NL[i]=nl_zero[i]
            self.cal(0)
        else:
            N.left=a[0];
        a = np.unique(nl_one)
      #  print(a)
        if len(a) > 1:
            age.clear()
            pres.clear()
            ast.clear()
            tear.clear()
            NL.clear()
            for i in range(0, len(age_one)):
                age.append(age_one[i])
                pres.append(press_one[i])
                ast.append(ast_one[i])
                tear.append(tear_one[i])
                NL.append(nl_one[i])
            self.cal(1)
        else:
            N.right=a[0]




    def entropy(self,column_features):
        zero = 0
        one = 0
        global entropy
        for i in range(0,len(column_features)):
            if column_features[i]==0:
                zero+=1
            elif column_features[i]==1:
                one+=1
        length=len(column_features)

        if zero/length==0 and one/length!=0:
            entropy = -(0 + ((one / length) * math.log2(one / length)));
        elif zero / length == 0 and one / length == 0:
            entropy = 0;
        elif zero/length!=0 and one/length==0:
            entropy = -(((zero / length) * math.log2(zero / length))  + 0);
        else:
            entropy = -(((zero / length) * math.log2(zero / length)) + ((one / length) * math.log2(one / length)));


        return entropy

    def gain(self,column_features,feature_NL):
        length=len(column_features)
        zero_feature_count=0
        one_feature_count=0
        zero_feature=[]
        one_feature=[]
        for i in range(0,length):
            if column_features[i]==0:
                zero_feature_count+=1
                zero_feature.append(feature_NL[i])
            elif column_features[i]==1:
                one_feature_count+=1
                one_feature.append(feature_NL[i])
        NL=self.entropy(feature_NL)
        zero_entropy=self.entropy(zero_feature)
        one_entropy=self.entropy(one_feature)
        gain_feature=NL-( ((zero_feature_count/length)*zero_entropy) + ((one_feature_count/length)*one_entropy) )
        return gain_feature



    def classify(self, input):
        # takes an array for the features ex. [0, 0, 1, 1]
        # should return 0 or 1 based on the classification
       for  i in range(0,len(self.features)):
           self.features[i].visited= -1



       self.set_Dataset()
       # for j,i in arrnode.items():
       #     print(i.name, i.left, i.right)
       global N

       for  i in arrnode:
           N=arrnode[i]
           break
       while  True:

            if N.name=='tearRate':
                if input[3]==1:
                    if N.right==0 or N.right==1:
                       return N.right
                    else:
                        N=arrnode.get(N.right)
                elif input[3]==0:
                    if N.left==0 or N.left==1:
                       return N.left
                    else:
                        N=arrnode.get(N.left)
            elif N.name=='astigmatic':
                if input[2]==1:
                    if N.right == 0 or N.right == 1:
                        return N.right
                    else:
                        N=arrnode.get(N.right)
                elif input[2]==0:
                    if N.left == 0 or N.left == 1:
                        return N.left
                    else:
                        N=arrnode.get(N.left)
            elif N.name=='prescription':
                if input[1]==1:
                    if N.right == 0 or N.right == 1:
                        return N.right
                    else:
                        N=arrnode.get(N.right)
                elif input[1]==0:
                    if N.left == 0 or N.left == 1:
                        return N.left
                    else:
                        N=arrnode.get(N.left)
            elif N.name=='age':
                if input[0]==1:
                    if N.right == 0 or N.right == 1:
                        return N.right
                    else:
                        N=arrnode.get(N.right)
                elif input[0]==0:
                    if N.left == 0 or N.left == 1:
                        return N.left
                    else:
                        N=arrnode.get(N.left)
        #pass



dataset = getDataset()
features = [Feature('age'), Feature('prescription'), Feature('astigmatic'), Feature('tearRate')]
id3 = ID3(features)
cls = id3.classify([0, 0, 1, 1])  # should print 1
print('testcase 1: ', cls)
cls = id3.classify([1, 1, 0, 0])  # should print 0
print('testcase 2: ', cls)
cls = id3.classify([1, 1, 1, 0])  # should print 0
print('testcase 3: ', cls)
cls = id3.classify([1, 1, 0, 1])  # should print 1
print('testcase 4: ', cls)



