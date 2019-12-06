from sklearn.tree import export_graphviz
import graphviz
import pandas as pd

ta = pd.read_csv('data.csv')
# train_pre = pd.read_csv('imfo2.csv')
train_pre = pd.read_csv('tr.csv')

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(train_pre, ta[['301']], test_size=0.2, random_state=13)
# X = X_test
# Y = y_test
# #
# ta = pd.read_csv('ta4.csv')
# train_pre = pd.read_csv('ta_pre4.csv')
# from sklearn.model_selection import train_test_split
# X_train, X_test, y_train, y_test = train_test_split(train_pre, ta[['classification']], test_size=0.1, random_state=11)
# X_test = X
# y_test = Y
# print(X)
# print(X_test)
check = '15'
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
tree_clf = DecisionTreeClassifier(max_depth=15,random_state=13)
tree_clf.fit(X_train, y_train)
print('Score: {}'.format(tree_clf.score(X_train, y_train)))

# with open('t.txt','w') as t:
#     # for i in tree_clf.decision_path(X_train ,check_input=True):
#     #     t.write(str(i))
#     t.writelines(str(tree_clf.decision_path(X_train ,check_input=True)))
# print(tree_clf.decision_path(X_train ,check_input=True))
# #
# feature_imp = tree_clf.feature_importances_
# #
# print('{}'.format(feature_imp))
# # print(len(feature_imp))
# fi = []
# for i in range(0,299):
#     if feature_imp[i] == 0:
#         fi.append(i)
# print(sorted(fi,reverse=True))
# print(len(fi))
export_graphviz(
        tree_clf,
        out_file=check + ".dot",
        # feature_names=['age','bp','sg','al','su','rbc','pc','pcc','ba','bgr','bu','sc','sod','hemo','pcv','rc','htn','dm','appet','pe','ane'],
        # feature_names=['rbc','pc','pcc','ba','htn','dm','appet','pe','ane','sgg','hemoo','bgrr','suu','all','buu','sodd','rcc','pcvv','scc'],
        # feature_names=['rbc', 'pc', 'pcc', 'ba', 'htn', 'dm', 'appet', 'pe', 'ane','sgg', 'hemoo', 'bgrr', 'suu', 'all', 'buu','sodd', 'rcc', 'pcvv', 'bpp', 'scc'],
        feature_names=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '90', '91', '92', '93', '94', '95', '96', '97', '98', '99', '100', '101', '102', '103', '104', '105', '106', '107', '108', '109', '110', '111', '112', '113', '114', '115', '116', '117', '118', '119', '120', '121', '122', '123', '124', '125', '126', '127', '128', '129', '130', '131', '132', '133', '134', '135', '136', '137', '138', '139', '140', '141', '142', '143', '144', '145', '146', '147', '148', '149', '150', '151', '152', '153', '154', '155', '156', '157', '158', '159', '160', '161', '162', '163', '164', '165', '166', '167', '168', '169', '170', '171', '172', '173', '174', '175', '176', '177', '178', '179', '180', '181', '182', '183', '184', '185', '186', '187', '188', '189', '190', '191', '192', '193', '194', '195', '196', '197', '198', '199', '200', '201', '202', '203', '204', '205', '206', '207', '208', '209', '210', '211', '212', '213', '214', '215', '216', '217', '218', '219', '220', '221', '222', '223', '224', '225', '226', '227', '228', '229', '230', '231', '232', '233', '234', '235', '236', '237', '238', '239', '240', '241', '242', '243', '244', '245', '246', '247', '248', '249', '250', '251', '252', '253', '254', '255', '256', '257', '258', '259', '260', '261', '262', '263', '264', '265', '266', '267', '268', '269', '270', '271', '272', '273', '274', '275', '276', '277', '278', '279', '280', '281', '282', '283', '284', '285', '286', '287', '288', '289', '290', '291', '292', '293', '294', '295', '296', '297', '298', '299', '300'],
       #  feature_names=['4', '5', '6', '8', '9', '11', '14', '16', '32', '34', '41', '45', '46',
       # '47', '48', '56', '61', '64', '69', '73', '74', '75', '76', '79', '80',
       # '81', '88', '90', '96', '101', '103', '104', '105', '107', '108', '109',
       # '110', '111', '115', '116', '117', '118', '119', '125', '126', '127',
       # '133', '137', '141', '142', '147', '150', '151', '153', '154', '155',
       # '156', '158', '160', '161', '163', '164', '165', '166', '167', '169',
       # '171', '174', '182', '185', '186', '187', '188', '192', '198', '200',
       # '201', '203', '207', '209', '210', '219', '231', '234', '245', '246',
       # '251', '253', '264', '289', '290', '295', '298', '300'],
        class_names=['1', '0'],
        rounded=True,
        filled=True
        # node_ids = True
    )
#
with open(check + ".dot") as f:
    dot_graph = f.read()


dot = graphviz.Source(dot_graph)
dot.format = 'png'
dot.render(filename=check, directory='images/dm', cleanup=True)
dot
