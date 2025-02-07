from llm_helper import llm
from few_shots import FewShotPosts

few_shot = FewShotPosts()


def get_length_str(length):
    if length == "Short":
        return "1 to 5 lines"
    if length == "Medium":
        return "6 to 10 lines"
    if length == "Long":
        return "11 to 15 lines"


def generate_post(length, language, tag):
    prompt = get_prompt(length, language, tag)
    response = llm.invoke(prompt)
    return response.content


def get_prompt(length, language, tag):
    length_str = get_length_str(length)

    prompt = f"""
    You are an expert LinkedIn post writer. Generate a compelling LinkedIn post based on the following details:

    - **Topic**: {tag}
    - **Length**: {length_str}
    - **Language**: {language} (but always write in English)
    
    The post should be:
    - Engaging, thought-provoking, and professional.
    - Well-structured with a **strong opening**, valuable insights, and a call to action.
    - Written in an **authentic and conversational tone** suitable for LinkedIn.

    """

    examples = few_shot.get_filtered_posts(length, language, tag)

    if examples:
        prompt += "\n### **Examples for Writing Style**"

    for i, post in enumerate(examples[:2]):  # Use max 2 examples
        post_text = post['text']
        prompt += f'\n\n#### Example {i+1}:\n{post_text}'

    prompt += "\n\n### **Now, generate the post.**"
    
    return prompt



if __name__ == "__main__":
    print(generate_post("Medium", "English", "Mental Health"))