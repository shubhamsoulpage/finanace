#!/usr/bin/env python
# coding: utf-8

# In[1]:


#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

gender={'male':1,'female':0}
married={'yes':1,'no':0}
graduate={'no':1,'yes':0}
employed={'yes':1,'no':0}
credit={'yes':1,'no':0}
property_type={'rural':0,'urban':2,'semi urban':1}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [x for x in request.form.values()]
    a=int_features[0]
    aa=gender[a]
    b=int_features[1]
    bb=married[b]
    cc=int(int_features[2])
    d=int_features[3]
    dd=graduate[d]
    e=int_features[4]
    ee=employed[d]
    ff=int(int_features[5])
    gg=int(int_features[6])
    hh=int(int_features[7])
    ii=int(int_features[8])
    j=int_features[9]
    jj=credit[d]
    k=int_features[10]
    kk=property_type[k]
    apple=[aa,bb,cc,dd,ee,ff,gg,hh,ii,jj,kk]
    final_features = [np.array(apple)]
    prediction = model.predict(final_features)
    output = round(prediction[0])
    change=""
    if output==1:
    	change='eligible'
    elif output==0:
    	change='not eligible'

    return render_template('index.html', prediction_text= 'The applicant is {} .'.format(change))

@app.route('/predict_api',methods=['POST'])
def predict_api():
    '''
    For direct API calls trought request
    '''
    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)


# In[ ]:





# In[ ]:




