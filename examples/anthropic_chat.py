"""Profile 03-anthropic. Set ANTHROPIC_API_KEY and ANTHROPIC_MODEL."""
import os
from anthropic import Anthropic
r=Anthropic().messages.create(model=os.environ['ANTHROPIC_MODEL'],max_tokens=256,messages=[{'role':'user','content':'Explain an agent loop in two sentences.'}])
for b in r.content:
 if b.type=='text':print(b.text)
