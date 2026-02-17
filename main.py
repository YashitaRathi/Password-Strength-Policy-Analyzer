from unittest import result, skip
from flask import app
import config
import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from password_checker import checkPassword
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.factory import Factory
from policy_analyzer import policy_analyzer, NIST_rules
from kivy.core.window import Window
from kivy.properties import StringProperty
Window.title = "NIST Password Strength Analyzer"

kivy.require('2.3.1')
Window.size = (750, 800)


def show_popup_result(self, result):
    strength = result['strength']
    points = result['points'] if result["issues"] else "0"
    issues = "\n | " + \
        "\n |" .join(result['issues']) if result["issues"] else "None"
    suggestions = "\n | " + "\n | " .join(
        result['suggestions']) if result["suggestions"] else "None"
    context = BoxLayout(orientation="vertical", padding=20, spacing=10)
    context.add_widget(
        Label(text=f"Strength of your password: {strength} ", markup=True))
    context.add_widget(
        Label(text=f"Point of your password: {points} ", markup=True))
    context.add_widget(
        Label(text=f"Issues in your password: {issues} ", markup=True))
    context.add_widget(
        Label(text=f"Suggestions for your password: {suggestions} ", markup=True))

    close_btn = Button(text="Close", size_hint=(1, None), height=50)
    context.add_widget(close_btn)

    popup = Popup(title="Password Analysis Result",
                  content=context, size_hint=(0.85, 0.7), auto_dismiss=False)
    close_btn.bind(on_release=popup.dismiss)
    popup.open()


def analyze_password(self, pwd):
    result = checkPassword(pwd)
    popup = Factory.AnalysisResult()
    popup.ids.strength_label.text = f"Strength: {result['strength']}"
    popup.ids.points_label.text = f"Points: {result['points']}"
    issues = "\n > " + \
        "\n > " .join(result['issues']) if result["issues"] else "None"
    suggestions = "\n > " + "\n > " .join(
        result['suggestions']) if result["suggestions"] else "None"
    popup.ids.issues_label.text = f"Issues: {issues}"
    popup.ids.suggestions_label.text = f"Suggestions: {suggestions}"

    popup.open()


def analyze_policy(self):
    screen = self.root.get_screen("Policy Analyzer")
    ids = screen.ids

    policy = {
        "min_length": int(ids.min_length.text or 0),
        "max_length": int(ids.max_length.text or 0),
        "password_requirement": ids.requirement.active,
        "password_expiration": ids.expiration.active,
        "password_blocklist": ids.blocklist.active,
        "no_security_question": not ids.security_question.active,
        "login_attempts": int(ids.login.text or 0),
        "passphrase_support": ids.passphrase.active,
        "mfa_applied": ids.mfa.active
    }

    result = policy_analyzer(policy, NIST_rules)

    popup = Factory.PoliyPasswordPopup()
    popup.ids.rating_label.text = f"Rating: {result['rating']}"
    popup.ids.score_label.text = f"Score: {result['score']}"
    issues = "\n > " + \
        "\n > " .join(result['issues']) if result['issues'] else "None"
    suggestions = "\n > " + \
        "\n > " .join(result['suggestions']
                      ) if result['suggestions'] else "None"
    popup.ids.issues_label.text = f"Issues: {issues}"
    popup.ids.suggestions_label.text = f"Suggestions: {suggestions}"
    popup.open()


def input_details(self):
    popup = Factory.UserDetails()
    popup.open()


class WelcomePage(Screen):
    pass


class PasswordAnalyzer(Screen):
    pass


class OrganizationPolicyChecker(Screen):
    pass


class PersonalInfoPage(Screen):
    password = StringProperty("")

    def set_password(self, pwd):
        self.password = pwd

    def submit_details(self, skip=False):

        password = self.password

        if skip:
            result = checkPassword(password)
        else:
            personal_info = {
                "name": self.ids.name_input.text,
                "birth_year": self.ids.birth_input.text,
                "pet": self.ids.pet_input.text,
                "common": self.ids.common_input.text
            }

            result = checkPassword(password, personal_info)

        app = App.get_running_app()
        app.show_analysis_popup(result)

        self.manager.current = "Password Analyzer"


screen_manager = ScreenManager()
screen_manager.add_widget(WelcomePage(name='Welcome Page'))
screen_manager.add_widget(PasswordAnalyzer(name='Password Analyzer'))
screen_manager.add_widget(OrganizationPolicyChecker(name='Policy Analyzer'))
screen_manager.add_widget(PersonalInfoPage(name='Personal Info'))


class PasswordChecker(App):
    current_password = ""

    def build(self):
        return Builder.load_file('Screens\passwordchecker.kv')

    def analyze_password(self, pwd):
        self.current_password = pwd
        screen = self.root.get_screen("Personal Info")
        screen.set_password(pwd)
        self.root.current = "Personal Info"

    def analyze_policy(self):
        analyze_policy(self)

    def input_details(self):
        input_details(self)

    def show_analysis_popup(self, result):
        popup = Factory.AnalysisResult()
        popup.ids.strength_label.text = f"Strength: {result['strength']}"
        popup.ids.points_label.text = f"Points: {result['points']}"

        issues = "\n > " + \
            "\n > ".join(result['issues']) if result["issues"] else "None"
        suggestions = "\n > " + \
            "\n > ".join(result['suggestions']
                         ) if result["suggestions"] else "None"

        popup.ids.issues_label.text = f"Issues: {issues}"
        popup.ids.suggestions_label.text = f"Suggestions: {suggestions}"

        popup.open()


if __name__ == "__main__":
    PasswordChecker().run()
