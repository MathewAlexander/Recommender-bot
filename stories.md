## story_greet <!--- The name of the story. It is not mandatory, but useful for debugging. --> 
* greet <!--- User input expressed as intent. In this case it represents users message 'Hello'. --> 
 - utter_name <!--- The response of the chatbot expressed as an action. In this case it represents chatbot's response 'Hello, how can I help?' --> 
 
## story_goodbye
* goodbye
 - utter_goodbye

## story_thanks
* thanks
 - utter_thanks
 
## story_name
* name{"name":"Sam"}
 - utter_greet
 
## story_Perfume_like
* greet
 - utter_name
* name{"name":"Lucy"} <!--- User response with an entity. In this case it represents user message 'My name is Lucy.' --> 
 - utter_greet
* rec_perfume
 - utter_ask_perf_price
* price_perfume{"price_above":"2000"} OR price_perfume{"price_below":"4000"} OR price_perfume{"price_above":2000,"price_below":4000} OR price_perfume{"price_range":"5000"}
 - utter_ask_accord
* accord_perfume{"accord":"woody"}
 - slot{"accord": "woody"}
 - action_perf_suggestion
 - utter_feedback_suggestion
* like_suggestion
 -utter_goodbye


## story_Perfume_dislike
* greet
 - utter_name
* name{"name":"Lucy"} <!--- User response with an entity. In this case it represents user message 'My name is Lucy.' --> 
 - utter_greet
* rec_perfume
 - utter_ask_perf_price
* price_perfume{"price_above":"2000"} OR price_perfume{"price_below":"4000"} OR price_perfume{"price_above":2000,"price_below":4000} OR price_perfume{"price_range":"5000"}
 - utter_ask_accord
* accord_perfume{"accord":"woody"}
 - slot{"accord": "woody"}
 - action_perf_suggestion
 - utter_feedback_suggestion
* dislike_suggestion
 -utter_goodbye


