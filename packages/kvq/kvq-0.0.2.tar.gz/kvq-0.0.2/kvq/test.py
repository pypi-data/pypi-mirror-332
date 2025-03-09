import sys

from kvq import KVQ

sys.path.append("/mnt/rds/VipinRDS/VipinRDS/users/mxh1029/common")

import torch
from llm import generate_hf, load_model, model_info, model_props
from llm.helpers import gpu_usage_load_model, set_seed
from llm.inference import (
    generate,
    generate_dynamic,
    generate_static,
    generate_static_update,
    sampling,
)

model_name_hf = "meta-llama/Llama-3.2-1B-Instruct"


load_params = {
    "torch_dtype": torch.bfloat16,
    "compile_model": False,
    # "attn_implementation": "flash_attention_2",
}
model, tokenizer, model_name = load_model(model_repo=model_name_hf, **load_params)

input_prompt = "How are you today?"


@torch.inference_mode()
def gen_quant(model, tokenizer, input_text, nbits_k, nbits_v, max_new_tokens):

    custom_cache = KVQ(
        {
            "backend": "quanto",
            "nbits_k": nbits_k,
            "nbits_v": nbits_v,
            "axis_key": 0,
            "axis_value": 0,
            "q_group_size": 32,
            "residual_length": 64,
            "compute_dtype": torch.float16,
            "device": model.device,
        }
    )

    # input_text = "What is the meaning of life?"
    inputs = tokenizer(input_text, return_tensors="pt").to(model.device)
    generated_ids = inputs["input_ids"]
    input_tokens_len = len(generated_ids[0])

    cache_position = torch.arange(
        inputs["input_ids"].shape[1], dtype=torch.int64, device=model.device
    )

    for _ in range(max_new_tokens):

        outputs = model(
            **inputs,
            cache_position=cache_position,
            past_key_values=custom_cache,
            use_cache=True,
        )

        # Greedily select the token with the highest probability from the last time step.
        next_token = outputs.logits[:, -1].argmax(dim=-1, keepdim=True)

        # Append the new token to the generated sequence.
        generated_ids = torch.cat([generated_ids, next_token], dim=-1)

        # Update the attention mask by appending a 1 for the new token.
        new_attention = torch.ones(
            (inputs["attention_mask"].shape[0], 1),
            dtype=inputs["attention_mask"].dtype,
            device=model.device,
        )
        new_attention_mask = torch.cat(
            [inputs["attention_mask"], new_attention], dim=-1
        )

        # For autoregressive generation, the new input is just the newly generated token.
        inputs = {"input_ids": next_token, "attention_mask": new_attention_mask}

        # Update cache_position: the next token’s position is the last element + 1.
        cache_position = cache_position[-1:] + 1

    # Decode and print the generated sequence
    generated_text = tokenizer.decode(
        generated_ids[0][input_tokens_len:], skip_special_tokens=True
    )

    del custom_cache
    del outputs
    torch.cuda.empty_cache()

    return generated_text


nbits_k = 2
nbits_v = 2
max_new_tokens = 50

out = gen_quant(model, tokenizer, input_prompt, nbits_k, nbits_v, max_new_tokens)

print(out)
