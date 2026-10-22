"""Profile 19-model-dev. Requires a separately downloaded complete local model."""
import os
os.environ['HF_HUB_OFFLINE']='1'
from transformers import AutoTokenizer,AutoModelForCausalLM
model_dir=os.environ['LOCAL_MODEL_DIR']
tok=AutoTokenizer.from_pretrained(model_dir,local_files_only=True)
model=AutoModelForCausalLM.from_pretrained(model_dir,local_files_only=True)
inputs=tok('Explain what an agent is:',return_tensors='pt')
outputs=model.generate(**inputs,max_new_tokens=48)
print(tok.decode(outputs[0],skip_special_tokens=True))
