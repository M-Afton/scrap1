import openai
openai.api_key = "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"

class TextProcessor:
    def openai_translate(self, text):
        
        # Make a translation request
        translation = openai.Completion.create(
            engine='davinci',
            prompt=text,
            max_tokens=300,
            temperature=0.7,
        )

        # Get the translated text from the response
        translated_text = translation.choices[0].text.strip()

        return translated_text

    def openai_text_summary(self, text):
        # Make a summarization request
        summarization = openai.Completion.create(
            engine='davinci',
            prompt=text,
            max_tokens=150,
            temperature=0.3,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0,
            stop=None,
            n=1,
            log_level=None,
            logprobs=None,
            echo=False,
            logit_bias=None,
        )

        # Get the summarized text from the response
        summarized_text = summarization.choices[0].text.strip()

        return summarized_text

    def openai_text_generator(self, theme, content):
        # Set the prompt for text generation
        prompt = f"Theme: {theme}\nContent: {content}\nGenerate Text:"

        # Make a text generation request
        response = openai.Completion.create(
            engine='gpt-3.5-turbo',
            prompt=prompt,
            max_tokens=100,
            temperature=0.7,
            n=1,
        )

        # Get the generated text from the response
        generated_text = response.choices[0].text.strip()

        return generated_text

    def openai_codex(self, code):
        # Make a code completion request
        completion = openai.Completion.create(
            engine='davinci-codex',
            prompt=code,
            max_tokens=100,
            temperature=0.7,
            n=1,
        )

        # Get the corrected code from the response
        corrected_code = completion.choices[0].text.strip()

        return corrected_code

    def openai_image(self, prompts):
        # Make an image generation request

        # Generate image from text
        image_generation = openai.Image.create(
            #prompt="a white siamese cat",
            prompt=prompts,
            n=1,
            size="512x512"
        )
        image_url = image_generation['data'][0]['url']
        image_url

        return image_url
