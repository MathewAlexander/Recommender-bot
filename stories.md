## story_greet <!--- The name of the story. It is not mandatory, but useful for debugging. --> 
* greet <!--- User input expressed as intent. In this case it represents users message 'Hello'. --> 
 - utter_name <!--- The response of the chatbot expressed as an action. In this case it represents chatbot's response 'Hello, how can I help?' --> 
 
## story_goodbye
* goodbye
 - utter_goodbye


 
## story_name
* name{"name":"Sam"}
 - utter_greet
 - utter_suggestion_options



## quit_suggestion_and_feedback
* dont_try_again
 - utter_goodbye

 
## story_Perfume_Quiz
* greet
 - utter_name
* name{"name":"Lucy"} <!--- User response with an entity. In this case it represents user message 'My name is Lucy.' --> 
 - utter_greet
 - utter_suggestion_options
* take_quiz
 - utter_ask_perf_price
* price_perfume{"price_above":"2000"} OR price_perfume{"price_below":"4000"} OR price_perfume{"price_above":2000,"price_below":4000} OR price_perfume{"price_range":"5000"}
 - utter_ask_accord
* accord_perfume{"accord":"woody"}
 - utter_ask_trail
* silage_perfume{"sillage":"High"}
 - action_perf_suggestion
 - utter_ask_try_again
* try_again
 - utter_suggestion_options
* take_quiz
 - utter_ask_perf_price
* price_perfume{"price_above":"2000"} OR price_perfume{"price_below":"4000"} OR price_perfume{"price_above":2000,"price_below":4000} OR price_perfume{"price_range":"5000"}
 - utter_ask_accord
* accord_perfume{"accord":"woody"}
 - utter_ask_trail
* silage_perfume{"sillage":"High"}
 - action_perf_suggestion
 - utter_ask_try_again
* try_again
 - utter_suggestion_options


## story_Quick_Suggest
* greet
 - utter_name
* name{"name":"Lucy"} <!--- User response with an entity. In this case it represents user message 'My name is Lucy.' --> 
 - utter_greet
 - utter_suggestion_options
* quick_suggest
 - utter_ask_perf_price
* price_perfume{"price_above":"2000"} OR price_perfume{"price_below":"4000"} OR price_perfume{"price_above":2000,"price_below":4000} OR price_perfume{"price_range":"5000"}
 - utter_ask_accord
* accord_perfume{"accord":"woody"}
 - action_perf_suggestion
 - utter_ask_try_again
* try_again
 - utter_suggestion_options
* quick_suggest
 - utter_ask_perf_price
* price_perfume{"price_above":"2000"} OR price_perfume{"price_below":"4000"} OR price_perfume{"price_above":2000,"price_below":4000} OR price_perfume{"price_range":"5000"}
 - utter_ask_accord
* accord_perfume{"accord":"woody"}
 - action_perf_suggestion
 - utter_ask_try_again
* try_again
 - utter_suggestion_options


