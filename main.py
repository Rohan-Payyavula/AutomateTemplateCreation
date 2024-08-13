from langchain_openai import ChatOpenAI
import csv
import os


templates = [
    "Are you experiencing *symptoms 1*? If it persists, it's a good idea to have a conversation with your doctor. Also, be attentive to any sensations of *symptoms 2*. Keeping your healthcare provider informed about your symptoms is crucial, especially when it comes to potential signs of *health condition*.",
    "Would you kindly consider including *nutrition advice*? Prioritize *healthy eating habits*. Avoid *food items*. Additionally, seeking guidance from a dietitian can greatly assist you in planning balanced meals. Your well-being matters!",
    "Could you kindly ensure you're maintaining *a balanced diet*? Please refrain from *bad habits*. It would be beneficial to monitor your *vital signs* regularly. Remember to take your *medication as prescribed*. Additionally, it's advisable to engage in *regular exercise*. Your well-being is important, and these measures can contribute positively to your health.",
    "How are you feeling today? *Managing health condition* can be tough. It's okay to *have moments when you're not feeling your best*. Remember to *take time for yourself* and prioritize your mental well-being. If you ever need someone to talk to or share your struggles with, I'm here for you. Take care.",
    "Have you ever wondered how *disease is diagnosed*? Procedures like *tests can reveal* crucial information. Just something to be aware of, especially for your well-being.",
    "Hey, have you checked your *vitals* today? Monitoring these regularly is crucial for effectively managing *your condition*. Take care of yourself.",
    "Hey, ever wondered *how disease impacts your health*? Understanding *the disease* can make a big difference. Knowing the *signs* can help you stay on top of your health. Let's work together to navigate this journey and prioritize your well-being.",
    "Hey, have you scheduled your *annual risk assessment*? Getting your *vitals* checked is crucial. Let's prioritize your health by staying proactive!",
    "Hey, do you know that monitoring your *risk* regularly is crucial for preventing complications? Keeping track of your *vitals* can help you stay ahead of any potential problems and manage your condition effectively. Let's make sure to schedule your *risk assessment* to prioritize your health!",
    "Are you taking proactive measures to *ensure good health condition*? It's vital to *follow your healthcare provider's guidance* closely, including *medical adherence*."
]


class FAQGenerator:
    def __init__(self, api_key):
        self.llm = ChatOpenAI(api_key=api_key)

    def generate_filled_templates(self, topic):
        filled_templates = [template.replace('*', topic) for template in templates]
        return filled_templates

    def generate_detailed_content(self, filled_template, topic):
        prompt = f"Expand on this by filling out the blanks represented by ** on the topic {topic}: {filled_template}"
        response = self.llm.invoke(prompt)
        return response.content
input("Give the site link: //#pass#This is the codemain code")
    def save_to_csv(self, filename, topic, filled_templates, detailed_contents):
        file_exists = os.path.isfile(filename)

        with open(filename, 'a', newline='') as file:
            writer = csv.writer(file)
            if not file_exists:
                # Write header
                writer.writerow(["Topic", "Template", "Detailed Content"])

            for template, content in zip(filled_templates, detailed_contents):
                writer.writerow([topic, template, content])


def main():
    pass


if __name__ == "__main__":
    main()
