import litellm
import os
from litellm import batch_completion
import litellm
import pandas as pd
from more_itertools import batched
# litellm._turn_on_debug()
df = pd.read_parquet('snr_prompts_20250414.parquet')
os.environ['OPENROUTER_API_KEY'] = ""
qrys = []
for _,row in df.iterrows():
    qrys.append([{'role':'user','content':row.o_prompt}])

fs = []
rs = []

i = 0
for batch in batched(qrys,100):
    i+=1
    responses = batch_completion(
        model="openrouter/deepseek/deepseek-r1",
        # model='openrouter/meta-llama/llama-3.2-1b-instruct',
        messages = batch,
        provider= {
            'order':['Lambda']
        },
        max_tokens=8192*4
    )


    for res in responses:
        try:
            final = res.choices[0].message.content
        except:
            final = None

        try:
            reasoning = res.choices[0].message.reasoning_content
        except:
            reasoning = None

        fs.append(final)
        rs.append(reasoning)

    batch_df = df[:len(fs)]
    batch_df['o_r1_response']=fs
    batch_df['o_r1_reasoning']=rs
    
    batch_df.to_parquet('snr_o_r1_log2.parquet',index=False)
 
