from D_ID import Clips # pip install did-api 

api_key = '<api_key>'
d_id = Clips(api_key)

# Create a text-to-video clip
text = "Hello, D-ID!"
result = d_id.create_text_to_video_clip(text)
"""
result => {'id': 'clip_id', 'created_at': '2023-09-06T21:45:50.298Z', 'object': 'clip', 'status': 'created'}
"""
print(result)
clip_id = result['id']


# Get information about a specific clip
clip_id = "your_clip_id_here"
clip_info = d_id.get_clip_by_id(clip_id)
print(clip_info)

