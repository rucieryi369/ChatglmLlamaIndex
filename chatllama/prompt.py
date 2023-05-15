from llama_index.prompts.prompts import QuestionAnswerPrompt

DEFAULT_PROMPT=(
         """基于以下已知信息，简洁和专业的来回答用户的问题。如果无法从中得到答案，请说 "根据已知信息无法回答该问题" 或 "没有提供足够的相关信息"，不允许在答案中添加编造成分，答案请使用中文。已知内容:{context_str}问题:{query_str}"""
        )
DEFAULT_PROMPT1 = (
    "We have provided context information below: \n"
    "---------------------\n"
    "{context_str}\n"
    "---------------------\n"
    "Given this information, Please answer my question in the same language that I used to ask you.\n"
    "Please answer the question: {query_str}\n"
)


def get_prompt():
    return QuestionAnswerPrompt(DEFAULT_PROMPT)
