class ActionFramework:
    def __init__(self):
        self.goal = None
        self.situation = None
        self.preferences = None
        self.standards = None

    def set_goal(self, goal):
        self.goal = goal

    def set_situation(self, situation):
        self.situation = situation

    def set_preferences(self, preferences):
        self.preferences = preferences

    def set_standards(self, standards):
        self.standards = standards

    def generate_prompt(self):
        prompt = f"Given the goal to {self.goal} about {self.situation}, with preferences leaning towards {self.preferences}, adhering to the following standards: {self.standards}, how would you respond?"
        return prompt


class Chatbot:
    def __init__(self):
        self.user_preferences = {}
        self.action_framework = ActionFramework()

    def interact(self, message):
        topic = self.detect_topic(message)
        self.user_preferences[topic] = self.user_preferences.get(topic, 0) + 1
        response = self.generate_response(topic, self.action_framework.generate_prompt())
        return response


class SpeechTherapyChatbot(Chatbot):
    def analyze_speech(self, audio_input):
        feedback = self.speech_analysis_model(audio_input)
        return feedback


class EmotionalChatbot(Chatbot):
    def analyze_emotion(self, message):
        emotion = self.sentiment_analysis_model(message)
        response = self.generate_response(emotion, self.action_framework.generate_prompt())
        return response


class EngagementChatbot(Chatbot):
    def track_engagement(self, message):
        engagement_level = self.engagement_model(message)
        return engagement_level


class PromptChatbot(Chatbot):
    def send_reminder(self, reminder_time, reminder_message):
        self.schedule_reminder(reminder_time, reminder_message)


class BreakChatbot(Chatbot):
    def set_break(self, activity_time, break_time):
        self.schedule_break(activity_time, break_time)
