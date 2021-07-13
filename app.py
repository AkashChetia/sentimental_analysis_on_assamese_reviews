# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 05:48:22 2021

@author: Reckon Mazumdar
"""
##Importing required libraries
import streamlit as st
import pickle
import nltk

#Function to clean the text
def transform_text(text):
    text=nltk.word_tokenize(text)
    stop=['অতএব', 'অথচ', 'অথবা', 'অধঃ', 'অন্ততঃ', 'অৰ্থাৎ', 'অৰ্থে', 'আও', 'আঃ', 'আচ্ছা', 'আপাততঃ', 'আয়ৈ', 'আৰু',
      'আস্', 'আহা', 'আহাহা', 'ইতস্ততঃ', 'ইতি', 'ইত্যাদি', 'ইস্', 'ইহ', 'উঃ', 'উৱা', 'উস্', 'এতেকে', 'এথোন',
      'ঐ', 'ওঁ', 'ওৰফে', 'ঔচ্', 'কি', 'কিম্বা', 'কিন্তু', 'কিয়নো', 'কেলেই', 'চোন', 'ছাৰি', 'ছিকৌ', 'ছেই',
      'ঠাহ্', 'ঢেঁট্', 'তত', 'ততক', 'ততেক', 'তেতেক', 'ততেক', 'তত্ৰাচ', 'তথা', 'তথৈবচ', 'তাতে', 'তেও',
      'তো', 'তৌৱা', 'দেই', 'দেহি', 'দ্বাৰা', 'ধৰি', 'ধিক্', 'নতুবা', 'নি', 'নো', 'নৌ', 'পৰা', 'পৰ্যন্ত',
      'বৰঞ্চ', 'বহিঃ', 'বাবে', 'বাৰু', 'বাহ্', 'বাহিৰে', 'বিনে', 'বে', 'মতে', 'যথা', 'যদি', 'যদ্যপি', 'যে',
      'যেনিবা', 'যেনে', 'যোগে', 'লৈ', 'সত্ত্বে', 'সমন্ধি', 'সম্প্ৰতি', 'সহ', 'সু', 'সেইদেখি', 'সৈতে', 'স্বতঃ', 'হঞে', 'হতুৱা', 'হন্তে',
      'হবলা', 'হয়', 'হা', 'হুঁ', 'হুই', 'হে', 'হেই', 'হেঃ', 'হেতুকে', 'হেনে', 'হেনো', 'হেৰ', 'হেৰি', 'হৈ', 'হোঁ', 'ইঃ', 'ইচ্',
      'চুহ্', 'চুঃ', 'আঁ']
    punc="!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~।"
    puncword=[]
    for i in punc:
         puncword.append(i)
    y=[]
    for i in text:
        if i not in stop and i not in punc:
            y.append(i)
    text=y[:]
    y.clear()
    for i in text:
        i=''.join(j for j in i if not j in puncword)
        y.append(i)
    return " ".join(y)

#Loading the model and vectorizer
tfidf = pickle.load(open('vectorizer.pkl','rb'))
model = pickle.load(open('model.pkl','rb'))

#App title
st.title("Assamese song review sentiment analyzer")

#Text box
ip_sentence=st.text_area("Enter the assamese sentence")

if st.button('Predict'):
    #Taking input and Cleaning the text
    transformed_sentence=transform_text(ip_sentence)
    #Vectorizing
    vec=tfidf.transform([transformed_sentence])
    #predicting result and displaying it
    result= model.predict(vec)[0]
    if result == 1:
        st.header("Positive😇")
    else:
        st.header("Negative☹️")
