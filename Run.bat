call activate rbot
python -m rasa_core.run  --core models/dialogue --nlu models/current/nlu  --endpoints endpoints.yml --credentials credentials.yml