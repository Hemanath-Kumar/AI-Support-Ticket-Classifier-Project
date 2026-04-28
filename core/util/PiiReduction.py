
import re

masked_data = {}
def process(text):
        # Block API key
        if re.search(r"sk-[a-zA-Z0-9]{32}", text):
            raise ValueError("API key detected!")

        # Redact email
        if re.search(r'\b[\w\.-]+@[\w\.-]+\.\w+\b', text):
              mail=re.findall(r'\b[\w\.-]+@[\w\.-]+\.\w+\b', text)
              masked_data['email']=mail
              for m in mail:
                text=re.sub(m, f'[MASKED_EMAIL_{mail.index(m)}]', text)
            

        # Mask credit card
        if re.search(r'\b\d{4}-?\d{4}-?\d{4}-?\d{4}\b', text):
             card=re.findall(r'\b\d{4}-?\d{4}-?\d{4}-?\d{4}\b', text)
             masked_data['credit_card']=card
             for c in card:
                text = re.sub(c, f'[MASKED_CREDIT_CARD_{card.index(c)}]', text)

        # text = re.sub(r'\b\d{4}-?\d{4}-?\d{4}-?\d{4}\b', '[MASKED_CREDIT_CARD]', text)

        return {"processed_question_for_llm": text, "masked_data": masked_data}

if __name__ == "__main__":
    print(process("""Hi, my name is Rahul Sharma. You can reach me at rahul.sharma1998@gmail.com for any updates. 
    I recently made a payment using my credit card 4532-9876-1234-5678. 
    If needed, you can also contact my colleague Priya at priya.work@company.com."""))



