call activate rbot
python -m rasa_core.train -d domain.yml -s stories.md -o models/dialogue

python -m rasa_core.run  --core models/dialogue --nlu models/current/nlu  --endpoints endpoints.yml --credentials credentials.yml