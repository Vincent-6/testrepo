{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 57,
   "id": "af486826",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: ibm_watson in ./opt/anaconda3/lib/python3.8/site-packages (5.2.2)\n",
      "Requirement already satisfied: wget in ./opt/anaconda3/lib/python3.8/site-packages (3.2)\n",
      "Requirement already satisfied: ibm-cloud-sdk-core==3.*,>=3.3.6 in ./opt/anaconda3/lib/python3.8/site-packages (from ibm_watson) (3.10.1)\n",
      "Requirement already satisfied: requests<3.0,>=2.0 in ./opt/anaconda3/lib/python3.8/site-packages (from ibm_watson) (2.25.1)\n",
      "Requirement already satisfied: python-dateutil>=2.5.3 in ./opt/anaconda3/lib/python3.8/site-packages (from ibm_watson) (2.8.1)\n",
      "Requirement already satisfied: websocket-client==1.1.0 in ./opt/anaconda3/lib/python3.8/site-packages (from ibm_watson) (1.1.0)\n",
      "Requirement already satisfied: PyJWT<3.0.0,>=2.0.1 in ./opt/anaconda3/lib/python3.8/site-packages (from ibm-cloud-sdk-core==3.*,>=3.3.6->ibm_watson) (2.1.0)\n",
      "Requirement already satisfied: six>=1.5 in ./opt/anaconda3/lib/python3.8/site-packages (from python-dateutil>=2.5.3->ibm_watson) (1.15.0)\n",
      "Requirement already satisfied: chardet<5,>=3.0.2 in ./opt/anaconda3/lib/python3.8/site-packages (from requests<3.0,>=2.0->ibm_watson) (4.0.0)\n",
      "Requirement already satisfied: urllib3<1.27,>=1.21.1 in ./opt/anaconda3/lib/python3.8/site-packages (from requests<3.0,>=2.0->ibm_watson) (1.26.4)\n",
      "Requirement already satisfied: certifi>=2017.4.17 in ./opt/anaconda3/lib/python3.8/site-packages (from requests<3.0,>=2.0->ibm_watson) (2020.12.5)\n",
      "Requirement already satisfied: idna<3,>=2.5 in ./opt/anaconda3/lib/python3.8/site-packages (from requests<3.0,>=2.0->ibm_watson) (2.10)\n"
     ]
    }
   ],
   "source": [
    "!pip install ibm_watson wget"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "id": "8df47850",
   "metadata": {},
   "outputs": [],
   "source": [
    "from ibm_watson import LanguageTranslatorV3\n",
    "from ibm_cloud_sdk_core.authenticators import IAMAuthenticator"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "id": "e7aefe64",
   "metadata": {},
   "outputs": [],
   "source": [
    "url_lt='https://api.eu-de.language-translator.watson.cloud.ibm.com/instances/fa569bdf-c8a6-4923-872f-3428ab62d4ae'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "id": "98f4b621",
   "metadata": {},
   "outputs": [],
   "source": [
    "apikey_lt='ZvdcqxFTdMv--BUvtosO0lZ2MoXLQAxW5S1FNc6IbPKF'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "94fbce17",
   "metadata": {},
   "outputs": [],
   "source": [
    "#version_lt='2018-05-01'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "id": "a089d7f3",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<ibm_watson.language_translator_v3.LanguageTranslatorV3 at 0x105173bb0>"
      ]
     },
     "execution_count": 61,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "authenticator = IAMAuthenticator(apikey_lt)\n",
    "language_translator = LanguageTranslatorV3(version=version_lt,authenticator=authenticator)\n",
    "language_translator.set_service_url(url_lt)\n",
    "language_translator"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "id": "a310a326",
   "metadata": {},
   "outputs": [],
   "source": [
    "def englishtofrench(text_en):\n",
    "    translation_response = language_translator.translate(text_en, model_id='en-fr')\n",
    "    translation = translation_response.get_result()\n",
    "    text_fr = translation['translations'][0]['translation']\n",
    "    return text_fr"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "id": "94bd55db",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Bonjour'"
      ]
     },
     "execution_count": 63,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "englishtofrench(\"hello\")"
   ]
  },
  {
   "cell_type": "raw",
   "id": "cb4ca204",
   "metadata": {},
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
