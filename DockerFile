FROM python:2-onbuild
EXPOSE 5000
CMD [ "python", "./myhero_data/myhero_data.py" ]

