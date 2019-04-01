from sklearn.naive_bayes import GaussianNB

# create naive bayes classifier
gaunb = GaussianNB()

# create dataset
X = [[121, 80, 44], [180, 70, 43], [166, 60, 38], [153, 54, 37], [166, 65, 40], [190, 90, 47], [175, 64, 39],
     [174, 71, 40], [159, 52, 37], [171, 76, 42], [183, 85, 43]]

Y = ['male', 'male', 'female', 'female', 'male', 'male', 'female', 'female', 'female', 'male', 'male']

num_array = list()
num = raw_input("Enter how many elements you want:")
print 'Enter numbers in array: '
for i in range(int(num)):
    n = raw_input("num :")
    num_array.append(int(n))
print 'ARRAY: ',num_array

# train classifier with dataset
gaunb = gaunb.fit(X, Y)

# predict using classifier
prediction = gaunb.predict([num_array])
print(prediction)
