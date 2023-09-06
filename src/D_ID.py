import requests,json


class __D_ID:
    def __init__(self,api_key:str) -> None:
        try:
            split_key = api_key.split(':')
            username = split_key[0]
            password = split_key[1]
        except Exception as e:
            raise 'API key should contain a colon. Format-> username:password'
        
        self.username = username
        self.password = password
        self.base_url = 'https://api.d-id.com/'
        self.headers = {
            'Content-Type' : 'application/json',
            'Accept' : 'application/json',
            'Authorization' : 'Basic ' + username + ':' + password
        }
        
class Clips(__D_ID):
    def __init__(self, api_key: str) -> None:
        super().__init__(api_key)
        self.endpoint = 'clips/'
        self.url = self.base_url + self.endpoint
        
    def get_actor_list(self) -> dict:
        url = self.url + 'actors' # https://api.d-id.com/clips/actors
        
        response  = requests.get(url=url,headers=self.headers)
        
        return response.json()
    
    def get_driver_list_of_an_actor(self,id:str) -> dict:
        url = self.url + 'actors/'+ id +'/drivers' # https://api.d-id.com/clips/actors/<id>/drivers
        
        response = requests.get(url, headers=self.headers)
        
        return response.json()
    
    def get_list_of_the_presenter(self,limit:int=100) -> dict:
        url = self.url + 'presenters/' + '?limit=' + str(limit) # https://api.d-id.com/clips/presenters
        
        response = requests.get(url, headers=self.headers)
        
        return response.json()
    
    def get_presenter_by_id(self,id:str) -> dict:
        url = self.url + 'presenters/' +  str(id) # https://api.d-id.com/clips/presenters/<id>
        
        response = requests.get(url, headers=self.headers)
        
        return response.json()
    
    def get_clips(self,limit:int=100) -> dict:
        url = self.url + '?limit=' +  str(limit) # https://api.d-id.com/clips?limit=100
        
        response = requests.get(url, headers=self.headers)
        
        return response.json()
    
    def get_clip_by_id(self,id:str) -> dict:
        url = self.url +  str(id) # https://api.d-id.com/clips/<id>
        
        response = requests.get(url, headers=self.headers)
        
        return response.json()
    
    def delete_a_clip(self,id:str) -> dict:
        url = self.url +  str(id) # https://api.d-id.com/clips/<id>
        
        response = requests.delete(url, headers=self.headers)
        
        return response.json()
    
    def get_presenter_driver_by_id(self,id:str) -> dict:
        url = self.url + 'presenters/' +  str(id) + '/drivers' # https://api.d-id.com/clips/presenters/id/drivers
        
        response = requests.get(url, headers=self.headers)
        
        return response.json()
    
    
    def create_text_to_video_clip(self,text:str,presenter_id:str='amy-jcwCkr1grs',driver_id:str='uM00QMwJ9x',voice_provider_name='microsoft',voice_id:str='en-US-JennyNeural',WEBHOOK_URL=None,background_color:str='#ffffff',extra_data={}) -> dict:

        url = self.url # https://api.d-id.com/clips/

        payload = {
            "presenter_id": presenter_id,
            "driver_id": driver_id,
            "script": {
                "type": "text",
                "subtitles": False,
                "provider": {
                    "type": voice_provider_name,
                    "voice_id": voice_id
                },
                "ssml": False,
                "input": text
            },
            "config": { "result_format": "mp4" },
            "user_data" : json.dumps(extra_data),
            "background": { "color": background_color }
            
        }
        if WEBHOOK_URL:
            payload['webhook'] = WEBHOOK_URL
        response = requests.post(url, json=payload, headers=self.headers)

        return response.json()