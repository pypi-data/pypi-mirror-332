from typing import Optional
from print_color import print
import time
from semantic_router.layer import RouteLayer
from semantic_router import Route
import os
from semantic_router.encoders import CohereEncoder, OpenAIEncoder, MistralEncoder, FastEmbedEncoder
from semantic_router.llms import MistralAILLM, OpenAILLM


class CustomOpenAILLM(OpenAILLM):
    base_url: Optional[str]

    def __init__(
        self,
        name: Optional[str] = None,
        openai_api_key: Optional[str] = None,
        temperature: float = 0.01,
        max_tokens: int = 200,
        base_url: Optional[str] = None,
    ):
        super().__init__(name, openai_api_key, temperature, max_tokens)
        self.base_url = base_url

        if base_url is not None:
            self.client.base_url = base_url


# we could use this as a guide for our chatbot to avoid political conversations
politics = Route(
    name="politics",
    utterances=[
        "isn't politics the best thing ever",
        "why don't you tell me about your political opinions",
        "don't you just love the president",
        "they're going to destroy this country!",
        "they will save the country!",
    ],
)

# this could be used as an indicator to our chatbot to switch to a more
# conversational prompt
chitchat = Route(
    name="chitchat",
    utterances=[
        "how's the weather today?",
        "how are things going?",
        "lovely weather today",
        "the weather is horrendous",
        "let's go to the chippy",
    ],
    score_threshold=0.3,
    llm=CustomOpenAILLM(
        openai_api_key="7kcEQJ6tfSRNwUxbcioCxEdTmCDLpGUHRPY6WxWPuIgstver",
        base_url="https://api.fireworks.ai/inference/v1",
        name="accounts/fireworks/models/firefunction-v1",
    )
)

# we place both of our decisions together into single list
routes = [politics, chitchat]

# or for OpenAI
os.environ["OPENAI_API_KEY"] = "<YOUR_API_KEY>"
openai_encoder = OpenAIEncoder(
    # openai_api_key="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",
    # name="text-embedding-3-small",
    openai_api_key="7kcEQJ6tfSRNwUxbcioCxEdTmCDLpGUHRPY6WxWPuIgstver",
    openai_base_url="https://api.fireworks.ai/inference/v1",
    name="nomic-ai/nomic-embed-text-v1.5",
    dimensions=768
)

mist_encoder = MistralEncoder(
    mistralai_api_key="Uv8jED45NE9pu7rO0AkeD9gobB0mJUjY"
)

fastem_encoder = FastEmbedEncoder()

rl = RouteLayer(
    encoder=fastem_encoder,
    # encoder=openai_encoder,
    # encoder=mist_encoder,
    routes=routes,

)

while 1:
    inp = input("You: ")
    if inp != "":
        t0 = time.time()
        resp = rl(inp)
        print("Response: ", resp)
        t1 = time.time() - t0
        # print("AI responded in : {:.2f} milliseconds".format(t1 * 1000), color='blue')
        print("time taken {:.2f} ms ".format(
            t1 * 1000), color="green")
    else:
        print("\t A valid input is required!")
