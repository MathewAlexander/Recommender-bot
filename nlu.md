<!--- Make sure to update this training data file with more training examples from https://forum.rasa.com/t/grab-the-nlu-training-dataset-and-starter-packs/903 --> 

## intent:bye <!--- The label of the intent --> 
- Bye 			<!--- Training examples for intent 'bye'--> 
- Goodbye
- See you later
- Bye bot
- Goodbye friend
- bye
- bye for now
- catch you later
- gotta go
- See you
- goodnight
- have a nice day
- i'm off
- see you later alligator
- we'll speak soon

## intent:greet
- Hi
- Hey
- Hi bot
- Hey bot
- Hello
- Good morning
- hi again
- hi folks
- hi Mister
- hi pal!
- hi there
- greetings
- hello everybody
- hello is anybody there
- hello robot

## intent:thank
- Thanks
- Thank you
- Thank you so much
- Thanks bot
- Thanks for that
- cheers
- cheers bro
- ok thanks!
- perfect thank you
- thanks a bunch for everything
- thanks for the help
- thanks a lot
- amazing, thanks
- cool, thanks
- cool thank you

## intent:affirm
- yes
- yes sure
- absolutely
- for sure
- yes yes yes
- definitely


## intent:name
- My name is [Juste](name)  <!--- Square brackets contain the value of entity while the text in parentheses is a a label of the entity --> 
- I am [Josh](name)
- I'm [Lucy](name)
- People call me [Greg](name)
- It's [David](name)
- Usually people call me [Amy](name)
- My name is [John](name)
- You can call me [Sam](name)
- Please call me [Linda](name)
- Name name is [Tom](name)
- I am [Richard](name)
- I'm [Tracy](name)
- Call me [Sally](name)
- I am [Philipp](name)
- I am [Charlie](name)
- my name is [Shanid](name)
- people call me [Shanid](name)
- [Mathew](name) here
- i am [Nihal](name)
- it's me [Shanid](name)
- this is [Devadath](name)
- My name is [juste](name)  <!--- Square brackets contain the value of entity while the text in parentheses is a a label of the entity --> 
- I am [josh](name)
- I'm [lucy](name)
- People call me [greg](name)
- It's [david](name)
- Usually people call me [amy](name)
- My name is [john](name)
- You can call me [sam](name)
- Please call me [linda](name)
- Name name is [tom](name)
- I am [richard](name)
- I'm [tracy](name)
- Call me [sally](name)
- I am [philipp](name)
- I am [charlie](name)
- [Rafi](name)
- [fitha](name)


## intent:joke
- Can you tell me a joke?
- I would like to hear a joke
- Tell me a joke
- A joke please
- Tell me a joke please
- I would like to hear a joke
- I would loke to hear a joke, please
- Can you tell jokes?
- Please tell me a joke
- I need to hear a joke

## intent:rec_perfume
- Suggest me a perfume
- i need a perfume
- i want a perfume
- please suggest me a perfume
- what are some good perfumes
- i want you to suggest me a perfume

## intent:price_perfume
- it should  within [7000](price_below) 
- it should above [5000](price_above)
- a perfume between [3000](price_above) and [4000](price_below)
- [3000](price_above) to  [4000](price_below)
- a perfume between [2000](price_above) and [7000](price_below)
- i need a perfume under [3000](price_below)
- it should be under [4000](price_below)
- the price should be below [5000](price_below)
- the price should be above [3000](price_above)
- pice above [3000](price_above)
- price should be between [4000](price_above) and [5000](price_below)
- [5000](price_range) range
- it should be in the range of [7000](price_range)
- it should be in [3000](price_range) range
- perfume in [3000](price_range) range
- perfume of [400](price_range)
- perfume of [5000](price_range) rs
- perfume of [5000](price_range) rupees
- [3500](price_range) rupees
- [3500](price_range) rs
- [5000](price_range)

## intent:accord_perfume
- A perfume with [woody](accord) smell
- a perfume  with [floral](accord) note 
- suggest me a perfume with [woody](accord) 
- [floral](accord) smell
- [woody](accord) smell
- [woody](accord) note
- [fruity](accord) smell
- i need a [spicy](accord) perfume
- i need a [woody](accord) perfume
- i need a [fruity](accord) perfume
- i need a [floral](accord) perfume
- i need a [citrus](accord) perfume
- i need a [leather](accord) perfume
- i need an [aromatic](accord) perfume
- i need a [sweet](accord) perfume
- a perfume of [sweet](accord) smell
- [fruity](accord)
- [woody](accord)
- [woody](accord) smell
- [floral](accord) smell
- [citrus](accord) smell

## like_suggestion
- Yes
- yes
- it's Ok
- seems good
- ok
- Wonderfull
- yes i am 
- awesome
- cool

## dislike_suggestion
- No
- no
- aweful
- very bad
- not at all
- Not a good suggestion
- 