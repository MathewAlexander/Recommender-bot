# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging
import requests
import json
from rasa_core_sdk import Action
import pandas as pd

logger = logging.getLogger(__name__)


class ActionJoke(Action):
    def name(self):
        # define the name of the action which can then be included in training stories
        return "action_perf_suggestion"

    def run(self, dispatcher, tracker, domain):
        # what your action should do
        df=pd.read_csv('Perfume_data.csv')
        df.reset_index(inplace=True)
        
        print(tracker.get_slot('accord'))
        print(tracker.get_slot('price_above'))
        print(tracker.get_slot('price_below'))
        print(tracker.get_slot('price_range'))
        try:
            df=df.loc[df['predominant_accord'] == tracker.get_slot('accord')]
            print('accord')
            print(df)
        except:
        	pass
        try:
            df=df.loc[df['Price'] <= int(tracker.get_slot('price_range'))+1000]
            df=df.loc[df['Price'] >= int(tracker.get_slot('price_range'))-500]
            print('range')
            print(df)
        except Exception as Err:
            print(Err)
        if tracker.get_slot('price_range')==None:
            try:
                
                df=df.loc[df['Price'] <= int(tracker.get_slot('price_below'))]
                print('below')
                print(df)
            except Exception as Err:
                print(Err)
            try:
                
                df=df.loc[df['Price'] >= int(tracker.get_slot('price_above'))]
                print('price_above')
                print(df)
            except Exception as Err:
            	print(Err)

        

        try:
        	perfume= str([i for i in df['Perfume']])
            
        	print(perfume)
        	print(type(perfume))
        	dispatcher.utter_message(perfume)
        except Exception as err:
        	print(v)
        	
        	# print(df['Perfume'])