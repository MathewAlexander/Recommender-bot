call activate pbot
python -m rasa_core.train -d domain.yml -s stories.md -o models/dialogue --endpoints endpoints.yml
python -m rasa_nlu.train -c nlu_config.yml --data nlu.md -o models --fixed_model_name nlu --project current --verbose
python -m rasa_core.run  --core models/dialogue --nlu models/current/nlu  --endpoints endpoints.yml --credentials credentials.yml